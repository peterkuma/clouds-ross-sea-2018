import Pysolar
import datetime as dt
import numpy as np


def daynight(lon, lat, time):
    origin = dt.datetime(1970, 1, 1)
    n = len(lon)
    out = np.zeros(n)
    for i in range(n):
        # Ignore leap seconds.
        t = origin + dt.timedelta(0, time[i])
        out[i] = Pysolar.solar.GetAltitude(lat[i], lon[i], t) > 0
    return out
