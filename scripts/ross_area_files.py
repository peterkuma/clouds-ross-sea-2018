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


if __name__ == '__main__':
    sc = SparkContext(appName='CloudTopDist')

    parser = argparse.ArgumentParser(description='Ross area files')
    parser.add_argument('files', metavar='FILES', type=str,
                       help='files glob')

    args = parser.parse_args()

    filenames = glob.glob(args.files)

    data = [{'filename': x} for x in filenames]

    rdd = sc.parallelize(data) \
        .map(expect(unzip())) \
        .map(expect(hdfeos({
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
        .map(filter_area(is_ross_area)) \
        .filter(not_empty('lon')) \
        .map(select('filename'))

    for x in rdd.collect():
        print(x)

    sc.stop()
