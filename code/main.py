import pandas as pd

df = pd.read_csv("D:/Projects/aviation_ai_project/data/flight_delays.csv")
print(df.head()) # Display the first 5 rows of the dataset
print("\n-------------------------------\n")
print(df.shape) #how many flights you have  #how many columns (features)
print("\n-------------------------------\n")
print(df.columns) # List of all column names
print("\n-------------------------------\n")
print(df.isnull().sum()) # Check for missing values in each column
print("\n-------------------------------\n")
print(df.describe()) # Get summary statistics for numerical columns
print("\n-------------------------------\n\n")

'''
     We can drop the "DelayReason" column as it contains categorical data 
     that may not be directly useful for our analysis.
'''
df1 = df.drop(columns=["DelayReason"])
print(df1.isnull().sum())
print("\n-------------------------------\n")
# Converting date & time columns to datetime format
# Convert the "ScheduledDeparture" column to datetime format
df1["ScheduledDeparture"] = pd.to_datetime(df1["ScheduledDeparture"])
# Convert the "ActualDeparture" column to datetime format
df1["ActualDeparture"] = pd.to_datetime(df1["ActualDeparture"])
# Convert the "ScheduledArrival" column to datetime format
df1["ScheduledArrival"] = pd.to_datetime(df1["ScheduledArrival"])
# Convert the "ActualArrival" column to datetime format
df1["ActualArrival"] = pd.to_datetime(df1["ActualArrival"])
# Calculate the departure delay and flight duration in minutes
df1["DepartureDelay"] = (df1["ActualDeparture"] - df1["ScheduledDeparture"]).dt.total_seconds() / 60
df1["FlightDuration"] = (df1["ActualArrival"] - df1["ActualDeparture"]).dt.total_seconds() / 60
''' 
   After processing date & time columns, we can check the first 
   few rows and the info of the DataFrame again
'''
print(df1.head())
print("\n-------------------------------\n")
print(df1.info())
print("\n-------------------------------\n\n")

