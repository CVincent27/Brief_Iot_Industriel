import pandas as pd
from pathlib import Path

STAGING_DIR = Path("data/staging")
CURATED_DIR = Path("data/curated")
CURATED_DIR.mkdir(exist_ok=True)


df = pd.read_csv(STAGING_DIR / "LineC_Turbulent.csv")

df["timestamp"] = pd.to_datetime(df["timestamp"]) 
hourly_agg = df.groupby(pd.Grouper(key="timestamp", freq="1H")).agg({
    "temperature": ["mean", "min", "max"],
    "pressure": "mean",
}).reset_index()
hourly_agg.columns = ["_".join(col).strip() for col in hourly_agg.columns.values]


hourly_agg.to_csv(CURATED_DIR / "hourly_turbulence_aggregates.csv", index=False)

print("Tables Curated générées :")
print(f"   - {CURATED_DIR / 'hourly_turbulence_aggregates.csv'}")