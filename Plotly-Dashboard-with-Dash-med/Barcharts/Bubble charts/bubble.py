import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

# importing data from sorcedato to analysis with bubble chart
df = pd.read_csv(r"SourceData\mpg.csv")
print(df)
data = [go.Scatter(
    x=df["horsepower"],
    y=df["mpg"],
    text=df["name"],
    mode="markers",
    marker=dict(size=2*df["cylinders"], color=df["cylinders"], showscale=True)
)]
layout = go.Layout(title="Bubble Charts", hovermode="closest")
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename="bubbl_chart.html")
