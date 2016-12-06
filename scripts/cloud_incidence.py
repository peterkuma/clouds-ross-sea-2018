from __future__ import print_function

import sys
import os
from os import path
import argparse
import numpy as np
import h5py
from pyspark import SparkContext

sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from lib.spark.map import h5, select, filter_cloudsat_quality, split, cloudsat_daynight, filter_daynight
from lib.spark.filter import not_empty


heights = np.arange(0, 15000)


def cloud_incidence1(heights, top, base):
    w = top.size
    h = heights.size
    top_idx = np.searchsorted(heights, top)
    base_idx = np.searchsorted(heights, base)
    hist = np.zeros(h, np.int64)
    for i in range(w):
        hist[base_idx[i]:top_idx[i]] += 1
    # for i in range(h):
    #     hist[i] = np.sum((base_idx <= i) & (top_idx > i))
    return hist


def cloud_incidence_by_type_phase(heights, top, base, type, phase):
    w = top.size
    h = heights.size
    t = type.size
    p = phase.size
    top_idx = np.searchsorted(heights, top)
    base_idx = np.searchsorted(heights, base)
    hist = np.zeros((h, t, p), np.int64)
    for i in range(w):
        hist[base_idx[i]:top_idx[i], type[i], phase[i]] += 1
    return hist


def cloud_incidence():
    def f(data):
        w = data['datasets']['lon'].size
        h = heights.size

        data['datasets']['cloud_incidence'] = np.zeros(h, np.int64)

        if 'cloud_type' in data['datasets']:
            t = 9
            data['datasets']['cloud_incidence_by_type'] = np.zeros((h, t), np.int64)

        if 'cloud_phase' in data['datasets']:
            p = 3
            data['datasets']['cloud_incidence_by_phase'] = np.zeros((h, t), np.int64)

        heightsx = np.tile(heights, (w, 1))
        max_layers = data['datasets']['layer_top'].shape[1]

        for i in range(max_layers):
            top = data['datasets']['layer_top'][:, i]
            base = data['datasets']['layer_base'][:, i]
            mask = (top >= 0) & (base >= 0)
            topx = top[mask]
            basex = base[mask]

            data['datasets']['cloud_incidence'] += \
                cloud_incidence1(heights, topx, basex)

            if 'cloud_type' in data['datasets']:
                type = data['datasets']['cloud_type'][:, i]
                typex = type[mask]
                for j in range(t):
                    maskt = typex == j
                    topxt = topx[maskt]
                    basext = basex[maskt]
                    data['datasets']['cloud_incidence_by_type'][:, j] += \
                        cloud_incidence1(heights, topxt, basext)

            if 'cloud_phase' in data['datasets']:
                phase = data['datasets']['cloud_phase'][:, i]
                phasex = phase[mask]
                for j in range(p):
                    maskp = phasex == j
                    topxp = topx[maskp]
                    basexp = basex[maskp]
                    data['datasets']['cloud_incidence_by_phase'][:, j] += \
                        cloud_incidence1(heights, topxp, basexp)

            if (
                'cloud_type' in data['datasets'] and
                'cloud_phase' in data['datasets']
            ):
                type = data['datasets']['cloud_type'][:, i]
                phase = data['datasets']['cloud_phase'][:, i]
                data['datasets']['cloud_incidence_by_type_phase'] += \
                    cloud_incidence_by_type_phase(heights, topx, basex, type, phase)
        return data
    return f


if __name__ == '__main__':
    sc = SparkContext(appName='CloudIncidence')

    parser = argparse.ArgumentParser(description='Cloud incidence histogram')
    parser.add_argument('files', metavar='FILES', type=str,
                       help='HDF5 input files', nargs='*')
    parser.add_argument('-o', dest='output', type=str,
                       help='output')
    parser.add_argument('-n', dest='daynight', type=int,
                       help='day/night only (0 - night, 1 - day)')

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
            'cloud_type': {
                'dataset': 'cloud_type'
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
        })) \
        .filter(not_empty('lon')) \
        .map(filter_cloudsat_quality('data_quality')) \
        .flatMap(split(10000)) \
        .sample(False, 0.01, 1)

    if args.daynight is not None:
        rdd = rdd \
            .map(cloudsat_daynight()) \
            .map(filter_daynight(args.daynight))

    rdd = rdd\
        .map(cloud_incidence()) \

    cloud_incidence = rdd \
        .map(select('datasets/cloud_incidence')) \
        .reduce(np.add)

    cloud_incidence_by_type = rdd \
        .map(select('datasets/cloud_incidence_by_type')) \
        .reduce(np.add)

    cloud_incidence_total = rdd \
        .map(select('datasets/lon')) \
        .map(lambda x: x.size) \
        .sum()

    with h5py.File(args.output, 'w') as f:
        f.create_dataset('cloud_incidence', data=cloud_incidence)
        f.create_dataset('cloud_incidence_by_type', data=cloud_incidence_by_type)
        f.create_dataset('cloud_incidence_total', data=cloud_incidence_total)

    sc.stop()
