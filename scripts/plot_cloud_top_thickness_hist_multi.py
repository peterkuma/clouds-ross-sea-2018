import numpy as np
import h5py
from matplotlib import pyplot as plt
import argparse
import json
from matplotlib import gridspec
import colormaps


def plot_main(f, show_xlabel=True, show_ylabel=True):
    data = f['cloud_top_thickness_hist'][::]
    total = np.sum(data)
    plt.imshow(
        (100.0 * data / total),
        interpolation='nearest',
        extent=(0, 15, 0, 15),
        origin='lower',
        cmap=colormaps.parula,
        vmin=0,
        vmax=10
    )

    plt.grid()
    plt.gca().set_xlim((0, 12))
    plt.gca().set_ylim((0, 12))
    plt.xticks(np.arange(0, 13, 1))
    plt.yticks(np.arange(0, 13, 1))

    if show_ylabel:
        plt.ylabel('Height (km)')
    else:
        plt.xticks([])

    if show_xlabel:
        plt.xlabel('Thickness (km)')
    else:
        plt.yticks([])

    # cb = plt.colorbar(pad=0.03)
    # cb.set_label('Frequency (%)')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Plot cloud top-thickness histogram')
    parser.add_argument('-o', dest='outfile', type=str, help='output plot', default='')
    parser.add_argument('-c', dest='config', type=str, help='config file')
    args = parser.parse_args()

    plt.rcParams['font.family'] = 'Open Sans'

    config = json.load(open(args.config))

    w = len(config['xlabels'])
    h = len(config['ylabels'])

    # plt.figure(figsize=(config['width'], config['height']))
    gs = gridspec.GridSpec(h, w, wspace=0, hspace=0)

    for i in xrange(h):
        for j in xrange(w):
            filename = config['files'][i][j]
            with h5py.File(filename) as f:
                plt.subplot(gs[i*h + j])
                plot_main(f,
                    show_xlabel=False,
                    show_ylabel=False
                )

    plt.savefig(args.outfile, bbox_inches='tight')
