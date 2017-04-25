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


def is_ross_sea_east(lon, lat):
    return is_ross_sea(lon, lat) & ((lon < 0.0) & (lon >= -175.0))


def is_ross_sea_west(lon, lat):
    return is_ross_sea(lon, lat) & ((lon < -175.0) | (lon >= 0.0))


def is_ross_ice_shelf_east(lon, lat):
    return is_ross_ice_shelf(lon, lat) & ((lon < 0.0) & (lon >= -175.0))


def is_ross_ice_shelf_west(lon, lat):
    return is_ross_ice_shelf(lon, lat) & ((lon < -175.0) | (lon >= 0.0))


def is_ross_area(lon, lat):
    return is_ross_sea(lon, lat) | is_ross_ice_shelf(lon, lat)


def is_any_area(lon, lat):
    return np.ones(lat.size)


areas = {
    'any': is_any_area,
    'ross_sea': is_ross_sea,
    'ross_sea_east': is_ross_sea_east,
    'ross_sea_west': is_ross_sea_west,
    'ross_ice_shelf': is_ross_ice_shelf,
    'ross_ice_shelf_east': is_ross_ice_shelf_east,
    'ross_ice_shelf_west': is_ross_ice_shelf_west
}
