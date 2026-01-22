import pandas as pd

# ----------------------------
# 1. Load raw data
# ----------------------------
df = pd.read_csv("../data_raw/ev_sessions_raw.csv")

print("Raw rows:", len(df))

# ----------------------------
# 2. Parse datetimes
# ----------------------------
df["start_time"] = pd.to_datetime(df["start_time"], errors="coerce")
df["end_time"] = pd.to_datetime(df["end_time"], errors="coerce")

# ----------------------------
# 3. Derive duration (minutes)
# ----------------------------
df["duration_min"] = (df["end_time"] - df["start_time"]).dt.total_seconds() / 60

# ----------------------------
# 4. Basic data quality rules
# ----------------------------
df_clean = df[
    (df["start_time"].notna()) &
    (df["end_time"].notna()) &
    (df["duration_min"] > 0) &
    (df["energy_kwh"] > 0) &
    (df["cost"] >= 0)
].copy()

# ----------------------------
# 5. Standardize text columns
# ----------------------------
df_clean["city"] = df_clean["city"].str.strip().str.title()
df_clean["vehicle_type"] = df_clean["vehicle_type"].str.strip().str.title()
df_clean["user_type"] = df_clean["user_type"].str.strip().str.title()

# ----------------------------
# 6. Final column order
# ----------------------------
final_cols = [
    "session_id",
    "station_id",
    "city",
    "start_time",
    "end_time",
    "duration_min",
    "energy_kwh",
    "cost",
    "vehicle_type",
    "user_type"
]

df_clean = df_clean[final_cols]

# ----------------------------
# 7. Save clean data
# ----------------------------
df_clean.to_csv("../data_clean/ev_sessions_clean.csv", index=False)

print("Clean rows:", len(df_clean))
print("Rows removed:", len(df) - len(df_clean))
print("Clean file written: data_clean/ev_sessions_clean.csv")
