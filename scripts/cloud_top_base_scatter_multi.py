from __future__ import print_function

import sys
import os
from os import path
import glob
import argparse
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import gridspec
import h5py
import json
import string
from pyspark import SparkContext

sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from lib.spark.map import select, h5, filter_cloudsat_quality
from lib.spark.filter import not_empty


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


def plot_panel(
    filename,
    show_xaxis=True,
    show_yaxis=True,
    annotation=None
):
    data = [{'filename': filename}]

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
            }
        })) \
        .filter(not_empty('lon')) \
        .map(filter_cloudsat_quality('data_quality')) \
        .map(cloud_top_base())

    point_groups = rdd \
        .map(select('datasets/cloud_top_base')) \
        .collect()
    points = np.concatenate(point_groups, axis=0)
    npoints = points.shape[0]
    indexes = np.random.choice(npoints, 100000, replace=False)
    points_sample = points[indexes]

    # points_sample = np.zeros((1,2), dtype=np.float)

    plt.scatter(
        (points_sample[:, 0] + np.random.normal(0, 10, points_sample.shape[0]))/1000.0,
        (points_sample[:, 1] + np.random.normal(0, 10, points_sample.shape[0]))/1000.0,
        s=1,
        marker='.',
        edgecolors='none',
        color='#1124c0',
        alpha=0.25
    )

    plt.xlim(-1, 21)
    plt.ylim(-1, 21)

    plt.grid()

    if show_xaxis:
        plt.xlabel('Cloud Base (km)')
    else:
        plt.gca().set_xticklabels([])

    if show_yaxis:
        plt.ylabel('Cloud Top (km)')
    else:
        plt.gca().set_yticklabels([])

    if annotation is not None:
        plt.annotate(
            annotation,
            xy=(0, 1),
            xytext=(5, -5),
            ha='left',
            va='top',
            xycoords='axes fraction',
            textcoords='offset points',
            weight='bold'
        )


if __name__ == '__main__':
    sc = SparkContext(appName='Cloud top-base scatter plot (multi)')

    parser = argparse.ArgumentParser(description='Cloud top/base scatter plot (multi)')
    parser.add_argument('-c', dest='config', type=str, help='config file', required=True)
    parser.add_argument('-o', dest='output', type=str, help='output plot')

    args = parser.parse_args()

    config = json.load(open(args.config))

    nrows = len(config['panels'])
    ncols = len(config['panels'][0])

    plt.figure(figsize=(10, 8))
    plt.rcParams['font.family'] = 'Open Sans'

    gs = gridspec.GridSpec(
        nrows,
        ncols,
        wspace=0,
        hspace=0
    )

    for i, row in enumerate(config['panels']):
        for j, filename in enumerate(row):
            plt.subplot(gs[i*ncols + j])
            plot_panel(
                filename,
                show_xaxis=(i == nrows - 1),
                show_yaxis=(j == 0),
                annotation=string.lowercase[i * ncols + j]
            )

            if i == 0:
                plt.annotate(config['xlabels'][j],
                    xy=(0.5, 1.08), xytext=(0, 0),
                    xycoords=('axes fraction', 'axes fraction'),
                    textcoords='offset points',
                    size=14,
                    ha='center',
                    va='center',
                    weight='bold'
                )

            if j == 0:
                plt.annotate(config['ylabels'][i],
                    xy=(-0.25, 0.5), xytext=(0, 0),
                    xycoords=('axes fraction', 'axes fraction'),
                    textcoords='offset points',
                    size=14,
                    ha='left',
                    va='center',
                    weight='bold'
                )

    if args.output:
        plt.savefig(args.output, bbox_inches='tight')
    else:
        plt.show()

    sc.stop()
