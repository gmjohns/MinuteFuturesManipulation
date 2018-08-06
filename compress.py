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
    new_ser = []

    while i < data['volume'].size:
        while rv < vpp and i < data['volume'].size:
            rv += data['volume'][i]
            i += 1
        if i != data['volume'].size:
            new_ser.append(i)
        rv = rv-vpp
    return pd.Series(new_ser)


def compress(data, seq):
    n = 0
    full = []
    print(seq)
    while n <= seq.size-2:
        segment = data.iloc[[seq[n],seq[n+1]], :]
        point = [str(segment.iloc[-1, 0]), str(segment.iloc[-1, 1]),
                np.average(segment.iloc[:, 3], weights=segment.iloc[:, 6])]
        n += 1
        full.append(point)
        '''print(point)'''

    return pd.DataFrame(full, columns=['date', 'time', 'vwa'])


fname = 'test1'
ppd = 2
raw = pd.read_csv(os.getcwd() + '/minute_futures_data/' + fname + '.txt', sep=",", header=None)
raw.columns = ['date', 'time', 'open', 'close', 'high', 'low', 'volume']
vpp = get_vpp(raw)
seq = make_seq(raw, vpp)
cdf = compress(raw, seq)
cdf.to_csv(fname + 'compressed.csv', sep=',', index=False)

