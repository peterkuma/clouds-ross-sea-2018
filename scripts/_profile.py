from __future__ import print_function

import sys
import os
from os import path
import argparse
import numpy as np
from matplotlib import pyplot as plt


sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))


heights = np.linspace(0, 15000, 100)


def profile():
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
            topx = np.tile(top, (h, 1)).T
            basex = np.tile(base, (h, 1)).T
            data['datasets']['profile'] = data['datasets']['profile'] | ((heightsx <= topx) & (heightsx >= basex))
        return data
    return f


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Profile')
    parser.add_argument('filename', metavar='FILES', type=str,
                       help='HDF5 file')

    args = parser.parse_args()

    data = {'filename': filename}

    data = h5({
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
    })(data)

    data = filter(not_empty('lon'))(data)
        .map(filter_cloudsat_quality('data_quality')) \
        .map(lon_rel(160, 1)) \
        .map(profile()) \
        .map(select('datasets/profile'))

    profiles = rdd.takeSample(False, 1)

    # profile = rdd.reduce(lambda a, b: np.concatenate([a, b], axis=0)).T

    # profiles = rdd.collect()

    # profile = profiles[0]

    # rows = np.array_split(profile, 25, axis=1)
    #img = np.concatenate(rows[0:10], axis=0)

    # img = np.concatenate(profiles, axis=1)

    print(profiles[0])

    plt.imshow(
        profiles[0].T,
        interpolation='nearest',
        origin='lower',
        cmap=plt.cm.Greys
    )
    plt.show()

    # for x in rdd.collect():
    #     print(x)

