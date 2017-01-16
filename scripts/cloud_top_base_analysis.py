from __future__ import print_function
import sys
from os import path
import argparse
import h5py
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.cm

sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))


heights = np.linspace(0, 20000, 101)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Cloud top/base analysis')
    parser.add_argument('file', metavar='FILE', type=str,
                       help='HDF5 input file')

    args = parser.parse_args()

    with h5py.File(args.file) as f:
        hist = np.histogram(points[points[:, 0] < 8200, 1], bins=heights)[0]
        hist_norm = hist/np.fmin(hist[1][1:], 8200)
        plt.yscale('log')
        plt.bar(heights[:-1], hist_norm, width=200)
        plt.show()

        plt.bar(heights[:-1], hist_norm, width=200)
        plt.show()

        plt.bar(heights[:-1], hist, width=200)
        plt.show()
