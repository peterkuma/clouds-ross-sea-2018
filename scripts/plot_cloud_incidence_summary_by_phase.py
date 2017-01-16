import h5py
from matplotlib import pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.lines as mlines
import argparse
from matplotlib import gridspec
import numpy as np
from scipy.ndimage.filters import gaussian_filter


heights = np.arange(0, 15000)

cloud_phases = [
    'ice',
    'mixed',
    'liquid'
]

phase_linestyle = [
    'dotted',
    'dashed',
    'solid'
]

phase_lw = [
    2.5,
    1.7,
    1.6
]

colors = [
    '#ec0028',
    '#199800',
    '#0400bc',
    '#e5d300',
    '#ba00e5'
]


def plot_main(files, labels):
    for i, f in zip(range(len(files)), files):
        total = f['cloud_incidence_total'][()]
        for j in range(len(cloud_phases)):
            cloud_incidence_p = np.sum(
                    1.0*f['cloud_incidence_by_type_phase'][:, :, j],
                    axis=1
                )/total
            line, = plt.plot(
                gaussian_filter(cloud_incidence_p*100.0, 50),
                heights/1000.0,
                linestyle=phase_linestyle[j],
                lw=phase_lw[j],
                color=colors[i]
            )

    plt.xlabel('Frequency (%)')
    plt.ylabel('Height (km)')
    plt.xlim(0, 35)
    plt.ylim(0, 15)
    plt.xticks(plt.xticks()[0][:-1])

    plt.grid()

    legend_phase = plt.legend(handles=[
        mlines.Line2D([], [], color='#000000', label=cloud_phases[i], linestyle=phase_linestyle[i], lw=phase_lw[i])
        for i in range(len(cloud_phases))
    ], fontsize='medium', bbox_to_anchor=(0.82, 1))
    legend_phase.get_frame().set_linewidth(0.8)

    if labels is not None:
        legend = plt.legend(handles=[
            mlines.Line2D([], [], color=colors[i], label=labels[i], lw=1.5)
            for i in range(len(files))
        ], fontsize='medium')
        legend.get_frame().set_linewidth(0.8)

    plt.gca().add_artist(legend_phase)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Plot cloud incidence summary by phase')
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
