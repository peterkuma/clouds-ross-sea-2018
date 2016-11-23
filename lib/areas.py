import numpy as np


def is_ross_sea(lon, lat):
    return (
        ((lat <= -75.0) & (lat >= -78.0)) & (
            ((lon >= 160) & (lon <= 180.0)) |
            ((lon >= -180) & (lon <= -150.0))
        )
    )


def is_ross_ice_shelf(lon, lat):
    return (
        ((lat <= -78.0) & (lat >= -82.0)) & (
            ((lon >= 160) & (lon <= 180.0)) |
            ((lon >= -180) & (lon <= -150.0))
        )
    )


def is_ross_area(lon, lat):
    return is_ross_sea(lon, lat) | is_ross_ice_shelf(lon, lat)


def is_any_area(lon, lat):
    return np.ones(lat.size)
