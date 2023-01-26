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
print(df.groupby("total_rooms").mean()) # group by colums and aggregate by sum

