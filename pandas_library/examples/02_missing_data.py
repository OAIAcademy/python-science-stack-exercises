import numpy as np
import pandas as pd

url = "https://storage.googleapis.com/academy-datasets-public/exercises/california-house-prices/california_housing_test.csv"
df = pd.read_csv(url)
df.loc[df["latitude"] < 33, "median_house_value"] = None
df.loc[(df["latitude"] > 33) & (df["latitude"] < 34), "median_house_value"] = np.NAN

# some time data source has missing or invalid data, and this can create problems on calculation
print(df.info())
# .fillna fill the null/na value with the selected method
df.fillna(0)
# fill with 0
df.fillna('a')  # fill with a string
df.fillna(method='ffill')  # use last valid value
df.fillna(method='backfill')  # use next valid value
values = {1: 0, 2: 1, 4: 2, 3: 3}
df.fillna(value=values)  # fill with specific value for index
# one can also drop na with .dropna()
df.dropna()
# there are also more advance method of filling missing like .interpolate(), which uses linear (by default) interpolation
df.interpolate()
