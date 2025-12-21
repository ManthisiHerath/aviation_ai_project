print("\n-------------  Day 001  ------------------\n")

import pandas as pd

df = pd.read_csv("D:/Projects/aviation_ai_project/data/flight_delays.csv")
print(df.head()) # Display the first 5 rows of the dataset
print("\n-------------------------------\n")
print(df.shape) #how many flights you have  #how many columns (features)
print("\n-------------------------------\n")
print(df.columns) #list of all column names
print("\n-------------------------------\n")
print(df.isnull().sum())
print("\n-------------------------------\n")
print(df.describe())


print("\n-------------  Day 002  ------------------\n")

df1 = df.drop(columns=["DelayReason"])
print(df1.isnull().sum())