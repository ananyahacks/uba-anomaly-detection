import pandas as pd

# ------------------------
# Load Raw Data
# ------------------------
users = pd.read_csv("data/raw/users.csv")
logs = pd.read_csv("data/raw/activity_logs.csv")

print("Loaded raw users and activity logs")

# ------------------------
# Basic Data Cleaning
# ------------------------

# 1. Remove duplicate rows (if any)
users_before = len(users)
logs_before = len(logs)

users = users.drop_duplicates()
logs = logs.drop_duplicates()

print(f"Users duplicates removed: {users_before - len(users)}")
print(f"Logs duplicates removed: {logs_before - len(logs)}")

# 2. Check and handle missing values
print("\nMissing values in users:")
print(users.isna().sum())

print("\nMissing values in activity logs:")
print(logs.isna().sum())

# Drop rows with critical missing values (if any)
users = users.dropna()
logs = logs.dropna()

# 3. Enforce correct data types
logs["Login_Timestamp"] = pd.to_datetime(logs["Login_Timestamp"], errors="coerce")

logs["Failed_Login_Count"] = pd.to_numeric(
    logs["Failed_Login_Count"], errors="coerce"
)

logs["Data_Transfer_Amount"] = pd.to_numeric(
    logs["Data_Transfer_Amount"], errors="coerce"
)

# Drop rows that became invalid after type conversion
logs = logs.dropna()

# 4. Validate ranges (basic sanity checks)
logs = logs[logs["Failed_Login_Count"] >= 0]
logs = logs[logs["Data_Transfer_Amount"] > 0]

# ------------------------
# Save Cleaned Data
# ------------------------
users.to_csv("data/raw/users_cleaned.csv", index=False)
logs.to_csv("data/raw/activity_logs_cleaned.csv", index=False)

print("\nCleaned files saved:")
print(" - data/raw/users_cleaned.csv")
print(" - data/raw/activity_logs_cleaned.csv")

print("\nData cleaning completed successfully!")

