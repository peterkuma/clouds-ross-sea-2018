import sys
import os
from os import path
import h5py
import glob
import argparse
from pyspark import SparkContext

sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from lib import h5_save
from lib.areas import is_ross_sea, is_ross_ice_shelf, is_any_area
from lib.spark.map import unzip, hdfeos, filter_area, select, expect, cloudsat_time
from lib.spark.filter import not_empty, not_bad


AREAS = {
    'ross_sea': is_ross_sea,
    'ross_ice_shelf': is_ross_ice_shelf,
    'any': is_any_area
}


PRODUCT_TYPES = {
    '2b-geoprof-lidar': {
        'swath': '2B-GEOPROF-LIDAR',
        'datasets': {
            'data_quality': 'Data_quality',
            'layer_top': 'LayerTop',
            'layer_base': 'LayerBase',
            'cloud_layers': 'CloudLayers',
            'lat': 'Latitude',
            'lon': 'Longitude',
            'flag_top': 'FlagTop',
            'flag_base': 'FlagBase',
            'profile_time': 'Profile_time',
            'tai_start': 'TAI_start'
        }
    },
    '2b-cldclass-lidar': {
        'swath': '2B-CLDCLASS-LIDAR',
        'datasets': {
            'data_quality': 'Data_quality',
            'layer_top': 'CloudLayerTop',
            'layer_base': 'CloudLayerBase',
            'cloud_layers': 'Cloudlayer',
            'cloud_phase': 'CloudPhase',
            'cloud_type': 'CloudLayerType',
            'cloud_phase': 'CloudPhase',
            'lat': 'Latitude',
            'lon': 'Longitude',
            'profile_time': 'Profile_time',
            'tai_start': 'TAI_start'
        }
    }
}


def datasets(product_type):
    return {
        k: {
            'swath': PRODUCT_TYPES[product_type]['swath'],
            'dataset': v
        }
        for k, v in PRODUCT_TYPES[product_type]['datasets'].iteritems()
    }


def data_transform(product_type):
    def f(data):
        if product_type == '2b-cldclass-lidar':
            data['datasets']['layer_top'] = data['datasets']['layer_top']*1000
            data['datasets']['layer_base'] = data['datasets']['layer_base']*1000
        return data
    return f


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Extract Area')
    parser.add_argument('files', metavar='FILES', type=str, help='files glob', nargs='?')
    parser.add_argument('-f', dest='file', type=str, help='file containing list of files')
    parser.add_argument('-o', dest='outfile', type=str, help='output h5 file', required=True)
    parser.add_argument('-a', dest='area', type=str, help='area name', required=True)
    parser.add_argument('-p', dest='product_type', type=str, help='product type ("2b-geoprof-lidar" or "2b-cldclass-lidar", default "2b-geoprof-lidar")', default='2b-geoprof-lidar')

    args = parser.parse_args()

    if args.file:
        filenames = [x.strip() for x in open(args.file).readlines()]
    else:
        filenames = glob.glob(args.files)

    area_func = AREAS[args.area]

    sc = SparkContext(appName='ExtractRossSea')

    try:
        os.remove(args.outfile)
    except OSError:
        pass

    data = [{'filename': x} for x in filenames]

    rdd = sc.parallelize(data) \
        .map(expect(unzip())) \
        .map(expect(hdfeos(datasets(args.product_type)))) \
        .map(data_transform(args.product_type)) \
        .filter(not_bad()) \
        .map(cloudsat_time()) \
        .map(filter_area(area_func)) \
        .filter(not_empty('lon'))

    res = rdd.collect()

    f = h5_save(args.outfile)
    for data in res:
        f(data)

    sc.stop()
