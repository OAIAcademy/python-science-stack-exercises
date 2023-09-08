from datetime import datetime

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


# line


x = np.linspace(0, 10, 101)
y = x ** 2

plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('y = x^2')
plt.show()

# scatter
x = np.random.rand(50)
y = np.random.rand(50)

plt.scatter(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Scatter Plot')
plt.show()

# bar
grades = ['A', 'B', 'C', 'D']
counts = [10, 20, 15, 5]

plt.bar(grades, counts)
plt.xlabel('Grades')
plt.ylabel('Counts')
plt.title('Test Scores')
plt.show()

# histogram
data = np.random.normal(0, 1, 1000)

plt.hist(data, bins=30)
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram')
plt.show()

# pie plot

labels = ['A', 'B', 'C', 'D']
sizes = [15, 30, 45, 10]

fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
ax1.axis('equal')
plt.show()

# multiple line
x = np.linspace(0, 10, 101)
y = x ** 2
y1 = x ** 1.5
y2 = -x ** 1.1

plt.plot(x, y)
plt.plot(x, y1)
plt.plot(x, y2)
plt.xlabel('x')
plt.ylabel('y')
plt.title('multi')
plt.show()

# log
x = np.linspace(0, 100, 101)
y = np.exp(x)

plt.plot(x, y)
plt.yscale("log")
plt.xlabel('x')
plt.ylabel('y')
plt.title('log')
plt.show()

# from pandas
with open('pandas_library/data/D202.csv', 'r') as fp:
    df = pd.read_csv(fp)

df["time"] = df[['DATE', 'END TIME']].apply(
    lambda x: datetime.strptime(x.DATE + ' ' + x['END TIME'], '%m/%d/%Y %H:%M'), axis=1)
df = df.set_index('time')
df['COST'] = df['COST'].apply(lambda x: float(x.replace("$", "")))

df[['USAGE', 'COST']].plot()
plt.show()
