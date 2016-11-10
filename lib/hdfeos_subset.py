from pyspark import SparkContext

from spark.map import unzip, hdfeos, filter_area, select, expect
from spark.filter import not_empty, not_bad
from . import h5_save


def hdfeos_subset(sc, h5_filename, filenames, area_func, dataset_names):
    data = [{'filename': x} for x in filenames]

    res = sc.parallelize(data) \
        .map(expect(unzip())) \
        .map(expect(hdfeos(dataset_names))) \
        .filter(not_bad()) \
        .map(filter_area(area_func)) \
        .filter(not_empty('lon')) \
        .collect()

    f = h5_save(h5_filename)
    for data in res:
        f(data)
