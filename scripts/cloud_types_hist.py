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


def cloud_types_hist():
    def f(data):
        cloud_type = data['datasets']['cloud_type']
        cloud_layers = data['datasets']['cloud_layers']
        w = cloud_type.shape[0]
        max_layers = cloud_type.shape[1]
        hist = np.zeros(257, np.int64)

        for i in xrange(w):
            mask = 0
            for j in xrange(cloud_layers[i]):
                mask |= 1 << (cloud_type[i, j])
            hist[mask] += 1

        data['datasets']['cloud_types_hist'] = hist
        return data
    return f


if __name__ == '__main__':
    sc = SparkContext(appName='CloudTypesHist')

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
        'cloud_type': {
            'dataset': 'cloud_type'
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

    cloud_types_hist = rdd \
        .map(cloud_types_hist()) \
        .map(select('datasets/cloud_types_hist')) \
        .reduce(np.add)

    with h5py.File(args.output, 'w') as f:
        f.create_dataset('cloud_types_hist', data=cloud_types_hist)

    sc.stop()
