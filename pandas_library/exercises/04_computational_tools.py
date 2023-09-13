import pandas as pd

url = "https://storage.googleapis.com/academy-datasets-public/exercises/california-house-prices/california_housing_test.csv"
df = pd.read_csv(url)

# 1 - compute standard deviation of median_income for sample with grater than average total_bedrooms
# 2 - compute maximum ratio of population to rooms
# 3 - compute median bedrooms value using 300 random samples weighted by population
# 4 - compute average remainder (a%b) of  total_rooms / total_bedrooms  (hint apply to multiple columns)

# SOLUTION
# 1
print(
    df[df['total_bedrooms'] > df['total_bedrooms'].mean()]  # filter with boolean indexing
    ['median_income']  # select column
        .std()  # compute std on series
)
# 2
print(
    (df['population'] / df['total_rooms']).max()  # simply dividing the columns
)
# 3
print(
    df.sample(300, weights='population')['total_bedrooms'].median()
)
# 4
print(
    df[['total_rooms', 'total_bedrooms']].apply(lambda x: x.total_rooms % x.total_bedrooms, axis=1).mean()
)
