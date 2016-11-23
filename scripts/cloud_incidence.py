from __future__ import print_function

import sys
import os
from os import path
import argparse
import numpy as np
import h5py
from pyspark import SparkContext

sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from lib.spark.map import h5, select, filter_cloudsat_quality, split
from lib.spark.filter import not_empty


heights = np.arange(0, 15000)


def cloud_incidence1(heights, top, base):
    w = top.size
    h = heights.size
    top_idx = np.searchsorted(heights, top)
    base_idx = np.searchsorted(heights, base)
    hist = np.zeros(h, np.int64)
    for i in range(w):
        hist[base_idx[i]:top_idx[i]] += 1
    return hist


def cloud_incidence():
    def f(data):
        w = data['datasets']['lon'].size
        h = heights.size
        data['datasets']['cloud_incidence'] = np.zeros(h, np.int64)
        heightsx = np.tile(heights, (w, 1))
        max_layers = data['datasets']['layer_top'].shape[1]
        for i in range(max_layers):
            top = data['datasets']['layer_top'][:, i]
            base = data['datasets']['layer_base'][:, i]
            mask = (top >= 0) & (base >= 0)
            topx = top[mask]
            basex = base[mask]
            data['datasets']['cloud_incidence'] += cloud_incidence1(heights, topx, basex)
        return data
    return f


if __name__ == '__main__':
    sc = SparkContext(appName='CloudIncidence')

    parser = argparse.ArgumentParser(description='Cloud incidence histogram')
    parser.add_argument('files', metavar='FILES', type=str,
                       help='HDF5 input files', nargs='*')
    parser.add_argument('-o', dest='output', type=str,
                       help='output')

    args = parser.parse_args()

    data = [{'filename': x} for x in args.files]

    rdd = sc.parallelize(data) \
        .map(h5({
            'data_quality': {
                'dataset': 'data_quality'
            },
            'layer_top': {
                'dataset': 'layer_top'
            },
            'layer_base': {
                'dataset': 'layer_base'
            },
            'lat': {
                'dataset': 'lat'
            },
            'lon': {
                'dataset': 'lon'
            }
        })) \
        .filter(not_empty('lon')) \
        .map(filter_cloudsat_quality('data_quality')) \
        .flatMap(split(10000)) \
        .map(cloud_incidence())

    cloud_incidence = rdd \
        .map(select('datasets/cloud_incidence')) \
        .reduce(np.add)

    cloud_incidence_total = rdd \
        .map(select('datasets/lon')) \
        .map(lambda x: x.size) \
        .sum()

    with h5py.File(args.output, 'w') as f:
        f.create_dataset('cloud_incidence', data=cloud_incidence)
        f.create_dataset('cloud_incidence_total', data=cloud_incidence_total)

    sc.stop()
