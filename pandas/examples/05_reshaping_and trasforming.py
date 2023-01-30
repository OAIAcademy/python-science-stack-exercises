import numpy as np
import pandas as pd

url = "https://storage.googleapis.com/academy_datasets/exercises/california-house-prices/california_housing_test.csv"
df = pd.read_csv(url)
# to change to index of a df
print(df.index)
print(df.reindex(pd.RangeIndex(1000, 4000, 1)).index)

# .T return the transposed dataframe (switches columns and rows)
print(df.T)

# .pivot is used to create a new table using the original table data

print(df.pivot(index="population", columns='total_rooms',
               values="median_house_value"))  # index is the columns to be useed as index, columns the new columns and values the value to assing

# drop and drop_duplicates
print(df.drop("latitude", axis="columns").columns)  # drop columns
print(df.drop([1, 2, 3, 4, 5, 6], axis="rows").head())  # drop rows by index
print(df['total_rooms'].drop_duplicates().count() == len(df['total_rooms'].unique()))  # drop duplicates

# pandas features also a sql like groupby
print("group")
print(df.groupby("total_rooms").mean())  # group by column and aggregate by average
print(df.groupby("total_rooms").sum())  # group by column and aggregate by sum
print(df.groupby("total_rooms").agg({"median_income": lambda x: np.min(x)}))  # group by column custom agg
# also a sql like join (default left join)
df1 = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3', 'K4', 'K5'],
                    'A': ['A0', 'A1', 'A2', 'A3', 'A4', 'A5']})
df2 = pd.DataFrame({'key': ['K0', 'K1', 'K2'],
                    'B': ['B0', 'B1', 'B2']})
print(df1.join(df2.set_index('key'), on='key', how='inner'))
# or the merge methods, similar to join but not working on indexes (default inner)
print(df1.merge(df2, left_on='key', right_on='key', how='left'))
