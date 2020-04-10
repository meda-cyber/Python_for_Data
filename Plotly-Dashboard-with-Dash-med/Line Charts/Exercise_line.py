#######
# Objective: Using the file 2010YumaAZ.csv, develop a Line Chart
# that plots seven days worth of temperature data on one graph.
# You can use a for loop to assign each day to its own trace.
######

# Perform imports here:
import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

# Create a pandas DataFrame from 2010YumaAZ.csv
df = pd.read_csv(
    r"C:\Users\User\Desktop\My_projects\Python_for_Data_science\Plotly-Dashboard-with-Dash-med\SourceData/2010YumaAZ.csv")
print(df)
days = ['TUESDAY', 'WEDNESDAY', 'THURSDAY',
        'FRIDAY', 'SATURDAY', 'SUNDAY', 'MONDAY']


# Use a for loop (or list comprehension to create traces for the data list)
data = []

for day in days:
    # What should go inside this Scatter call?
    trace = go.Scatter(x=df["LST_TIME"], y=df[df["DAY"]
                                              == day]["T_HR_AVG"], mode="lines", name=day)
    data.append(trace)

# Define the layout
layout = go.Layout(title="Daily temp avgs")


# Create a fig from data and layout, and plot the fig
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig)
