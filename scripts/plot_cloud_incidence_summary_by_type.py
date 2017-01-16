import h5py
from matplotlib import pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.lines as mlines
import argparse
from matplotlib import gridspec
import numpy as np
from scipy.ndimage.filters import gaussian_filter


heights = np.arange(0, 15000)

cloud_types = [
    'N/A',
    'Ci',
    'As',
    'Ac',
    'St',
    'Sc',
    'Cu',
    'DC',
    'Ns'
]

colors = [
    '#EEEEEE',
    '#450084',
    '#0000FF',
    '#00A7FF',
    '#00E831',
    '#FEFE00',
    '#FFAA00',
    '#C800C8',
    '#F73C0A'
]

markers = [
    's',
    'o',
    '*',
    'D',
    '^'
]


def plot_main(files, labels):
    for i, f in zip(range(len(files)), files):
        total = f['cloud_incidence_total'][()]
        for j in range(len(cloud_types)):
            cloud_incidence_p = np.sum(
                    1.0*f['cloud_incidence_by_type_phase'][:, j, :],
                    axis=1
                )/total
            line, = plt.plot(
                gaussian_filter(cloud_incidence_p*100.0, 50),
                (heights/1000.0),
                lw=1,
                color=colors[j],
            )
            plt.scatter(
                gaussian_filter(cloud_incidence_p*100.0, 50)[::1000],
                (heights/1000.0)[::1000],
                lw=1,
                color=colors[j],
                marker=markers[i],
                s=25,
                edgecolor='none',
                zorder=10
            )

    plt.xlabel('Frequency (%)')
    plt.ylabel('Height (km)')
    plt.xlim(0, 25)
    plt.ylim(0, 15)
    plt.xticks(plt.xticks()[0][:-1])

    plt.grid()

    legend_type = plt.legend(handles=[
        mlines.Line2D([], [], color=colors[i], label=cloud_types[i], lw=2)
        for i in range(len(cloud_types))
    ], fontsize='medium')
    legend_type.get_frame().set_linewidth(0.8)

    if labels is not None:
        legend = plt.legend(handles=[
            mlines.Line2D([], [], color='#000000', marker=markers[i], label=labels[i], lw=1, markersize=4)
            for i in range(len(files))
        ], fontsize='medium', bbox_to_anchor=(0.83, 1))
        legend.get_frame().set_linewidth(0.8)

    plt.gca().add_artist(legend_type)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Plot cloud incidence summary by type')
    parser.add_argument('files', type=str, help='HDF5 input files', nargs='*')
    parser.add_argument('-o', dest='outfile', type=str, help='output plot')
    parser.add_argument('-t', dest='title', type=str, help='plot title', default='')
    parser.add_argument('-l', dest='labels', type=str, help='labels', default='')

    args = parser.parse_args()

    labels = args.labels.split(',')

    files = [h5py.File(filename) for filename in args.files]
    plt.rcParams['font.family'] = 'Open Sans'
    plt.suptitle(args.title, fontsize=14)
    plot_main(files, labels)
    plt.savefig(args.outfile, bbox_inches='tight')
