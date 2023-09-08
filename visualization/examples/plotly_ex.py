from datetime import datetime
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv('pandas_library/data/D202.csv')
df["time"] = df[['DATE', 'END TIME']].apply(
    lambda x: datetime.strptime(x.DATE + ' ' + x['END TIME'], '%m/%d/%Y %H:%M'), axis=1)

# scatter plot
fig = go.Figure(data=[go.Scatter(x=df['time'], y=df['USAGE'], mode='markers')])
fig.show()

#line
# Create line plot
fig = go.Figure(data=[go.Scatter(x=df['time'], y=df['USAGE'], mode='lines', name='USAGE'),
                      go.Scatter(x=df['time'], y=df['COST'], mode='lines', name='COST')])

fig.show()

#histogram
fig = go.Figure(data=[go.Histogram(x=df['USAGE'])])
fig.show()