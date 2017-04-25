import numpy as np
import h5py
from matplotlib import pyplot as plt
import matplotlib as mpl
import matplotlib.patches as mpatches
import argparse
import json


cloud_types = np.array([
    'C/S',
    'N/A',
    'Ci',
    'As',
    'Ac',
    'St',
    'Sc',
    'Cu',
    'DC',
    'Ns'
])

cloud_types_order = np.array([
    0, # C/S
    1, # N/A
    9, # Ci
    8, # As
    7, # Ac
    6, # St
    5, # Sc
    4, # Cu
    3, # DC
    2, # Ns
])

cloud_colors = np.array([
    '#FFFFFF', # C/S
    '#EEEEEE', # N/A
    '#450084', # Ci
    '#0000FF', # As
    '#00A7FF', # Ac
    '#00E831', # St
    '#FEFE00', # Sc
    '#FFAA00', # Cu
    '#C800C8', # DC
    '#F73C0A' # Ns
])


def popcount(x):
    return bin(x).count('1')


def order_number(x):
    mask = np.nonzero(
            np.array(list(np.binary_repr(x)), dtype=np.int)[::-1]
        )[0] + 1
    a = cloud_types_order[mask]
    new_mask = 0
    for i in a:
        new_mask |= i
    return new_mask


def plot_main(files, labels):
    n = len(files)
    idx = np.arange(n)
    for f, i in zip(files, idx):
        hist = f['cloud_types_hist'][::]
        n = hist.size
        total = np.sum(hist)
        nlayers = np.array([popcount(x) for x in xrange(n)])
        #order = np.lexsort([-hist, nlayers])
        order_numbers = np.array([order_number(x) for x in xrange(n)])
        order = np.lexsort([order_numbers, nlayers])

        bottom = 0
        for j in order:
            p = 100.0 * hist[j] / total
            m = max(1, nlayers[j])
            if nlayers[j] > 0:
                mask = np.nonzero(
                        np.array(list(np.binary_repr(j)), dtype=np.int)[::-1]
                    )[0] + 1
            else:
                mask = np.array([0])
            order = np.argsort(cloud_types_order[mask])
            colors = cloud_colors[mask[order]]
            rect = plt.bar(
                left=(i * np.ones(m) + (1.0 / m) * np.arange(m)),
                height=(p * np.ones(m)),
                width=(1.0 / m * np.ones(m)),
                bottom=(bottom * np.ones(m)),
                color=colors,
                lw=0.4
            )
            bottom += p

    plt.ylabel('Cumulative frequency (%)')
    plt.yticks(np.arange(0, 101, 10))
    plt.xticks(idx + 0.5, labels)
    plt.ylim([0, 100])
    plt.gca().get_xaxis().set_tick_params(which=u'both', length=0)

    cmap = mpl.colors.ListedColormap(cloud_colors[cloud_types_order])
    norm = mpl.colors.Normalize(vmin=0, vmax=cloud_types.size)
    cax, kw = mpl.colorbar.make_axes(plt.gca(), pad=0.02, aspect=25)
    cb = mpl.colorbar.ColorbarBase(
        cax,
        cmap=cmap,
        norm=norm,
        **kw
    )
    cb.set_ticks(np.arange(cloud_types.size) + 0.5)
    cb.set_ticklabels(cloud_types[cloud_types_order])
    cb.ax.yaxis.set_tick_params(length=0)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Plot cloud types histogram')
    parser.add_argument('-c', dest='config', type=str, help='config file')
    parser.add_argument('-o', dest='outfile', type=str, help='output plot', default='')

    args = parser.parse_args()

    config = json.load(open(args.config))

    n = len(config['labels'])

    # plt.figure(figsize=(config['width'], config['height']))
    plt.rcParams['font.family'] = 'Open Sans'

    files = [h5py.File(filename) for filename in config['files']]

    plot_main(files, config['labels'])

    plt.savefig(args.outfile, bbox_inches='tight')
