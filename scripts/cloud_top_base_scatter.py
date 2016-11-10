from __future__ import print_function

import sys
import os
from os import path
import glob
import argparse
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import gridspec
from pyspark import SparkContext

sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from lib.spark.map import select, lon_rel, h5, filter_cloudsat_quality, split
from lib.spark.filter import not_empty
from lib.spark.misc import mask_datasets


heights = np.linspace(0, 15000, 100)


def cloud_top_base():
    def f(data):
        max_layers = data['datasets']['layer_top'].shape[1]
        data['datasets']['cloud_top_base'] = np.zeros((0, 2), np.float)
        for i in range(max_layers):
            mask = data['datasets']['cloud_layers'] >= i + 1
            cloud_top_base_i = np.zeros((np.sum(mask), 2), np.float)
            cloud_top_base_i[:, 0] = data['datasets']['layer_base'][mask, i]
            cloud_top_base_i[:, 1] = data['datasets']['layer_top'][mask, i]
            data['datasets']['cloud_top_base'] = np.concatenate(
                (data['datasets']['cloud_top_base'], cloud_top_base_i),
                axis=0
            )
        return data
    return f


if __name__ == '__main__':
    sc = SparkContext(appName='Profile')

    parser = argparse.ArgumentParser(description='Cloud top/base scatter plot')
    parser.add_argument('files', metavar='FILES', type=str,
                       help='HDF5 input files', nargs='*')
    parser.add_argument('-o', dest='output', type=str,
                       help='output plot')

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
            'cloud_layers': {
                'dataset': 'cloud_layers'
            },
            'lat': {
                'dataset': 'lat'
            },
            'lon': {
                'dataset': 'lon'
            },
            'flag_top': {
                'dataset': 'flag_top'
            }
        })) \
        .filter(not_empty('lon')) \
        .map(filter_cloudsat_quality('data_quality')) \
        .map(cloud_top_base()) \
        .map(select('datasets/cloud_top_base')) \

    point_groups = rdd.collect()
    points = np.concatenate(point_groups, axis=0)
    npoints = points.shape[0]
    indexes = np.random.choice(npoints, 100000, replace=False)
    points_sample = points[indexes]

    #plt.figure(figsize=(10, 10))

    plt.scatter(points_sample[:, 0], points_sample[:, 1],
        s=1,
        marker='.',
        edgecolors='none'
    )

    if args.output:
        plt.savefig(args.output, dpi=600)
    else:
        plt.show()

    sc.stop()
