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


df1 = df.drop(columns=["DelayReason"])
print(df1.isnull().sum())
print("\n--- Converting date & time columns ---\n")
df1["ScheduledDeparture"] = pd.to_datetime(df1["ScheduledDeparture"])
df1["ActualDeparture"] = pd.to_datetime(df1["ActualDeparture"])
df1["ScheduledArrival"] = pd.to_datetime(df1["ScheduledArrival"])
df1["ActualArrival"] = pd.to_datetime(df1["ActualArrival"])
df1["DepartureDelay"] = (df1["ActualDeparture"] - df1["ScheduledDeparture"]).dt.total_seconds() / 60
df1["FlightDuration"] = (df1["ActualArrival"] - df1["ActualDeparture"]).dt.total_seconds() / 60
print("\n--- After processing date & time ---\n")
print(df1.head())
print(df1.info())

