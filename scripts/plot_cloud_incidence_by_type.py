import numpy as np
import h5py
from matplotlib import pyplot as plt
import matplotlib.patches as mpatches
import argparse


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

cloud_colors = [
    '#EEEEEE',
    '#5400A3',
    '#0000FF',
    '#00A7FF',
    '#00E831',
    '#FEFE00',
    '#FFAA00',
    '#C800C8',
    '#F73C0A'
]


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Plot cloud incidence by type')
    parser.add_argument('file', type=str, help='HDF5 input file')
    parser.add_argument('-o', dest='outfile', type=str, help='output plot')
    parser.add_argument('-t', dest='title', type=str, help='plot title', default='')

    args = parser.parse_args()

    with h5py.File(args.file) as f:
        total = f['cloud_incidence_total'][()]
        plt.rcParams['font.family'] = 'Open Sans'

        h = len(heights)
        left = np.zeros(h, dtype=np.double)

        for i in reversed(range(len(cloud_types))):
        # for i in reversed(range(1)):
            cloud_incidence_p = 1.0*f['cloud_incidence_by_type'][:, i]/total
            plt.barh(
                heights/1000.0,
                cloud_incidence_p,
                height=0.001,
                left=left,
                edgecolor='none',
                color=cloud_colors[i]
            )
            left += cloud_incidence_p

        plt.title(args.title)
        plt.xlabel('Probability (1)')
        plt.ylabel('Height (km)')
        plt.xlim(0, 0.4)
        plt.ylim(0, 15)

        plt.legend(handles=[
            mpatches.Patch(color=cloud_colors[i], label=cloud_types[i])
            for i in range(len(cloud_types))
        ])

        plt.savefig(args.outfile)
