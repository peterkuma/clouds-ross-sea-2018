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


heights = np.arange(0, 15000)


def cloud_layers_hist():
    def f(data):
        hist = np.bincount(data['datasets']['cloud_layers'], minlength=10)
        data['datasets']['cloud_layers_hist'] = hist
        return data
    return f


if __name__ == '__main__':
    sc = SparkContext(appName='CloudLayersHist')

    parser = argparse.ArgumentParser(description='Cloud layers histogram')
    parser.add_argument('files', metavar='FILES', type=str, help='HDF5 input files', nargs='*')
    parser.add_argument('-o', dest='output', type=str, help='output')
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
        }
    }

    rdd = sc.parallelize(data) \
        .map(h5(dataset_names)) \
        .filter(not_empty('lon')) \
        .map(filter_cloudsat_quality('data_quality')) \
        .map(filter_coggins_regime(args.regime)) \
        .map(filter_season(args.season)) \
        .flatMap(split(10000))

    cloud_layers_hist = rdd \
        .map(cloud_layers_hist()) \
        .map(select('datasets/cloud_layers_hist')) \
        .sum()

    with h5py.File(args.output, 'w') as f:
        f.create_dataset('cloud_layers_hist', data=cloud_layers_hist)

    sc.stop()
