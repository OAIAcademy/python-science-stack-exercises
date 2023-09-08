import pandas as pd

# pandas provide some basic method on statistical analysis, here are some example
url = "https://storage.googleapis.com/academy_datasets/exercises/california-house-prices/california_housing_test.csv"
df = pd.read_csv(url)
print("average ", df.median_house_value.mean())
print("median ", df.median_house_value.median())
print("standard deviation ", df.median_house_value.std())
print("kurtosis ", df.median_house_value.kurt())
# one useful method is sample, which select n random sample
print(df.sample(1000).count())
print(df.sample(frac=0.2).count())

print(df.sample(100, weights=df["total_rooms"]).count())  # use Series as weight
# one useful method is .apply, it is used to apply a function to a whole series or dataframe
print("apply ", df.total_rooms.apply(lambda x: x / df.total_rooms.max()).max())
