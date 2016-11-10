import sys
import os
from os import path
import h5py
import glob
import argparse
from pyspark import SparkContext

sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from lib import hdfeos_subset
from lib.areas import is_ross_sea, is_ross_ice_shelf

AREAS = {
    'ross_sea': is_ross_sea,
    'ross_ice_shelf': is_ross_ice_shelf
}

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Extract Area')
    parser.add_argument('files', metavar='FILES', type=str,
                       help='files glob', nargs='?')
    parser.add_argument('-f', dest='file', type=str,
                       help='file containing list of files')
    parser.add_argument('-o', dest='outfile', type=str,
                       help='output h5 file', required=True)
    parser.add_argument('-a', dest='area', type=str,
                       help='area name', required=True)

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

    hdfeos_subset(sc, args.outfile, filenames, area_func, {
        'data_quality': {
            'swath': '2B-GEOPROF-LIDAR',
            'dataset': 'Data_quality'
        },
        'layer_top': {
            'swath': '2B-GEOPROF-LIDAR',
            'dataset': 'LayerTop'
        },
        'layer_base': {
            'swath': '2B-GEOPROF-LIDAR',
            'dataset': 'LayerBase'
        },
        'cloud_layers': {
            'swath': '2B-GEOPROF-LIDAR',
            'dataset': 'CloudLayers'
        },
        'lat': {
            'swath': '2B-GEOPROF-LIDAR',
            'dataset': 'Latitude'
        },
        'lon': {
            'swath': '2B-GEOPROF-LIDAR',
            'dataset': 'Longitude'
        },
        'flag_top': {
            'swath': '2B-GEOPROF-LIDAR',
            'dataset': 'FlagTop'
        },
        'flag_base': {
            'swath': '2B-GEOPROF-LIDAR',
            'dataset': 'FlagBase'
        }
    })

    sc.stop()
