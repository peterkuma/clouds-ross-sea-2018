import sys
import os
from os import path
import h5py
import glob
import argparse
from pyspark import SparkContext
import numpy as np

sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from lib import h5_save
from lib.spark.map import unzip, hdfeos, expect, filter_cloudsat_quality, include, select
from lib.spark.filter import not_empty, not_bad


lon = np.linspace(-180, 180, 39)
lat = np.linspace(-90, 90, 37)


def cloud_mask(name, height):
    def f(data):
        top = data['datasets']['layer_top'][::]
        base = data['datasets']['layer_base'][::]
        mask = (base <= height) & (top >= height)
        data['datasets'][name] = np.sum(mask, axis=1) > 0
        return data
    return f


def cloud_incidence(cloud_incidence_name, cloud_mask_name):
    def f(data):
        cloud_mask = data['datasets'][cloud_mask_name]
        data['datasets'][cloud_incidence_name] = np.histogram2d(
            data['datasets']['lon'][cloud_mask],
            data['datasets']['lat'][cloud_mask],
            bins=[lon, lat]
        )[0]
        data['datasets'][cloud_incidence_name + '_total'] = np.histogram2d(
            data['datasets']['lon'],
            data['datasets']['lat'],
            bins=[lon, lat]
        )[0]
        return data
    return f


def reduce():
    def f(d1, d2):
        data = {
            'datasets': {
                k: np.add(d1['datasets'][k], d2['datasets'][k])
                for k in d1['datasets'].keys()
            }
        }
        return data
    return f


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Global correction factor')
    parser.add_argument('files', metavar='FILES', type=str,
                       help='files glob', nargs='?')
    parser.add_argument('-f', dest='file', type=str,
                       help='file containing list of files')
    parser.add_argument('-o', dest='outfile', type=str,
                       help='output h5 file', required=True)

    args = parser.parse_args()

    if args.file:
        filenames = [x.strip() for x in open(args.file).readlines()]
    else:
        filenames = glob.glob(args.files)

    sc = SparkContext(appName='GlobalCorrectionFactor')

    data = [{'filename': x} for x in filenames]

    rdd = sc.parallelize(data) \
        .map(expect(unzip())) \
        .map(expect(hdfeos({
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
            }
        }))) \
        .filter(not_bad()) \
        .map(filter_cloudsat_quality('data_quality')) \
        .filter(not_empty('lon')) \
        .map(cloud_mask('cloud_mask_1', 8000)) \
        .map(cloud_mask('cloud_mask_2', 8300)) \
        .map(cloud_incidence('cloud_incidence_1', 'cloud_mask_1')) \
        .map(cloud_incidence('cloud_incidence_2', 'cloud_mask_2')) \
        .map(include([
            'cloud_incidence_1',
            'cloud_incidence_2',
            'cloud_incidence_1_total',
            'cloud_incidence_2_total'
        ]))

    data = rdd.reduce(reduce())

    data['datasets']['lon'] = lon[:-1]
    data['datasets']['lat'] = lat[:-1]

    try:
        os.remove(args.outfile)
    except OSError:
        pass

    f = h5_save(args.outfile)
    f(data)

    sc.stop()
