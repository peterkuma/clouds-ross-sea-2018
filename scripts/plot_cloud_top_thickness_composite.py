import json
from matplotlib import gridspec
import numpy as np
import h5py
from matplotlib import pyplot as plt
import argparse
import matplotlib as mpl
import string


blues = plt.get_cmap('Blues')
reds = plt.get_cmap('Reds')
# cmap_absolute = plt.get_cmap('Blues')

# greens = mpl.colors.LinearSegmentedColormap.from_list('greens', [
#     'white',
#     '#08306B'
# ])
cmap_absolute = mpl.colors.ListedColormap(
    plt.get_cmap('Blues')(np.linspace(0, 1, 10))
)
norm_absolute = mpl.colors.LogNorm(1e-4, 10)
#cmap_relative = plt.get_cmap('seismic')
norm_relative = mpl.colors.Normalize(-0.20, 0.20)


# blues = mpl.colors.LinearSegmentedColormap.from_list('blues', [
#     '#08306B',
#     'white'
# ])
# reds = mpl.colors.LinearSegmentedColormap.from_list('reds', [
#     'white',
#     '#67000C'
# ])
blues = plt.get_cmap('Blues_r')
cmap_relative = mpl.colors.ListedColormap(
    list(blues(np.linspace(0, 1, 9)))[0:-1] +
    ['white'] +
    list(reds(np.linspace(0, 1, 9)))[1:]
)


def plot_main(
    f,
    f0=None,
    show_ylabels=True,
    show_xlabels=True,
    cmap=None,
    norm=None,
    annotation=None
):
    hist = f['cloud_top_thickness_hist'][::]

    hist0 = f0['cloud_top_thickness_hist'][::] if f0 else None

    total = np.sum(hist)
    total0 = np.sum(hist0)

    if f0:
        data = 100*(1.0*hist/total - 1.0*hist0/total0)
        # data = np.log(1.0*hist/(total - hist)) - np.log(1.0*hist0/(total0 - hist0))
        # data = np.log(1.0*hist/total)
        extend = 'both'
    else:
        data = 100.0*hist/total
        # data = np.log(1.0*hist/(total - hist))
        # data = np.log(1.0*hist/total)
        # data = 100.0*hist/(total - hist)
        extend = 'neither'

    plt.imshow(
        data,
        interpolation='nearest',
        extent=(0, 15, 0, 15),
        origin='lower',
        cmap=cmap,
        norm=norm
    )

    plt.grid()
    plt.gca().set_xlim((0, 12))
    plt.gca().set_ylim((0, 12))
    plt.xticks(np.arange(0, 12, 2))
    plt.yticks(np.arange(0, 12, 2))

    if show_ylabels:
        plt.ylabel('CTH (km)')
    else:
        plt.gca().yaxis.set_ticklabels([])

    if show_xlabels:
        plt.xlabel('Thickness (km)')
    else:
        plt.gca().xaxis.set_ticklabels([])

    if annotation is not None:
        plt.annotate(
            annotation,
            xy=(1, 0),
            xytext=(-5, 5),
            ha='right',
            va='bottom',
            xycoords='axes fraction',
            textcoords='offset points',
            weight='bold'
        )


def plot_colorbar(cax, cmap, norm, label=None):
    cb = mpl.colorbar.ColorbarBase(
        cax,
        cmap=cmap,
        norm=norm,
        extend='both'
    )
    cb.set_label(label)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Plot cloud top/thickness composite')
    parser.add_argument('-o', dest='outfile', type=str, help='output plot', default='')
    parser.add_argument('-c', dest='config', type=str, help='config file')
    args = parser.parse_args()

    plt.rcParams['font.family'] = 'Open Sans'
    plt.rcParams['axes.linewidth'] = 0.5

    config = json.load(open(args.config))

    nrows = len(config['ytitles'])
    ncols = len(config['xtitles'])

    plt.figure(figsize=(config['width'], config['height']))

    width_ratios = np.ones(ncols + 2)
    width_ratios[ncols] = 0.003
    width_ratios[ncols + 1] = 0.015
    width_ratios[:ncols] = 1.0/ncols*(1 - np.sum(width_ratios[ncols:]))
    gs = gridspec.GridSpec(nrows, ncols + 2,
        wspace=0.03,
        hspace=0.03,
        width_ratios=width_ratios
    )

    for i in xrange(nrows):
        for j in xrange(ncols):
            ax = plt.subplot(gs[i, j])
            ax.set_aspect('auto')
            if j == 0:
                plot_main(
                    h5py.File(config['files'][i][j]),
                    show_xlabels=(i == nrows - 1),
                    cmap=cmap_absolute,
                    norm=norm_absolute,
                    annotation=string.lowercase[i*ncols + j]
                )
            else:
                plot_main(
                    h5py.File(config['files'][i][j]),
                    h5py.File(config['files'][i][0]),
                    show_ylabels=False,
                    show_xlabels=(i == nrows - 1),
                    cmap=cmap_relative,
                    norm=norm_relative,
                    annotation=string.lowercase[i*ncols + j]
                )

            if i == nrows - 1:
                plt.annotate(config['xtitles'][j],
                    xy=(0.5, 0.93), xytext=(0, 0),
                    xycoords=('axes fraction', 'figure fraction'),
                    textcoords='offset points',
                    size=14,
                    ha='center',
                    va='bottom',
                    weight='bold'
                )

            if j == 0:
                plt.annotate(config['ytitles'][i],
                    xy=(-0.4, 0.5), xytext=(0, 0),
                    xycoords=('axes fraction', 'axes fraction'),
                    textcoords='offset points',
                    size=14,
                    ha='left',
                    va='center',
                    weight='bold'
                )

    cax1 = plt.subplot(gs[0, ncols + 1])
    plot_colorbar(
        cax1,
        cmap=cmap_absolute,
        norm=norm_absolute,
        label='Frequency (%)'
    )

    cax2 = plt.subplot(gs[1, ncols + 1])
    plot_colorbar(
        cax2,
        cmap=cmap_relative,
        norm=norm_relative,
        label='Frequency difference (pp)'
    )

    plt.savefig(args.outfile, bbox_inches='tight')
