import numpy as np
import h5py
from matplotlib import pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.lines as mlines
import argparse
from matplotlib import gridspec
import json
import string


heights = np.arange(0, 15000)

cloud_phases = [
    'ice',
    'mixed',
    'water'
]

phase_colors = [
    '#b0d5ff',
    '#59aaff',
    '#0075f3'
]

region_labels = [
    'L',
    'M',
    'H'
]

region_heights = [
    0,
    2,
    6,
    15
]


def plot_main(
    f,
    fx=None,
    xlab=True,
    ylab=True,
    legend=True,
    annotation=None,
    show_height_labels=False
):
    h = len(heights)
    total = f['cloud_incidence_total'][()]
    clear = f['cloud_incidence_clear'][()]

    left = np.zeros(h, dtype=np.double)
    for i in reversed(range(len(cloud_phases))):
        cloud_incidence_p = np.sum(
                1.0*f['cloud_incidence_by_type_phase'][:, :, i],
                axis=1
            )/total
        plt.fill_betweenx(
            heights/1000.0,
            left,
            left + cloud_incidence_p*100.0,
            facecolor=phase_colors[i],
            lw=0,
            edgecolor='#002254'
        )
        left += cloud_incidence_p*100.0

    if xlab:
        plt.xlabel('Frequency (%)')
    else:
        plt.gca().set_xticklabels([])

    if ylab:
        plt.ylabel('Height (km)')
    else:
        plt.gca().set_yticklabels([])

    plt.xlim(0, 45)
    plt.ylim(0, 15)

    plt.xticks(plt.xticks()[0][:-1])

    plt.grid()

    for x in region_heights:
        plt.axhline(x,
            color='black',
            lw=0.5
        )

    if show_height_labels:
        for label, i in zip(region_labels, range(len(region_labels))):
            x = 0.5*(region_heights[i] + region_heights[i + 1])
            plt.annotate(
                label,
                xy=(1, x/15.0),
                xytext=(5, 0),
                va='center',
                ha='left',
                xycoords='axes fraction',
                textcoords='offset points',
                weight='bold'
            )

    if legend:
        legend = plt.legend(handles=[
            mpatches.Patch(label=cloud_phases[i], facecolor=phase_colors[i], edgecolor='#002254', lw=0.5)
            for i in range(len(cloud_phases))
        ], fontsize='11', borderaxespad=0, bbox_to_anchor=[1, 0.75])
        legend.get_frame().set_linewidth(0.8)

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

    cloud_fraction = 1.0 - 1.0 * clear / total
    plt.annotate(
        '%d %%' % np.round(cloud_fraction * 100.0),
        xy=(0.5, 1),
        xytext=(0, -5),
        ha='center',
        va='top',
        xycoords='axes fraction',
        textcoords='offset points',
        backgroundcolor='#eeeeee',
        weight='bold'
    )

    if fx is not None:
        east = 1.0 - 1.0*fx[0]['cloud_incidence_clear'][()]/ \
            fx[0]['cloud_incidence_total'][()]
        west = 1.0 - 1.0*fx[1]['cloud_incidence_clear'][()]/ \
            fx[1]['cloud_incidence_total'][()]

        plt.annotate(
            'W: %d %% E: %d %%' % (np.round(west*100.0), np.round(east*100.0)),
            xy=(0.5, 0.9),
            xytext=(0, -5),
            ha='center',
            va='top',
            xycoords='axes fraction',
            textcoords='offset points',
            backgroundcolor='#eeeeee',
            weight='bold'
        )


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Plot cloud incidence by phase (multiple)')
    parser.add_argument('-c', dest='config', type=str, help='config file')
    parser.add_argument('-o', dest='outfile', type=str, help='output plot', default='')

    args = parser.parse_args()

    config = json.load(open(args.config))

    xn = len(config['xtitles'])
    yn = len(config['ytitles'])

    plt.figure(figsize=(config['width'], config['height']))
    plt.rcParams['font.family'] = 'Open Sans'
    plt.rcParams['axes.linewidth'] = 0.7
    gs = gridspec.GridSpec(yn, xn)

    for i in range(yn):
        for j in range(xn):
            filename = config['files'][i][j]
            filenamesx = config['filesx'][i][j]
            fx = [h5py.File(filenamex) for filenamex in filenamesx]
            with h5py.File(filename) as f:
                plt.subplot(gs[i*xn + j])
                plot_main(
                    f,
                    fx=fx,
                    ylab=(j == 0),
                    xlab=(i == (yn - 1)),
                    legend=(i == 0 and j == (xn - 1)),
                    annotation=string.lowercase[i * xn + j],
                    show_height_labels=(j == xn - 1)
                )

                if i == yn - 1:
                    plt.annotate(config['xtitles'][j],
                        xy=(0.5, 0), xytext=(0, 5),
                        xycoords=('axes fraction', 'figure fraction'),
                        textcoords='offset points',
                        size=14,
                        ha='center',
                        va='bottom',
                        weight='bold'
                    )

                if j == 0:
                    plt.annotate(config['ytitles'][i],
                        xy=(-0.35, 0.5), xytext=(0, 0),
                        xycoords=('axes fraction', 'axes fraction'),
                        textcoords='offset points',
                        size=14,
                        ha='left',
                        va='center',
                        weight='bold'
                    )


    plt.subplots_adjust(wspace=0.05, hspace=0.05)
    plt.savefig(args.outfile, bbox_inches='tight')
