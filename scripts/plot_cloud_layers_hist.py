import numpy as np
import h5py
from matplotlib import pyplot as plt
import matplotlib as mpl
import argparse
import json
from matplotlib import gridspec
import string


colors = [
    '#ffffff',
    '#c5e1ff',
    '#8dc4ff',
    '#55a7ff',
    '#1d8aff',
    '#006ce2',
    '#0052aa',
    '#003772',
    '#001b38',
    '#000000'
]

max_layers = 2


def plot_main(files, labels, max_layers, sep=None, show_yax=True):
    n = len(files)
    idx = np.arange(n)
    for f, i in zip(files, idx):
        hist = f['cloud_layers_hist'][::]
        hist1 = hist[:(max_layers + 1)]
        hist1[max_layers] = np.sum(hist[max_layers:])
        m = hist1.size
        p = 100.0*hist1/np.sum(hist1)
        bottom = np.hstack([[0], np.cumsum(p)[:-1]])
        rects = plt.bar(
            left=(i * np.ones(m)),
            height=p,
            width=1,
            bottom=bottom,
            color=colors,
            tick_label='abc',
            lw=0.4
        )
        for j in range(m):
            if p[j] >= 1:
                def f(x):
                    if x < 3: return 8
                    elif x < 5: return 9
                    else: return 11
                plt.annotate(
                    ('%.0f' % np.round(p[j])),
                    (i + 0.5, bottom[j] + p[j] * 0.5),
                    xycoords='data',
                    ha='center',
                    va='center',
                    fontsize=f(p[j]),
                )

    if sep:
        for s in sep:
            plt.axvline(s, color='black')

    plt.yticks(np.arange(0, 101, 10))

    if show_yax:
        plt.ylabel('Cumulative frequency (%)')
    else:
        plt.gca().yaxis.set_ticklabels([])

    plt.xticks(idx + 0.5, labels)
    plt.ylim([0, 100])
    plt.gca().get_xaxis().set_tick_params(which=u'both', length=0)


def plot_colorbar(ax, n):
    cmap = mpl.colors.ListedColormap(colors[:(n + 1)])
    norm = mpl.colors.Normalize(vmin=0, vmax=(n + 1))
    cb = mpl.colorbar.ColorbarBase(
        ax,
        cmap=cmap,
        norm=norm,
        extend='max'
    )
    cb.set_ticks(np.arange(n + 1) + 0.5)
    cb.set_ticklabels(list(np.arange(n)) + ['%d+' % n])
    cb.set_label('Number of layers')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Plot cloud layers histogram')
    parser.add_argument('-c', dest='config', type=str, help='config file')
    parser.add_argument('-o', dest='outfile', type=str, help='output plot', default='')

    args = parser.parse_args()

    config = json.load(open(args.config))

    plt.rcParams['font.family'] = 'Open Sans'

    n = len(config['panels'])

    plt.figure(figsize=(config['width'], config['height']))

    width_ratios = np.ones(n + 1)
    width_ratios[:n] *= 1.0/n
    width_ratios[n] *= 0.05/n

    gs = gridspec.GridSpec(1, n + 1,
        wspace=0.05,
        hspace=0,
        width_ratios=width_ratios
    )

    for panel, i in zip(config['panels'], range(n)):
        files = [h5py.File(filename) for filename in panel['files']]
        plt.subplot(gs[i])
        plot_main(
            files,
            panel['labels'],
            max_layers,
            show_yax=(i == 0),
            sep=panel.get('sep')
        )

        plt.annotate(
            panel['title'],
            xy=(0.5, 0), xytext=(0, 5),
            xycoords=('axes fraction', 'figure fraction'),
            textcoords='offset points',
            size=14,
            ha='center',
            va='bottom',
            weight='bold'
        )

        plt.annotate(
            string.lowercase[i],
            xy=(0, 0.92), xytext=(0, 5),
            xycoords=('axes fraction', 'figure fraction'),
            textcoords='offset points',
            size=14,
            ha='left',
            va='bottom',
            weight='bold'
        )

    cax = plt.subplot(gs[n])
    plot_colorbar(cax, max_layers)

    plt.savefig(args.outfile, bbox_inches='tight')
