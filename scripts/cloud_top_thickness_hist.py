from __future__ import print_function

import sys
import os
from os import path
import argparse
import numpy as np
import h5py
from pyspark import SparkContext

sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from lib.spark.map import h5, select, filter_cloudsat_quality, split, cloudsat_daynight, filter_daynight, filter_coggins_regime, filter_season
from lib.spark.filter import not_empty


height_bins = np.linspace(0, 15000, 61)
thickness_bins = np.linspace(0, 15000, 61)


def cloud_top_thickness_hist():
    def f(data):
        layer_top = data['datasets']['layer_top']
        layer_base = data['datasets']['layer_base']
        cloud_layers = data['datasets']['cloud_layers']
        n = cloud_layers.shape[0]
        max_layers = layer_top.shape[1]
        cloud_thickness = layer_top - layer_base

        top = []
        thickness = []
        for i in xrange(n):
            for j in xrange(cloud_layers[i]):
                top.append(layer_top[i, j])
                thickness.append(cloud_thickness[i, j])

        hist = np.histogram2d(
            np.array(top),
            np.array(thickness),
            bins=[height_bins, thickness_bins]
        )[0]
        data['datasets']['cloud_top_thickness_hist'] = hist
        return data
    return f


if __name__ == '__main__':
    sc = SparkContext(appName='CloudIncidence')

    parser = argparse.ArgumentParser(description='Cloud types histogram')
    parser.add_argument('files', metavar='FILES', type=str, help='HDF5 input files', nargs='*')
    parser.add_argument('-o', dest='output', type=str, help='output')
    parser.add_argument('-n', dest='daynight', type=int, help='day/night only (0 - night, 1 - day)')
    parser.add_argument('-r', dest='regime', type=str, help='Coggins regime')
    parser.add_argument('-s', dest='season', type=str, help='season')

    args = parser.parse_args()

    data = [{'filename': x} for x in args.files]

    dataset_names = {
        'data_quality': {
            'dataset': 'data_quality'
        },
        'cloud_layers': {
            'dataset': 'cloud_layers'
        },
        'lat': {
            'dataset': 'lat'
        },
        'lon': {
            'dataset': 'lon'
        },
        'time': {
            'dataset': 'time'
        },
        'layer_top': {
            'dataset': 'layer_top'
        },
        'layer_base': {
            'dataset': 'layer_base'
        }
    }

    rdd = sc.parallelize(data) \
        .map(h5(dataset_names)) \
        .filter(not_empty('lon')) \
        .map(filter_cloudsat_quality('data_quality')) \
        .map(filter_coggins_regime(args.regime)) \
        .map(filter_season(args.season)) \
        .flatMap(split(10000))
        # .sample(False, 0.01, 1)

    if args.daynight is not None:
        rdd = rdd \
            .map(cloudsat_daynight()) \
            .map(filter_daynight(args.daynight))

    cloud_top_thickness_hist = rdd \
        .map(cloud_top_thickness_hist()) \
        .map(select('datasets/cloud_top_thickness_hist')) \
        .reduce(np.add)

    with h5py.File(args.output, 'w') as f:
        f.create_dataset(
            'cloud_top_thickness_hist',
            data=cloud_top_thickness_hist
        )

    sc.stop()
