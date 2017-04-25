import h5py
import argparse
import numpy as np


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Print fraction of cloudy profiles')
    parser.add_argument('file', type=str, help='HDF5 input file')

    args = parser.parse_args()

    with h5py.File(args.file) as f:
        print 1.0 - 1.0*f['cloud_incidence_clear'][()]/f['cloud_incidence_total'][()]
