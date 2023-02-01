import pandas as pd  # import pandas with the standard alias pd
import numpy as np

# a series is a one dimensional array (a column of a table) with an index
d = {'a': 1, 'b': 2, 'c': 3}
series = pd.Series(data=d, index=['a', 'b', 'c'])
print(series)

# a Dataframe is a two dimensional data structure with indexed rows and named columns (basically a table)
d = {'col1': [1, 2], 'col2': [3, 4]}
df = pd.DataFrame(data=d)
print(df)

# every column of the dict is a series
print(type(df['col1']))

# data frame can be created from other data structures
#       from dictionary
df = pd.DataFrame(data={'col1': [1, 2], 'col2': [3, 4]})
#       from numpy array
df = pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
                  columns=['a', 'b', 'c'])
#       from numpy array
df = pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
                  columns=['a', 'b', 'c'])
#       froma dict of series
d = {'col1': [0, 1, 2, 3], 'col2': pd.Series([2, 3], index=[2, 3])}
pd.DataFrame(data=d, index=[0, 1, 2, 3])

# and reading from sources
#          from csv
with open('pandas/data/D202.csv', 'r') as fp:
    df = pd.read_csv(fp)
#           from json
with open('pandas/data/D202.json', 'r', errors='ignore') as fp:
    df = pd.read_json(fp)
#           from url
url = "https://storage.googleapis.com/academy_datasets/exercises/california-house-prices/california_housing_test.csv"
df = pd.read_csv(url)

# some basic info about can be retrived using .describe() & .info()
print(df.info())  # info on the dataframe useful for the programmer
# Data columns (total 9 columns):
#  #   Column              Non-Null Count  Dtype
# ---  ------              --------------  -----
#  0   longitude           3000 non-null   float64
#  1   latitude            3000 non-null   float64
#  2   housing_median_age  3000 non-null   float64
#  3   total_rooms         3000 non-null   float64
#  4   total_bedrooms      3000 non-null   float64
#  5   population          3000 non-null   float64
#  6   households          3000 non-null   float64
#  7   median_income       3000 non-null   float64
#  8   median_house_value  3000 non-null   float64
# dtypes: float64(9)
# memory usage: 211.1 KB

print(df.describe())  # basic descriptive statistics
#          longitude    latitude  ...  median_income  median_house_value
# count  3000.000000  3000.00000  ...    3000.000000          3000.00000  number of valid (null/na) values in the row
# mean   -119.589200    35.63539  ...       3.807272        205846.27500  average
# std       1.994936     2.12967  ...       1.854512        113119.68747  standard deviation
# min    -124.180000    32.56000  ...       0.499900         22500.00000
# 25%    -121.810000    33.93000  ...       2.544000        121200.00000  # percentiles
# 50%    -118.485000    34.27000  ...       3.487150        177650.00000
# 75%    -118.020000    37.69000  ...       4.656475        263975.00000
# max    -114.490000    41.92000  ...      15.000100        500001.00000
#
