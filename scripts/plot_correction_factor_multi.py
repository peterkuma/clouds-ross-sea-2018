import argparse
import numpy as np
import h5py
import json
import string
import matplotlib as mpl
from matplotlib import pyplot as plt
from matplotlib import gridspec
from mpl_toolkits.basemap import Basemap
import colormaps



def plot_panel(
    filename,
    show_colorbar=True,
    xaxis='bottom',
    norm=None,
    cmap=None,
    annotation=None
):
    with h5py.File(filename) as f:
        correction_factor = 1.0*f['cloud_incidence_2'][::]/f['cloud_incidence_1'][::]

        m = Basemap(
            llcrnrlon=-180,
            llcrnrlat=-90,
            urcrnrlon=180,
            urcrnrlat=90
        )
        im = m.imshow(correction_factor.T,
        # im = m.imshow((f['cloud_incidence_1'][::]/f['cloud_incidence_1_total'][::]).T,
            interpolation='nearest',
            norm=norm,
            cmap=cmap
        )
        # if show_colorbar:
        #     m.colorbar(im, 'right', size='3%', pad='3%')
        m.drawcoastlines(linewidth=0.1)
        m.drawcountries(linewidth=0.1)
        m.drawparallels(np.arange(-90.,91.,20.), labels=[1,0,0,1], linewidth=0.1, color='#333333', fontsize=10)

        if xaxis == 'bottom':
            labels = [0, 0, 0, 1]
        elif xaxis == 'top':
            labels = [0, 0, 1, 0]
        else:
            labels = [0, 0, 0, 0]
        m.drawmeridians(np.arange(-180.,180.,30.), labels=labels, linewidth=0.1, color='#333333', fontsize=10)

        if annotation is not None:
            plt.annotate(
                annotation,
                xy=(0, 1),
                xytext=(5, -5),
                ha='left',
                va='top',
                xycoords='axes fraction',
                textcoords='offset points',
                weight='bold'
            )


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Plot correction factor (multi)')
    parser.add_argument('-c', dest='config', help='config file')
    parser.add_argument('-o', dest='outfile', type=str, help='output plot')
    args = parser.parse_args()
    config = json.load(open(args.config))

    plt.figure(figsize=(8,12))
    plt.viridis()
    plt.rcParams['font.family'] = 'Open Sans'

    nrows = len(config['files'])

    gs = gridspec.GridSpec(
        nrows + 1,
        1,
        wspace=0,
        hspace=0.15,
        height_ratios=(0.3, 0.3, 0.3, 0.015)
    )

    norm = mpl.colors.Normalize(0.2, 2)
    cmap = colormaps.parula

    for i, filename in enumerate(config['files']):
        plt.subplot(gs[i])

        if i == 0:
            xaxis = 'top'
        elif i == nrows - 1:
            xaxis = 'bottom'
        else:
            xaxis = None

        plot_panel(
            filename,
            xaxis=xaxis,
            show_colorbar=(i == 0),
            norm=norm,
            cmap=cmap,
            annotation=string.lowercase[i]
        )

        plt.annotate(
            config['labels'][i],
            xy=(-0.15, 0.5), xytext=(0, 0),
            xycoords=('axes fraction', 'axes fraction'),
            textcoords='offset points',
            size=14,
            ha='left',
            va='center',
            weight='bold'
        )

    cax = plt.subplot(gs[nrows])
    cb = mpl.colorbar.ColorbarBase(
        cax,
        orientation='horizontal',
        extend='both',
        cmap=cmap,
        norm=norm
    )
    cb.set_label('8.3 to 8 km cloud occurrence ratio (1)')

    if args.outfile:
        plt.savefig(args.outfile, bbox_inches='tight', pad_inches=0.5)
    else:
        plt.show()
