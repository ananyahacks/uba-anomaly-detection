from faker import Faker
import pandas as pd
import random

SEED = 42
random.seed(SEED)

fake = Faker()
fake.seed_instance(SEED)

NUM_USERS = 50
LOGS_PER_USER = 40

# ------------------------
# Generate Users Table
# ------------------------
users = []

roles = ["Employee", "Manager", "Admin", "HR", "IT Support"]
departments = ["IT", "Finance", "HR", "Sales", "Operations"]

for i in range(1, NUM_USERS + 1):
    users.append({
        "User_ID": i,
        "Username": fake.user_name(),
        "Role": random.choice(roles),
        "Department": random.choice(departments)
    })

users_df = pd.DataFrame(users)
users_df.to_csv("data/raw/users.csv", index=False)

print("users.csv generated")

# ------------------------
# Generate Activity Logs
# ------------------------
logs = []
log_id = 1

resources = [
    "File_Server",
    "Email_System",
    "HR_Portal",
    "Finance_DB",
    "Customer_DB",
    "Internal_Wiki"
]

for user in users:
    for _ in range(LOGS_PER_USER):
        logs.append({
            "Log_ID": log_id,
            "User_ID": user["User_ID"],
            "Login_Timestamp": fake.date_time_between(start_date="-30d", end_date="now"),
            "IP_Address": fake.ipv4(),
            "Resource_Accessed": random.choice(resources),
            "Failed_Login_Count": random.randint(0, 5),
            "Data_Transfer_Amount": round(random.uniform(10, 5000), 2)
        })

        log_id += 1

logs_df = pd.DataFrame(logs)
logs_df.to_csv("data/raw/activity_logs.csv", index=False)

print("activity_logs.csv generated")

print("Synthetic UBA data generation complete!")
