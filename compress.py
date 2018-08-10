import pandas as pd
import numpy as np
import os


def get_vpp(data):
    eod_v = data.groupby('date')['volume'].sum()
    avg = eod_v.mean()
    return avg/ppd


def make_seq(data, vpp):
    rv = 0
    i = 0
    new_ser = [[0, data['volume'][0]]]

    while i < data['volume'].size:
        while rv < vpp and i < data['volume'].size:
            rv += data['volume'][i]
            i += 1
        rv = rv - vpp
        new_ser.append([i-1, rv])
    return pd.DataFrame(new_ser, columns=['index', 'rem'])


def compress(data, seq):
    n = 0
    full = []
    while n <= seq.size/2-2:
        segment = data.iloc[seq['index'][n]:seq['index'][n+1]+1, :].copy()
        segment.iloc[0, 6] = seq['rem'][n]
        segment.iloc[-1, 6] = segment.iloc[-1, 6] - seq['rem'][n+1]
        print(segment)
        point = [str(segment.iloc[-1, 0]), str(segment.iloc[-1, 1]),
                 np.average(segment.iloc[:, 3], weights=segment.iloc[:, 6])]
        n += 1
        full.append(point)
    return pd.DataFrame(full, columns=['date', 'time', 'vwa'])


fname = 'CL'
ppd = 100
raw = pd.read_csv(os.getcwd() + '/minute_futures_data/' + fname + '.txt', sep=",", header=None)
raw.columns = ['date', 'time', 'open', 'close', 'high', 'low', 'volume']
vpp = get_vpp(raw)
seq = make_seq(raw, vpp)
cdf = compress(raw, seq)
cdf.to_csv(fname + 'compressed.csv', sep=',', index=False)

