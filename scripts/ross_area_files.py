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

from lib.spark.map import unzip, hdfeos, filter_area, select, expect
from lib.spark.filter import not_empty, not_bad
from lib.areas import is_ross_area


DATASETS = {
    '2b-geoprof-lidar': {
        'lat': {
            'swath': '2B-GEOPROF-LIDAR',
            'dataset': 'Latitude'
        },
        'lon': {
            'swath': '2B-GEOPROF-LIDAR',
            'dataset': 'Longitude'
        }
    },
    '2b-cldclass-lidar': {
        'lat': {
            'swath': '2B-CLDCLASS-LIDAR',
            'dataset': 'Latitude'
        },
        'lon': {
            'swath': '2B-CLDCLASS-LIDAR',
            'dataset': 'Longitude'
        }
    }
}


if __name__ == '__main__':
    sc = SparkContext(appName='RossAreaFiles')

    parser = argparse.ArgumentParser(description='Ross area files')
    parser.add_argument('files', metavar='FILES', type=str, help='files glob')
    parser.add_argument('-p', dest='product_type', type=str, help='product type ("2b-geoprof-lidar" or "2b-cldclass-lidar", default "2b-geoprof-lidar")', default='2b-geoprof-lidar')

    args = parser.parse_args()

    filenames = glob.glob(args.files)

    datasets = DATASETS[args.product_type]

    data = [{'filename': x} for x in filenames]

    rdd = sc.parallelize(data) \
        .map(expect(unzip())) \
        .map(expect(hdfeos(datasets))) \
        .filter(not_bad()) \
        .map(filter_area(is_ross_area)) \
        .filter(not_empty('lon')) \
        .map(select('filename'))

    for x in rdd.collect():
        print(x)

    sc.stop()
