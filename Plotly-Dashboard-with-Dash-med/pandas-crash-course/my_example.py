
import numpy as np
import pandas as pd


df = pd.read_csv(
    r"C:\Users\User\Desktop\My_projects\Python_for_Data_science\Plotly-Dashboard-with-Dash-med\pandas-crash-course\salaries.csv")
print(df)
# we can print also like this
print(df[["Name", "Salary"]])


# we can find out the minimum salary
print(df["Salary"].min())  # or print(df["Salary"].mean())


# conditional filtering
ser_of_bool = df["Age"] > 30
print(ser_of_bool)

# we can do the above in advanced level
print(df[df["Age"] > 30])

# unique values
print(df["Age"].unique())


# if we want for memory capacity
print(df.info())

# For statstical clarification
print(df.describe())
