from __future__ import print_function

import sys
import os
from os import path
import glob
import argparse
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import gridspec
from matplotlib import colors
from pyspark import SparkContext

sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from lib.spark.map import select, h5, filter_cloudsat_quality, split
from lib.spark.filter import not_empty
from lib.spark.misc import mask_datasets


heights = np.linspace(0, 15000, 100)

sample_size = 1000
samples_count  = 8


def profile(flag=None):
    def f(data):
        w = data['datasets']['lon'].size
        h = heights.size
        data['datasets']['profile'] = np.zeros((w, h), np.byte)
        max_layers = data['datasets']['layer_top'].shape[1]
        heightsx = np.tile(heights, (w, 1))
        data['datasets']['heightsx'] = heightsx.shape
        for i in range(max_layers):
            top = data['datasets']['layer_top'][:, i]
            base = data['datasets']['layer_base'][:, i]
            # flag_top = data['datasets']['flag_top'][:, i]
            # flag_base = data['datasets']['flag_base'][:, i]
            # if flag is not None:
            #     mask = data['datasets']['flag_top'][:, i] == flag
            #     top[~mask] = -99
            #     base[~mask] = -99
            topx = np.tile(top, (h, 1)).T
            basex = np.tile(base, (h, 1)).T
            # flag_topx = np.tile(flag_top, (h, 1)).T
            # flag_basex = np.tile(flag_base, (h, 1)).T
            mask = (heightsx < topx) & (heightsx > basex)
            data['datasets']['profile'][mask] = 1
        return data
    return f


def load(filenames):
    data = [{'filename': x} for x in filenames]
    return sc.parallelize(data) \
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
            }
        })) \
        .filter(not_empty('lon')) \
        .map(filter_cloudsat_quality('data_quality'))


def profile_sample(groups):
    rdds = [
        load(group['filenames'])
        for group in groups
    ]

    times = [
        rdd.select('datasets/time').collect()
        for rdd in rdds
    ]

    time = reduce(lambda a, b: np.intersect1d(a, b, True), times)
    n = time.size/sample_size
    sample_indexes = np.random.choice(range(n))

    time_sample = [
        time[i:(i + sample_size)]
        for i in sample_indexes
    ]

    samples = [
        np.searchsorted(t, time_sample)
        for t in times
    ]





if __name__ == '__main__':
    sc = SparkContext(appName='Profile')

    parser = argparse.ArgumentParser(description='Profile')
    parser.add_argument('files', metavar='FILES', type=str,
                       help='HDF5 input files', nargs='*')
    parser.add_argument('-o', dest='output', type=str,
                       help='output plot')
    parser.add_argument('-s', dest='sample', type=int,
                       help='sample size')


    args = parser.parse_args()

    data = [{'filename': x} for x in args.files]

    sample_size = args.sample if args.sample > 0 else 10000

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
            # 'flag_top': {
            #     'dataset': 'flag_top'
            # },
            # 'flag_base': {
            #     'dataset': 'flag_base'
            # }
        })) \
        .filter(not_empty('lon')) \
        # .flatMap(split(1000)) \
        # .sample(False, 0.1) \
        .map(filter_cloudsat_quality('data_quality')) \
        # .map(profile(flag=2)) \
        # .map(select('datasets/profile'))

    time =


    profiles = rdd.takeSample(False, 10, seed=1)

    plt.subplots(nrows=10, ncols=1, figsize=(20, 20))
    plt.subplots_adjust(hspace=.001)

    cmap = colors.ListedColormap(['white', 'black', 'blue', 'red'])
    norm = colors.BoundaryNorm([-0.5, 0.5, 1.5, 2.5, 3.5], cmap.N)

    gs = gridspec.GridSpec(10, 1)
    i = 0
    for profile in profiles:
        print(profile)
        plt.subplot(gs[i, 0])
        i = i + 1
        plt.imshow(
            profile.T,
            interpolation='nearest',
            origin='lower',
            cmap=cmap,
            norm=norm,
            extent=[0, profile.shape[0], heights[0], heights[-1]],
            aspect='auto'
        )
        plt.axhline(8200)

    if args.output:
        plt.savefig(args.output, dpi=600)
    else:
        plt.show()

    sc.stop()
