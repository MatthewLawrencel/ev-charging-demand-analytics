import pandas as pd
import random
from faker import Faker
from datetime import datetime, timedelta

fake = Faker()

cities = ["Bengaluru", "Delhi", "Mumbai", "Chennai", "Hyderabad"]
vehicle_types = ["Sedan", "SUV", "Hatchback"]
user_types = ["Public", "Private"]

rows = []

for i in range(100_000):   # big but manageable
    city = random.choice(cities)
    start = fake.date_time_between(start_date="-30d", end_date="now")
    duration = random.randint(10, 120)
    end = start + timedelta(minutes=duration)

    energy = round(duration * random.uniform(0.18, 0.30), 2)
    cost = round(energy * random.uniform(8, 14), 2)

    rows.append({
        "session_id": f"S{i+1}",
        "station_id": f"ST{random.randint(1,300)}",
        "city": city,
        "start_time": start,
        "end_time": end,
        "energy_kwh": energy,
        "cost": cost,
        "vehicle_type": random.choice(vehicle_types),
        "user_type": random.choice(user_types)
    })

df = pd.DataFrame(rows)

df.to_csv("../data_raw/ev_sessions_raw.csv", index=False)

print("Rows generated:", len(df))
