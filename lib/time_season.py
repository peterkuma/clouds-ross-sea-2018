import os
import pandas as pd
import datetime as dt
import pytz
import numpy as np


season_lookup = {
    1: 'djf',
    2: 'djf',
    3: 'mam',
    4: 'mam',
    5: 'mam',
    6: 'jja',
    7: 'jja',
    8: 'jja',
    9: 'son',
    10: 'son',
    11: 'son',
    12: 'djf'
}


def time_season(
    time,
    origin=dt.datetime(1993, 1, 1, tzinfo=pytz.utc)
):
    return np.array([
        season_lookup[(origin + dt.timedelta(0, t)).month]
        for t in time
    ])
