import numpy as np


def mask_datasets(datasets, mask):
    return {
        k: np.take(v, np.nonzero(mask)[0], axis=0)
        for k, v in datasets.iteritems()
    }


def log(data, msg):
    data['log'] = data.get('log', [])
    data['log'].append(msg)


def subset_datasets(datasets, start, len):
    return {
        k: np.take(v, np.arange(start, min(start + len, v.shape[0])), axis=0)
        for k, v in datasets.iteritems()
    }
