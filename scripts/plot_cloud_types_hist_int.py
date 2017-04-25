import numpy as np
import h5py
from matplotlib import pyplot as plt
import matplotlib as mpl
import argparse
import json
from matplotlib import gridspec
import string


cloud_types = np.array([
    'CS',
    'N/A',
    'Ci',
    'As',
    'Ac',
    'St+Sc',
    'Cu',
    'DC',
    'Ns'
])

cloud_types_order = np.array([
    0, # CS
    1, # N/A
    8, # Ci
    7, # As
    6, # Ac
    5, # St+Sc
    4, # Cu
    3, # DC
    2, # Ns
])

# cloud_colors = np.array([
#     '#FFFFFF', # CS
#     '#EEEEEE', # N/A
#     '#450084', # Ci
#     '#0000FF', # As
#     '#00A7FF', # Ac
#     '#00E831', # St+Sc
#     #'#FEFE00', # Sc
#     '#FFAA00', # Cu
#     '#C800C8', # DC
#     '#F73C0A' # Ns
# ])

# cloud_colors = np.array([
#     '#ffffff', # CS
#     '#e4e4e4', # N/A
#     '#965fff', # Ci
#     '#5f81ff', # As
#     '#5fe4ff', # Ac
#     '#abff5f', # St+Sc
#     #'#ebeb26', # Sc
#     '#ffb05f', # Cu
#     '#ff5fe2', # DC
#     '#f74e4e' # Ns
# ])

# cloud_colors = np.array([
#     '#ffffff', # CS
#     '#e4e4e4', # N/A
#     '#6500c7', # Ci
#     '#031ed3', # As
#     '#0195fc', # Ac
#     '#00560d', # St+Sc
#     #'#ebeb26', # Sc
#     '#d64400', # Cu
#     '#960096', # DC
#     '#f74e4e' # Ns
# ])

cloud_colors = np.array([
    '#FFFFFF', # CS
    '#EEEEEE', # N/A
    '#db244d', # Ci
    '#17c7ff', # As
    '#257ee3', # Ac
    '#7ADB22', # St+Sc
    #'#FEFE00', # Sc
    '#8895a4', # Cu
    '#434343', # DC
    '#F73C0A' # Ns
])

cloud_text_color = np.array([
    '#FFFFFF', # CS
    '#FFFFFF', # N/A
    '#FFFFFF', # Ci
    '#000000', # As
    '#FFFFFF', # Ac
    '#000000', # St+Sc
    #'#000000', # Sc
    '#FFFFFF', # Cu
    '#FFFFFF', # DC
    '#000000' # Ns
])


def plot_main(files, labels, sep=None, show_yax=True):
    n = len(files)
    idx = np.arange(n)
    for f, i in zip(files, idx):
        hist = f['cloud_types_hist_int'][::]
        hist = combine_st_sc(hist)
        hist = hist[cloud_types_order][1:]
        m = hist.size
        hist = hist/np.sum(hist)*100.0
        bottom = np.hstack([[0], np.cumsum(hist)[:-1]])
        rects = plt.bar(
            left=(i * np.ones(m)),
            height=hist,
            width=1,
            bottom=bottom,
            color=cloud_colors[cloud_types_order][1:],
            lw=0.4
        )
        for j in range(m):
            if hist[j] >= 1:
                def f(x):
                    if x < 3: return 8
                    elif x < 5: return 9
                    else: return 11
                plt.annotate(
                    ('%.0f' % np.round(hist[j])),
                    (i + 0.5, bottom[j] + hist[j] * 0.5),
                    xycoords='data',
                    ha='center',
                    va='center',
                    fontsize=f(hist[j]),
                    color=cloud_text_color[cloud_types_order][1:][j]
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


def plot_colorbar(cax, skip=None):
    mask = np.ones(len(cloud_types), dtype=np.bool)
    mask[skip] = 0

    cmap = mpl.colors.ListedColormap(cloud_colors[cloud_types_order][mask])
    norm = mpl.colors.Normalize(vmin=0, vmax=cloud_types[mask].size)
    cb = mpl.colorbar.ColorbarBase(
        cax,
        cmap=cmap,
        norm=norm
    )
    cb.set_ticks(np.arange(cloud_types[mask].size) + 0.5)
    cb.set_ticklabels(cloud_types[cloud_types_order][mask])
    cb.ax.yaxis.set_tick_params(length=0)


def combine_st_sc(hist):
    new_hist = np.zeros(hist.size - 1, dtype=np.float64)
    new_hist[:5] = hist[:5]
    new_hist[5] = hist[5] + hist[6]
    new_hist[6:] = hist[7:]
    return new_hist


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Plot cloud types histogram (integrated)')
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
            show_yax=(i == 0),
            sep=panel.get('sep')
        )

        plt.annotate(panel['title'],
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
    plot_colorbar(cax, skip=np.array([0, 1, 2]))

    plt.savefig(args.outfile, bbox_inches='tight')
