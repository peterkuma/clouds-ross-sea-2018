import numpy as np
import h5py
from matplotlib import pyplot as plt
import argparse


heights = np.arange(0, 15000)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Plot cloud incidence')
    parser.add_argument('file', type=str, help='HDF5 input file')
    parser.add_argument('-o', dest='outfile', type=str, help='output plot')
    parser.add_argument('-t', dest='title', type=str, help='plot title', default='')

    args = parser.parse_args()

    with h5py.File(args.file) as f:
        total = f['cloud_incidence_total'][()]
        cloud_incidence_p = 1.0*f['cloud_incidence'][::]/total
        plt.rcParams['font.family'] = 'Open Sans'
        plt.barh(
            heights/1000.0,
            cloud_incidence_p,
            height=0.001,
            edgecolor='none',
            color='#3356e8'
        )
        plt.title(args.title)
        plt.xlabel('Probability (1)')
        plt.ylabel('Height (km)')
        plt.xlim(0, 0.4)
        plt.ylim(0, 15)
        plt.savefig(args.outfile)
