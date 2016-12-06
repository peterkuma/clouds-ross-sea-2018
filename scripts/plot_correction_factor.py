import argparse
import numpy as np
from matplotlib import pyplot as plt
import h5py
from mpl_toolkits.basemap import Basemap
import colormaps


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Plot correction factor')
    parser.add_argument('file', type=str, help='input HDF5 file')
    parser.add_argument('-o', dest='outfile', type=str, help='output plot')
    parser.add_argument('-t', dest='title', type=str, help='plot title', default='')
    args = parser.parse_args()

    with h5py.File(args.file) as f:
        correction_factor = 1.0*f['cloud_incidence_2'][::]/f['cloud_incidence_1'][::]

        plt.figure(figsize=(16,10))
        plt.rcParams['font.family'] = 'Open Sans'
        plt.viridis()
        m = Basemap()
        im = m.imshow(correction_factor.T,
        # im = m.imshow((f['cloud_incidence_1'][::]/f['cloud_incidence_1_total'][::]).T,
            interpolation='nearest',
            vmin=0.3,
            vmax=2,
            cmap=colormaps.parula
        )
        m.colorbar(im, 'right', size='5%', pad='2%')
        m.drawcoastlines(linewidth=0.1)
        m.drawcountries(linewidth=0.1)
        m.drawparallels(np.arange(-90.,99.,30.), labels=[1,0,0,1], linewidth=0.05, color='#333333')
        m.drawmeridians(np.arange(-180.,180.,60.), labels=[1,0,0,1], linewidth=0.05, color='#333333')
        plt.title(args.title)

        if args.outfile:
            plt.savefig(args.outfile, bbox_inches='tight', pad_inches=0.5)
        else:
            plt.show()

