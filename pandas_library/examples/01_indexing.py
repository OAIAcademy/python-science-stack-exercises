import datetime

import pandas as pd

with open('pandas_library/data/D202.csv', 'r') as fp:
    df = pd.read_csv(fp)
# single/mutiple column can be select
df.USAGE
df[["USAGE", "TYPE"]]
# and assigned
df["COST_NEW"] = df["COST"]

# every dataframe has an index (which can be of different type)
print(df.index)
# to select a specific row there are multiple methods
df = df.sort_values(by='END TIME')  # sort by a column
#       .loc to access rows based on the index values
print(df.loc[2])
print(df.loc[[2, 3, 4]])  # multiple using a list
print(df.loc[[2, 3, 4], "DATE"])  # also select column
print(df.loc[1:10, "DATE"])  # from value to value with slicing
#       .iloc to access rows based on the integer position

print(df.iloc[2])
print(df.iloc[[2, 3, 4]])
print(df.iloc[1:10])
#       .at to select a single value (a single cell of the table), and does not return a series like loc and iloc
print("cost:")
print(df.at[1, "COST"])
print(df.loc[5].at['COST'])  # also in a series
#       .iat like .at but positional
print(df.iat[1, 2])
print(df.loc[5].iat[2])  # also in a series

# index need to be unique but they can be of different dtype
pd.RangeIndex(start=1, stop=10, step=2)  # Range of int
pd.CategoricalIndex(categories=["a", "b", "c", "d"], dtype='category', ordered=True)  # list of label ,can be ordered
pd.DatetimeIndex(data=[datetime.datetime(year=2021, month=1, day=1), datetime.datetime(year=2022, month=1, day=1),
                       datetime.datetime(year=2023, month=1, day=1)],
                 freq="infer", closed="left", )  # datetime
pd.PeriodIndex(year=[2020, 2021, 2022], month=[1, 1, 1], freq="w")  # period first week of 2020,2021,2022

# dataframe con be filtered by using boolean indexing
# a comparison exp return a series of boolean
print(df["USAGE"] > 0.10)
# which can then be used to select specific rows
print(df[df["USAGE"] > 0.10].info())
