from __future__ import print_function

import sys
from os import path
import argparse
import h5py
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.cm
from colormap.colormaps import viridis

sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

plt.register_cmap(name='viridis', cmap=viridis)


heights = np.linspace(0, 20000, 101)


def histogram(points):
    hist = np.histogram2d(points[:, 1], points[:, 0],
        bins=heights
    )[0]
    return hist


def plot_histogram(hist):
    plt.imshow(hist,
        interpolation='nearest',
        origin='lower',
        cmap=plt.get_cmap('viridis'),
        norm=matplotlib.colors.Normalize(np.min(hist), np.max(hist)*0.05)
    )
    plt.show()


def hist_entropy(hist):
    mask = hist > 0
    return np.sum(hist[mask] * np.log(hist[mask]))


def correct_hist(hist, a):
    lower = hist[:42, :]
    upper = hist[42:, :]
    print(np.sum(lower > 0))
    print(np.sum(upper > 0))
    l1 = np.sum(lower)
    u1 = np.sum(upper)
    print(l1, u1)
    o1 = u1/l1
    o2 = o1*np.exp(a)
    u2 = o2/(1 + o2)
    l2 = 1 - u2
    new_hist = np.copy(hist)
    print(l2, u2)
    new_hist[:42, :] *= l2/l1
    new_hist[42:, :] *= u2/u1
    return new_hist


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Cloud top/base correction')
    parser.add_argument('file', metavar='FILE', type=str,
                       help='HDF5 input file')

    args = parser.parse_args()

    with h5py.File(args.file) as f:
        hist = histogram(f['points'])
        hist = hist/np.sum(hist)
        #hist[:10,:] = 1
        new_hist = correct_hist(hist, 0.8)

        print(-2, hist_entropy(correct_hist(hist, -2)))
        print(-1.5, hist_entropy(correct_hist(hist, -1.5)))
        print(-1, hist_entropy(correct_hist(hist, -1)))
        print(-0.5, hist_entropy(correct_hist(hist, -0.5)))
        print(0, hist_entropy(correct_hist(hist, 0)))
        print(0.5, hist_entropy(correct_hist(hist, 0.5)))
        print(1, hist_entropy(correct_hist(hist, 1)))
        print(1.5, hist_entropy(correct_hist(hist, 1.5)))
        print(2, hist_entropy(correct_hist(hist, 2)))

        plot_histogram(new_hist)
        #print(hist_entropy(hist_norm))
