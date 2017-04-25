import sys
import numpy as np
import pandas as pd
import h5py
import argparse


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Print regime-season table')
    parser.add_argument('file', type=str, help='HDF5 input file')
    args = parser.parse_args()

    with h5py.File(args.file) as f:
        df = pd.DataFrame(
            f['regime_season_hist'][::],
            columns=f['seasons'][:],
            index=f['regimes'][:]
        )

        for i in xrange(df.shape[0]):
            row = df.iloc[i]
            df.iloc[i] = 100.0*row/np.sum(row)

        df['all'] = 100.0*np.sum(f['regime_season_hist'][::], axis=1) / \
            np.sum(f['regime_season_hist'][::])

        sys.stdout.write(df.to_csv(float_format='%0.f'))
