import numpy as np
import h5py
from matplotlib import pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.lines as mlines
import argparse
from matplotlib import gridspec


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

cloud_phases = [
    'ice',
    'mixed',
    'water'
]

cloud_colors = [
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

phase_hatches = [
    '..',
    '//',
    None
]

phase_linestyle = [
    'dotted',
    'dashdot',
    'dashed'
]


def plot_main(f):
    h = len(heights)
    total = f['cloud_incidence_total'][()]

    left = np.zeros(h, dtype=np.double)
    for i in reversed(range(len(cloud_types))):
        for j in range(len(cloud_phases)):
            cloud_incidence_p = 1.0*f['cloud_incidence_by_type_phase'][:, i, j]/total
            plt.fill_betweenx(
                heights/1000.0,
                left,
                left + cloud_incidence_p*100.0,
                facecolor=cloud_colors[i],
                lw=0,
            )
            # plt.fill_betweenx(
            #     heights/1000.0,
            #     left,
            #     left + cloud_incidence_p*100.0,
            #     facecolor='none',
            #     edgecolor='#000000',
            #     alpha=0.8,
            #     lw=0,
            #     hatch=phase_hatches[j]
            # )
            left += cloud_incidence_p*100.0

    plt.xlabel('Frequency (%)')
    plt.ylabel('Height (km)')
    plt.xlim(0, 45)
    plt.ylim(0, 15)
    plt.xticks(plt.xticks()[0][:-1])

    plt.grid()

    legend_type = plt.legend(handles=[
        mpatches.Patch(color=cloud_colors[i], label=cloud_types[i], lw=0.5)
        for i in range(len(cloud_types))
    ])
    legend_type.get_frame().set_linewidth(0.8)

    # legend_phase = plt.legend(handles=[
    #     mpatches.Patch(hatch=phase_hatches[i], label=cloud_phases[i], facecolor='none', edgecolor='#000000', lw=0.5)
    #     for i in range(len(cloud_phases))
    # ], bbox_to_anchor=(0.804, 1))
    # legend_phase.get_frame().set_linewidth(0.8)

    plt.gca().add_artist(legend_type)


def plot_side(f):
    total = f['cloud_incidence_total'][()]

    for i in reversed(range(len(cloud_types))):
        cloud_incidence_p = 1.0*f['cloud_incidence_by_type'][:, i]/total
        plt.plot(
            cloud_incidence_p*100.0,
            heights/1000.0,
            color=cloud_colors[i]
        )

    # for i in reversed(range(len(cloud_types))):
    #     for j in range(len(cloud_phases)):
    #         cloud_incidence_p = 1.0*f['cloud_incidence_by_type_phase'][:, i, j]/total
    #         plt.plot(
    #             cloud_incidence_p*100.0,
    #             heights/1000.0,
    #             color=cloud_colors[i],
    #             linestyle=phase_linestyle[j]
    #         )

    plt.xlim(0, 25)
    plt.ylim(0, 15)
    plt.xlabel('Frequency (%)')
    plt.gca().yaxis.set_ticklabels([])
    plt.grid()

    # legend = plt.legend(handles=
    #     [mlines.Line2D([], [], linestyle='solid', label='total', color='#000000')] + [
    #         mlines.Line2D([], [], linestyle=phase_linestyle[i], label=cloud_phases[i], color='#000000')
    #         for i in range(len(cloud_phases))
    #     ]
    # )
    # legend.get_frame().set_linewidth(0.8)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Plot cloud incidence by type')
    parser.add_argument('file', type=str, help='HDF5 input file')
    parser.add_argument('-o', dest='outfile', type=str, help='output plot')
    parser.add_argument('-t', dest='title', type=str, help='plot title', default='')

    args = parser.parse_args()

    with h5py.File(args.file) as f:
        plt.rcParams['font.family'] = 'Open Sans'
        plt.suptitle(args.title, fontsize=14)

        gs = gridspec.GridSpec(1, 2, width_ratios=[3, 1])

        plt.subplot(gs[0])
        plot_main(f)
        plt.subplot(gs[1])
        plot_side(f)

        plt.subplots_adjust(wspace=0, left=0, right=1)
        plt.savefig(args.outfile, bbox_inches='tight')
