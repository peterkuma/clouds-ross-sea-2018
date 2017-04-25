import sys
import numpy as np
import h5py
from matplotlib import pyplot as plt
import argparse
import colormaps
import logging
from matplotlib.colors import LogNorm


def plot_main(f, f0=None):
    hist = f['cloud_top_thickness_hist'][::]

    hist0 = f0['cloud_top_thickness_hist'][::] if f0 else None

    total = np.sum(hist)
    total0 = np.sum(hist0)

    if f0:
        # data = np.log(1.0*hist/(total - hist)) - np.log(1.0*hist0/(total0 - hist0))
        data = 100*(1.0*hist/total - 1.0*hist0/total0)
        vmin = -1
        vmax = 1
        cmap = plt.get_cmap('bwr')
        extend = 'both'
    else:
        # data = np.log(1.0*hist/(total - hist))
        # data = np.log(1.0*hist/total)
        # print data
        # vmin = np.min(data)
        # vmax = np.max(data)
        data = 100.0*hist/(total - hist)
        # vmin = 0
        # vmax = 3
        cmap = plt.get_cmap('Blues')
        extend = 'neither'

    plt.imshow(
        data,
        interpolation='nearest',
        extent=(0, 15, 0, 15),
        origin='lower',
        # cmap=colormaps.viridis,
        cmap=cmap,
        # vmin=vmin,
        # vmax=vmax
    )

    plt.grid()
    plt.gca().set_xlim((0, 10))
    plt.gca().set_ylim((0, 10))
    plt.xticks(np.arange(0, 11, 1))
    plt.yticks(np.arange(0, 11, 1))
    plt.ylabel('Height (km)')
    plt.xlabel('Thickness (km)')

    cb = plt.colorbar(pad=0.03, extend=extend)

    if f0:
        cb.set_label('Log odds ratio (1)')
    else:
        cb.set_label('Log odds (1)')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Plot cloud top-thickness histogram')
    parser.add_argument('-o', dest='outfile', type=str, help='output plot', default='')
    parser.add_argument('-t', dest='title', type=str, help='plot title')
    parser.add_argument('files', type=str, help='HDF5 input files', nargs='+')
    args = parser.parse_args()

    plt.rcParams['font.family'] = 'Open Sans'

    if len(args.files) == 1:
        with h5py.File(args.files[0]) as f:
            plot_main(f)
    elif len(args.files) == 2:
        with h5py.File(args.files[0]) as f:
            with h5py.File(args.files[1]) as f0:
                plot_main(f, f0)
    else:
        logging.error('Too many input files')
        sys.exit(1)

    if args.title:
        plt.suptitle(args.title)

    plt.savefig(args.outfile, bbox_inches='tight')
