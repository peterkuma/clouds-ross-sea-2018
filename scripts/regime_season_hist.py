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
from lib.coggins_regimes import coggins_regimes
from lib.time_season import time_season


regimes = np.array([
    'WNC',
    'SNC',
    'RAS',
    'WSC',
    'WS'
])

seasons = np.array([
    'DJF',
    'MAM',
    'JJA',
    'SON'
])


def regime_season_hist(regimes, seasons):
    def f(data):
        time = data['datasets']['time']
        w = time.size
        regime = coggins_regimes(time)
        season = time_season(time)

        regime_lookup = {k: v for k, v in zip(
            [x.lower() for x in regimes],
            range(regimes.size)
        )}

        season_lookup = {k: v for k, v in zip(
            [x.lower() for x in seasons],
            range(seasons.size)
        )}

        hist = np.zeros((regimes.size, seasons.size))

        for i in xrange(w):
            hist[
                regime_lookup[regime[i]],
                season_lookup[season[i]]
            ] += 1

        data['regime_season_hist'] = hist
        return data
    return f


if __name__ == '__main__':
    sc = SparkContext(appName='RegimeSeasonHist')

    parser = argparse.ArgumentParser(description='Regime-season histogram')
    parser.add_argument('files', metavar='FILES', type=str, help='HDF5 input files', nargs='*')
    parser.add_argument('-o', dest='output', type=str, help='output')

    args = parser.parse_args()

    data = [{'filename': x} for x in args.files]

    dataset_names = {
        'data_quality': {
            'dataset': 'data_quality'
        },
        'time': {
            'dataset': 'time'
        },
        'lon': {
            'dataset': 'lon'
        }
    }

    regime_season_hist = sc.parallelize(data) \
        .map(h5(dataset_names)) \
        .filter(not_empty('time')) \
        .map(filter_cloudsat_quality('data_quality')) \
        .flatMap(split(10000)) \
        .map(regime_season_hist(regimes, seasons)) \
        .map(select('regime_season_hist')) \
        .sum()

    with h5py.File(args.output, 'w') as f:
        f.create_dataset('regime_season_hist', data=regime_season_hist)
        f.create_dataset('regimes', data=regimes)
        f.create_dataset('seasons', data=seasons)

    sc.stop()
