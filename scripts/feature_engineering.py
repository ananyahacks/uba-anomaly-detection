import pandas as pd

# ------------------------
# Load Raw Activity Logs
# ------------------------
logs = pd.read_csv("data/raw/activity_logs.csv")

print("Loaded activity_logs.csv")

# Convert timestamp to datetime
logs["Login_Timestamp"] = pd.to_datetime(logs["Login_Timestamp"])

# Extract hour for time deviation
logs["Login_Hour"] = logs["Login_Timestamp"].dt.hour

# ------------------------
# Feature Engineering
# ------------------------

# 1. Login Frequency (per user)
login_freq = logs.groupby("User_ID").size().reset_index(name="Login_Frequency")

# 2. Access Frequency (unique resources accessed)
access_freq = (
    logs.groupby("User_ID")["Resource_Accessed"]
    .nunique()
    .reset_index(name="Access_Frequency")
)

# 3. Data Transfer Volume (total per user)
data_volume = (
    logs.groupby("User_ID")["Data_Transfer_Amount"]
    .sum()
    .reset_index(name="Data_Transfer_Volume")
)

# 4. Time Deviation (std deviation of login hours)
time_deviation = (
    logs.groupby("User_ID")["Login_Hour"]
    .std()
    .reset_index(name="Time_Deviation")
)

# ------------------------
# Merge All Features
# ------------------------
features = login_freq.merge(access_freq, on="User_ID")
features = features.merge(data_volume, on="User_ID")
features = features.merge(time_deviation, on="User_ID")

# Fill NaN time deviation (users with single login)
features["Time_Deviation"] = features["Time_Deviation"].fillna(0)

# ------------------------
# Save Feature Set
# ------------------------
features.to_csv("data/processed/feature_set.csv", index=False)

print("feature_set.csv generated successfully!")
print(features.head())
