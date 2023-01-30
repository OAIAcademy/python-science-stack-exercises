import numpy as np
import pandas as pd
import datetime

with open('pandas/data/d202.csv', 'r') as fp:
    df = pd.read_csv(fp)
# create a datetime column using apply to multiple column
df["time"] = df[['DATE', 'END TIME']].apply(
    lambda x: datetime.datetime.strptime(f"{x.DATE} {x['END TIME']}", '%m/%d/%Y %H:%M'), axis=1)
df.set_index('time', inplace=True)

# 1 - using the provided df resample to day average
# 2 - resample to every minute filling with zero
# 3 - create a new column with cumulative sum of previous 60 sample


# SOLUTION

# 1
print(df['USAGE'].resample('1d').sum().head())
# 2
print(df['USAGE'].resample('1s').sum().head())  # default to zero
# 3
df["cumulative"] = df['USAGE'].rolling(window=12,
                                       min_periods=1).sum()  # min_periods allows the first 12 sample to hava a windows smaller then 12
print(df.cumulative)
