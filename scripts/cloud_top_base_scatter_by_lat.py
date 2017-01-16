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

from lib.spark.map import select, lon_rel, h5, filter_cloudsat_quality, split, unzip, hdfeos
from lib.spark.filter import not_empty
from lib.spark.misc import mask_datasets


lat_bins = np.linspace(-90, 90, 19)
sample_size = 100000


# def cloud_top_base():
#     def f(data):
#         max_layers = data['datasets']['layer_top'].shape[1]
#         data['datasets']['cloud_top_base'] = np.zeros((0, 2), np.float)
#         for i in range(max_layers):
#             mask = data['datasets']['cloud_layers'] >= i + 1
#             cloud_top_base_i = np.zeros((np.sum(mask), 2), np.float)
#             cloud_top_base_i[:, 0] = data['datasets']['layer_base'][mask, i]
#             cloud_top_base_i[:, 1] = data['datasets']['layer_top'][mask, i]
#             data['datasets']['cloud_top_base'] = np.concatenate(
#                 (data['datasets']['cloud_top_base'], cloud_top_base_i),
#                 axis=0
#             )
#         return data
#     return f


def lat_histogram():
    def f(data):
        data['lat_histogram'] = np.histogram(
            data['datasets']['lat'],
            bins=lat_bins,
            weights=data['datasets']['cloud_layers']
        )[0]
        return data
    return f


if __name__ == '__main__':
    sc = SparkContext(appName='CloudTopBaseScatterPlotByLat')

    parser = argparse.ArgumentParser(description='Cloud top/base scatter plot by latitude')
    parser.add_argument('-g', dest='files', type=str, help='input files glob', nargs='?')
    parser.add_argument('-o', dest='output', type=str, help='output plot')

    args = parser.parse_args()

    filenames = glob.glob(args.files)

    data = [{'filename': x} for x in filenames]

    rdd = sc.parallelize(data) \
        .map(unzip()) \
        .map(hdfeos({
            'data_quality': {
                'swath': '2B-GEOPROF-LIDAR',
                'dataset': 'Data_quality'
            },
            'layer_top': {
                'swath': '2B-GEOPROF-LIDAR',
                'dataset': 'LayerTop'
            },
            'layer_base': {
                'swath': '2B-GEOPROF-LIDAR',
                'dataset': 'LayerBase'
            },
            'cloud_layers': {
                'swath': '2B-GEOPROF-LIDAR',
                'dataset': 'CloudLayers'
            },
            'lat': {
                'swath': '2B-GEOPROF-LIDAR',
                'dataset': 'Latitude'
            },
            'lon': {
                'swath': '2B-GEOPROF-LIDAR',
                'dataset': 'Longitude'
            },
            'flag_top': {
                'swath': '2B-GEOPROF-LIDAR',
                'dataset': 'FlagTop'
            },
            'flag_base': {
                'swath': '2B-GEOPROF-LIDAR',
                'dataset': 'FlagBase'
            }
        })) \
        .filter(not_empty('lon')) \
        .map(filter_cloudsat_quality('data_quality')) \
        .map(lat_histogram())

    lat_histogram = rdd \
        .map(select('lat_histogram')) \
        .reduce(np.add)

    sample_fraction = sample_size/lat_histogram

    # rdd \
    #     .map(sample(sample_fraction))
    #     .map(cloud_top_base())

    print(lat_histogram)

    #     .map(cloud_top_base()) \
    #     .map(select('datasets/cloud_top_base')) \

    # point_groups = rdd.collect()
    # points = np.concatenate(point_groups, axis=0)
    # npoints = points.shape[0]
    # indexes = np.random.choice(npoints, 100000, replace=False)
    # points_sample = points[indexes]

    # #plt.figure(figsize=(10, 10))

    # plt.scatter(points_sample[:, 0], points_sample[:, 1],
    #     s=1,
    #     marker='.',
    #     edgecolors='none'
    # )

    # if args.output:
    #     plt.savefig(args.output, dpi=600)
    # else:
    #     plt.show()

    sc.stop()
