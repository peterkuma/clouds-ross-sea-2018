import sys
from os import path
import numpy as np
import datetime as dt
from matplotlib import pyplot as plt
import argparse

sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from lib.coggins_regimes import coggins_regimes


MONTHS = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')
COLORS = ('#204a87', '#cc0000', '#4e9a06', '#edd400', '#5c3566')
REGIMES = ('wnc', 'snc', 'ras', 'wsc', 'ws')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Plot regimes')
    parser.add_argument('-o', dest='outfile', type=str, help='output plot')
    parser.add_argument('-t', dest='title', type=str, help='plot title', default='')
    args = parser.parse_args()

    d0 = dt.datetime(2007, 1, 1)
    d1 = dt.datetime(2010, 12, 31, 23, 59)
    seconds = (d1 - d0).total_seconds()
    time = np.arange(0, seconds, 60*60)
    regimes = coggins_regimes(time, origin=d0)
    months = np.array([(d0 + dt.timedelta(0, t)).month for t in time])

    lines = []
    labels = []

    plt.rcParams['font.family'] = 'Open Sans'

    for regime in REGIMES:
        mask = regimes == regime
        x = np.arange(1, 13)
        y = 1.0*np.bincount(months[mask])[1:]/len(time)*12
        line, = plt.plot(
            x,
            y,
            color=COLORS[len(lines)],
            lw=1.5,
            marker='s',
            markeredgecolor='none',
            markersize=1
        )
        lines.append(line)
        labels.append(regime.upper())
        plt.grid(axis='y')
        plt.xticks(x, MONTHS)
        plt.ylim(0, 0.7)
        plt.ylabel('Occurence (%)')

    for x in (2.5, 5.5, 8.5, 11.5):
        plt.axvline(x=x, color='#000000', lw=0.5, linestyle='dotted')

    plt.legend(lines, labels,
        loc='upper left',
        ncol=5,
        mode='expand'
    )

    plt.title(args.title)

    if args.outfile is not None:
        plt.savefig(args.outfile, bbox_inches='tight')
    else:
        plt.show()
