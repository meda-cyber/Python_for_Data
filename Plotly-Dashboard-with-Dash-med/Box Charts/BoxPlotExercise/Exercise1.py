#######
# Objective: Make a DataFrame using the Abalone dataset (../data/abalone.csv).
# Take two independent random samples of different sizes from the 'rings' field.
# HINT: np.random.choice(df['rings'],10,replace=False) takes 10 random values
# Use box plots to show that the samples do derive from the same population.
######

# Perform imports here:
import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go
import numpy as np

# create a DataFrame from the .csv file:
df = pd.read_csv(r"./SourceData/abalone.csv")
print(df)

# take two random samples of different sizes:
a = np.random.choice(df['rings'], 100, replace=False)
b = np.random.choice(df['rings'], 40, replace=False)


# create a data variable with two Box plots:
data = [go.Box(y=a, name="A"), go.Box(y=b, name="B")]
layout = go.Layout(title="2 Random Samples")

fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename="Ex1.html")
