from __future__ import print_function

import sys
import os
from os import path
import glob
import argparse
import numpy as np
from matplotlib import pyplot as plt
from pyspark import SparkContext

sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from lib.spark.map import select, lon_rel, h5, filter_cloudsat_quality
from lib.spark.filter import not_empty


heights = np.hstack([-np.inf, np.linspace(0, 15000, 16), np.inf])
longitudes_rel = np.linspace(0, 50, 22)


def cloud_top(flag_top=None):
    def f(data):
        layer_top = data['datasets']['layer_top']
        if flag_top is not None:
            mask = data['datasets']['flag_top'] == flag_top
            layer_top[~mask] = -99
        data['datasets']['cloud_top'] = np.amax(layer_top, axis=1)
        return data
    return f


def cloud_top_histogram():
    def f(data):
        data['datasets']['cloud_top_histogram'] = np.histogram2d(
            data['datasets']['cloud_top'],
            data['datasets']['lon_rel'],
            bins=[
                heights,
                longitudes_rel
            ]
        )[0]
        return data
    return f


if __name__ == '__main__':
    sc = SparkContext(appName='CloudTopDist')

    parser = argparse.ArgumentParser(description='Cloud top histogram')
    parser.add_argument('files', metavar='FILES', type=str,
                       help='HDF5 input files', nargs='*')
    parser.add_argument('-i', dest='instrument', type=int,
                       help='plot only cloud tops with given instrument flag')
    parser.add_argument('-o', dest='output', type=str,
                       help='output plot')
    parser.add_argument('-t', dest='title', type=str,
                       help='plot title')

    args = parser.parse_args()

    data = [{'filename': x} for x in args.files]

    freq = sc.parallelize(data) \
        .map(h5({
            'data_quality': {
                'dataset': 'data_quality'
            },
            'layer_top': {
                'dataset': 'layer_top'
            },
            'cloud_layers': {
                'dataset': 'cloud_layers'
            },
            'flag_top': {
                'dataset': 'flag_top'
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
        .map(lon_rel(160, 1)) \
        .map(cloud_top(flag_top=args.instrument)) \
        .map(cloud_top_histogram()) \
        .map(select('datasets/cloud_top_histogram')) \
        .reduce(np.add)

    hist = freq[1:, :]/np.sum(freq)*22

    plt.imshow(
        hist,
        interpolation='nearest',
        origin='lower',
        vmin=0,
        vmax=0.25
    )
    plt.colorbar()

    if args.title:
        plt.title(args.title)

    if args.output:
        plt.savefig(args.output)
    else:
        plt.show()

    sc.stop()
