import numpy as np
import h5py
from matplotlib import pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.lines as mlines
import json
import argparse


heights = np.arange(0, 15000)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Plot cloud incidence (multi)')
    parser.add_argument('-c', dest='config', type=str, help='config file')
    parser.add_argument('-o', dest='output', type=str, help='output plot')

    args = parser.parse_args()

    config = json.load(open(args.config))

    plt.rcParams['font.family'] = 'Open Sans'

    n = len(config['files'])

    for i, filename in enumerate(config['files']):
        with h5py.File(filename) as f:
            total = f['cloud_incidence_total'][()]
            cloud_incidence = 100.0*f['cloud_incidence'][::]/total

            plt.plot(
                cloud_incidence,
                heights/1000.0,
                color=config['colors'][i],
                lw=1.7
            )
            plt.xlabel('Frequency (%)')
            plt.ylabel('Height (km)')

    plt.xlim(0, 40)
    plt.ylim(0, 15)

    plt.grid()

    legend = plt.legend(handles=[
        mlines.Line2D([], [], label=config['labels'][i], color=config['colors'][i], lw=1.7)
        for i in range(n)
    ], fontsize='12', borderaxespad=0, bbox_to_anchor=[1, 1], labelspacing=0.8)
    legend.get_frame().set_linewidth(0.8)

    if args.output:
        plt.savefig(args.output, bbox_inches='tight')
    else:
        plt.show()
