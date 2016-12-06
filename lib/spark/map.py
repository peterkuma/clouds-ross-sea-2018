import copy
import zipfile
import tempfile
import dpath
import numpy as np
import h5py
import xarray as xr
from ccplot.hdfeos import HDFEOS

from .misc import mask_datasets, subset_datasets
from ..daynight import daynight


def noop():
    def f(data):
        return data
    return f


def unzip():
    def f(data):
        with zipfile.ZipFile(data['filename'], 'r') as zip:
            name = zip.namelist()[0]
            data['file_data'] = zip.open(name).read()
            return data
    return f


def hdfeos(dataset_names, xarray=False):
    def f(data):
        with tempfile.NamedTemporaryFile(suffix='.hdf') as f:
            f.write(data['file_data'])
            f.flush()
            f.tell()
            with HDFEOS(f.name) as product:
                if xarray:
                    data['datasets'] = xr.Dataset({
                        k: {
                            (
                                v['coords'],
                                product[v['swath']][v['dataset']][::]
                            )
                        }
                        for k, v, in dataset_names.iteritems()
                    })
                else:
                    data['datasets'] = {
                        k: product[v['swath']][v['dataset']][::]
                        for k, v, in dataset_names.iteritems()
                    }
                del data['file_data']
                return data
    return f


def h5(dataset_names):
    def f(data):
        with h5py.File(data['filename'], 'r') as f:
            data['datasets'] = {
                k: f[v['dataset']][::]
                for k, v, in dataset_names.iteritems()
            }
        return data
    return f


def filter_area(func):
    def f(data):
        mask = func(data['datasets']['lon'], data['datasets']['lat'])
        data['datasets'] = mask_datasets(data['datasets'], mask)
        return data
    return f


def filter_cloudsat_quality(dataset_name):
    def f(data):
        data_quality = data['datasets'][dataset_name]
        mask = data_quality == 0
        data['datasets'] = mask_datasets(data['datasets'], mask)
        return data
    return f


def select(name):
    def f(data):
        return dpath.util.get(data, name)
    return f


def lon_rel(lon_0, lon_dir):
    def f(data):
        data['datasets']['lon_0'] = lon_0
        data['datasets']['lon_dir'] = lon_dir
        lon_360 = data['datasets']['lon'] % 360.0
        data['datasets']['lon_rel'] = (lon_360 - lon_0)*lon_dir
        return data
    return f


def expect(func):
    def f(data):
        try:
            return func(data)
        except Exception as e:
            data['exceptions'] = data.get('exceptions', [])
            data['exceptions'].append(`e`)
            return data
    return f


def split(n):
    def f(data):
        return [
            dict(
                copy.deepcopy(data),
                datasets=subset_datasets(data['datasets'], i*n, n)
            )
            for i in xrange(int(np.ceil(1.0*data['datasets']['lon'].size/n)))
        ]
    return f


def size(dataset_name):
    def f(data):
        return data['datasets'][dataset_name].size
    return f


def cloudsat_time():
    def f(data):
        data['datasets']['time'] = (
            data['datasets']['tai_start'] +
            data['datasets']['profile_time']
        )
        del data['datasets']['tai_start']
        del data['datasets']['profile_time']
        return data
    return f


def cloudsat_daynight():
    def f(data):
        data['datasets']['daynight'] = daynight(
            data['datasets']['lon'],
            data['datasets']['lat'],
            data['datasets']['time']
        )
        return data
    return f


def filter_daynight(daynight):
    def f(data):
        mask = data['datasets']['daynight'] == daynight
        data['datasets'] = mask_datasets(data['datasets'], mask)
        return data
    return f


def include(names):
    def f(data):
        data['datasets'] = { k: data['datasets'][k] for k in names }
        return data
    return f
