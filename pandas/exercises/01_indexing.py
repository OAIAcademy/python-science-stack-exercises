import pandas as pd

with open('pandas/data/D202.csv', 'r') as fp:
    df = pd.read_csv(fp)
# 1 - using the provided df change the values to be in Wh and not kWh (multiply by 1000 the usage value and change the units)
# 2 - set to $0.00 the cost of all usage less than 100 Wh
# 3 - create a new df with only the 10/22/2016 values
# 4 - from the new df select the 1:30 cost value

# SOLUTIONS
# 1
df['USAGE'] = df['USAGE'] * 1000
df['UNITS'] = 'Wh'  # substitute the whole column with a single value
print(df[['USAGE', 'UNITS']].head())
# 2
df.loc[df['USAGE'] < 100, 'COST'] = '$0.00'
print(df[df['USAGE'] < 100][['USAGE', 'COST']])
# 3
df_new = df[df['DATE'] == '10/22/2016']
print(df_new.info())
# 4
i = df_new[df['START TIME'] == '1:30'].index[0]  # et the index value
print(df_new.at[i, "COST"])
