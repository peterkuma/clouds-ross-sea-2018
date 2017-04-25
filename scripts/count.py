from __future__ import print_function

import sys
import os
from os import path
import argparse
import numpy as np
import h5py
from pyspark import SparkContext

sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from lib.spark.map import h5, filter_cloudsat_quality, split, cloudsat_daynight, filter_daynight, filter_coggins_regime, filter_season, filter_area
from lib.areas import is_any_area, is_ross_sea, is_ross_sea_east, is_ross_sea_west, is_ross_ice_shelf, is_ross_ice_shelf_east, is_ross_ice_shelf_west
from lib.spark.filter import not_empty


AREAS = {
    'any': is_any_area,
    'ross_sea': is_ross_sea,
    'ross_sea_east': is_ross_sea_east,
    'ross_sea_west': is_ross_sea_west,
    'ross_ice_shelf': is_ross_ice_shelf,
    'ross_ice_shelf_east': is_ross_ice_shelf_east,
    'ross_ice_shelf_west': is_ross_ice_shelf_west
}


if __name__ == '__main__':
    sc = SparkContext(appName='Count')

    parser = argparse.ArgumentParser(description='Count')
    parser.add_argument('files', metavar='FILES', type=str, help='HDF5 input files', nargs='*')
    parser.add_argument('-n', dest='daynight', type=int, help='day/night only (0 - night, 1 - day)')
    parser.add_argument('-r', dest='regime', type=str, help='Coggins regime')
    parser.add_argument('-s', dest='season', type=str, help='season')
    parser.add_argument('-a', dest='area', type=str, help='area', default='any')

    args = parser.parse_args()

    data = [{'filename': x} for x in args.files]

    dataset_names = {
        'data_quality': {
            'dataset': 'data_quality'
        },
        'lat': {
            'dataset': 'lat'
        },
        'lon': {
            'dataset': 'lon'
        },
        'time': {
            'dataset': 'time'
        }
    }

    rdd = sc.parallelize(data) \
        .map(h5(dataset_names)) \
        .filter(not_empty('lon')) \
        .map(filter_cloudsat_quality('data_quality')) \
        .map(filter_coggins_regime(args.regime)) \
        .map(filter_season(args.season)) \
        .map(filter_area(AREAS[args.area])) \
        .flatMap(split(10000))

    if args.daynight is not None:
        rdd = rdd \
            .map(cloudsat_daynight()) \
            .map(filter_daynight(args.daynight))

    count = rdd \
        .map(lambda x: x['datasets']['lon'].size) \
        .sum()

    print(count)

    sc.stop()
