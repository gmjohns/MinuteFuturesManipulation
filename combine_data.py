import pandas as pd
import os

time_steps = pd.DataFrame({'timestamp': pd.DatetimeIndex(start='01/01/2009', freq='1min', end='12/31/2018')})
f_list = ['GC', 'SI', 'PL']
f = f_list[0]

for f in f_list[:]:
    df = pd.read_csv(os.getcwd() + '/minute_futures_data/' + f + '.txt', sep=",", header=None)
    df.columns = ['date', 'time', 'open', 'close', 'high', 'low', 'volume']

    new_df = pd.DataFrame({'timestamp': pd.to_datetime(df['date'] + ' ' + df['time'], format="%m/%d/%Y %H:%M"),
                           f+'close': df['close']})
    print(f)

    time_steps = time_steps.merge(new_df, how='outer')

time_steps.fillna(method='ffill', inplace=True)
print(time_steps)
time_steps.to_csv('full.csv', sep=',', index=False)