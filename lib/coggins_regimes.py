import os
import pandas as pd
import datetime as dt
import pytz
import numpy as np


regime_cluster_lookup = {
    '(2,1)': (1, 1),
    '(1,2)': (1, 0),
    '(2,2)': (1, 2),
    '(3,1)': (1, 3),
    '(3,2)': (1, 4),
    '(1,3)': (2, 5),
    '(2,3)': (2, 6),
    '(3,3)': (2, 7),
    '(1,4)': (3, 8),
    '(1,5)': (3, 9),
    '(1,6)': (3, 10),
    '(2,4)': (3, 11),
    '(2,5)': (3, 12),
    '(2,6)': (3, 13),
    '(3,4)': (4, 14),
    '(3,6)': (4, 15),
    '(4,2)': (5, 16),
    '(4,3)': (5, 17),
    '(4,4)': (5, 18),
    '(4,5)': (5, 19)
}

regime_names = [
    'n/a',
    'wnc',
    'snc',
    'ras',
    'wsc',
    'ws'
]

hours = np.array([0, 6, 12, 18])


# def read_clusters_table(filename):
#     df = pd.DataFrame.from_csv(filename, sep='\t', index_col=None)
#     df['date_str'] = (
#         np.char.array(df['year']) + '-' +
#         np.char.array(df['month']) + '-' +
#         np.char.array(df['day']) + '-' +
#         np.char.array(df['hour'])
#     )
#     df['regime'] = np.array([
#         regime_names[regime_cluster_lookup[c][0]]
#         for c in df['cluster']
#     ])
#     return df

clusters_table_filename = os.path.join(
    os.path.dirname(__file__),
    'coggins_clusters.tsv'
)

def read_clusters(filename):
    df = pd.DataFrame.from_csv(filename, sep='\t', index_col=None)
    df['regime'] = np.array([
        regime_names[regime_cluster_lookup[c][0]]
        for c in df['cluster']
    ])
    clusters = {}
    for i, row in df.iterrows():
        key = '%04d-%02d-%02d-%02d' % (
            row['year'],
            row['month'],
            row['day'],
            row['hour']
        )
        clusters[key] = df.loc[i, 'regime']
    return clusters

# clusters_table = read_clusters_table(clusters_table_filename)

clusters_lookup = None


def coggins_regimes(
    time,
    origin=dt.datetime(1993, 1, 1, tzinfo=pytz.utc)
):
    global clusters_lookup

    if clusters_lookup is None:
        clusters_lookup = read_clusters(clusters_table_filename)

    time_dt = [
        origin + dt.timedelta(0, t)
        for t in time
    ]

    year = np.array([t.year for t in time_dt])
    month = np.array([t.month for t in time_dt])
    day = np.array([t.day for t in time_dt])
    hour = np.array([t.hour for t in time_dt])
    indexes = np.searchsorted(
        hours,
        hour,
        side='right'
    ) - 1
    hourx = hours[indexes]

    keys = np.array([
        '%04d-%02d-%02d-%02d' % (
            year[i],
            month[i],
            day[i],
            hourx[i]
        )
        for i in range(len(time))
    ])

    return np.array([
        clusters_lookup[key]
        for key in keys
    ])

    # date_str = (
    #     np.char.array(year) + '-' +
    #     np.char.array(month) + '-' +
    #     np.char.array(day) + '-' +
    #     np.char.array(hourx)
    # )
    # print date_str
    # print clusters_table[37977]
    # indexes = np.searchsorted(clusters_table['date_str'], date_str)
    # print indexes
    # mask = clusters_table['date_str'][indexes] == date_str
    # print clusters_table['date_str'][indexes]
    # print mask
    # regimes = clusters_table['regime'][indexes]
    # regimes[~mask] = 'N/A'
    # return np.array(regimes)

# print (dt.datetime(2004, 12, 29, 9, tzinfo=pytz.utc) - dt.datetime(1993, 1, 1, tzinfo=pytz.utc)).total_seconds()

# print coggins_clusters(np.array([
#     (dt.datetime(2004, 12, 25, 0, tzinfo=pytz.utc) - dt.datetime(1993, 1, 1, tzinfo=pytz.utc)).total_seconds()
# ]))
