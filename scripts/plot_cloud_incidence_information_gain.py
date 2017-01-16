import h5py
from matplotlib import pyplot as plt
import argparse
import numpy as np
import json
from scipy.ndimage.filters import gaussian_filter


heights = np.arange(0, 15000)

colors = [
    '#0400bc',
    '#199800'
]


def information(files, type):
    inf = np.zeros(heights.size, np.double)
    c = 0.0
    for f in files:
        total = np.sum(f['cloud_incidence_total'][()])
        if type == 'phase':
            p = 1.0*np.sum(
                f['cloud_incidence_by_type_phase'][::],
                axis=1
            )/total
        elif type == 'type':
            p = 1.0*np.sum(
                f['cloud_incidence_by_type_phase'][::],
                axis=2
            )/total
        else:
            raise ValueError('Invalid type "%s"' % type)

        p[np.isnan(p)] = 0

        p_clear = 1 - np.sum(p, axis=1)

        inf0 = np.sum(np.vstack([
            np.where(p[:, i] > 0, p[:, i]*np.log2(p[:, i]), 0)
            for i in range(p.shape[1])
        ] + [p_clear*np.log2(p_clear)]), axis=0)

        inf += inf0*total
        c += total

    return inf/c


def plot_main(information, labels):
    lines = []
    for inf in information[1:]:
        line, = plt.plot(
            gaussian_filter(inf - information[0], 100),
            heights/1000.0,
            color=colors[len(lines)],
            lw=1.3
        )
        lines.append(line)

    plt.legend(lines, labels[1:], fontsize='medium')
    plt.xlabel('Information gain (1)')
    plt.ylabel('Height (km)')
    plt.xlim(0, 0.03)
    plt.ylim(0, 15)
    plt.grid()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Plot cloud incidence information gain')
    parser.add_argument('files', type=str, help='HDF5 input files', nargs='*')
    parser.add_argument('-o', dest='outfile', type=str, help='output plot')
    parser.add_argument('-t', dest='title', type=str, help='plot title', default='')
    parser.add_argument('-x', dest='type', type=str, help='plot type', default='phase', choices=('type', 'phase'))
    parser.add_argument('-c', dest='config', type=str, help='JSON config', required=True)

    args = parser.parse_args()

    plt.rcParams['font.family'] = 'Open Sans'
    plt.figure(figsize=(6, 6))

    inf = []
    with open(args.config) as f:
        config = json.load(f)
        for cls in config['classes']:
            files = [h5py.File(f) for f in cls]
            inf.append(information(files, args.type))

        plot_main(inf, config['labels'])
        plt.suptitle(args.title, fontsize=14)

    if args.outfile:
        plt.savefig(args.outfile, bbox_inches='tight')
    else:
        plt.show()
