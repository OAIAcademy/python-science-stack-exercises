# 1 - create a Series with number from 1 to 100
# 2 - create a dataframe with the multiplication table from 1 to 10 (index and column are the quotients), using a dict
# 3 - print the statistical description of the multiplication table of 3
# 4 - save the 2 dataframe as csv and read the resulting csv to a dataframe


# SOLUTION
# 1
import pandas as pd

s = pd.Series([i for i in range(1, 101)])
print(s.tail())  # tail return last values of df
# 2
d = {i: [i * j for j in range(1, 11)] for i in range(1, 11)}  # contextual creation of a dict
df = pd.DataFrame(d, index=d.keys(), columns=d.keys())
print(df)
# 3
print(df[3].describe())
# 4
with open('ex4.csv', 'w+') as fp:
    df.to_csv(fp)
with open('ex4.csv', 'r') as fp:
    df = pd.read_csv(fp, header=0, index_col=0)  # set first rows as header (columns names) and first column as index
print(df)
