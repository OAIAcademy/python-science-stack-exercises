import numpy as np
import pandas as pd
import datetime

with open('pandas_library/data/d202.csv', 'r') as fp:
    df = pd.read_csv(fp)
# create a datetime column using apply to multiple column
df["time"] = df[['DATE', 'END TIME']].apply(
    lambda x: datetime.datetime.strptime(x.DATE + ' ' + x['END TIME'], '%m/%d/%Y %H:%M'), axis=1)
df = df.set_index('time')

# is often useful to have data at clear fixed interval, this can be done using the .resample method
print(df['USAGE'].resample('1H').sum())  # resample to hour interval and sum

# one can also upsample using a filling method
print(df['USAGE'].groupby(by='time').sum().resample('30S').ffill().head())  # groupby to remove duplicated indexes

# another widely used method is windowing
print(df['USAGE'].resample('1H').sum().rolling(
    window=4).mean().head())  # computing the hour average with a rolling window of 4 hour
