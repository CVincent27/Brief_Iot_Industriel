from pathlib import Path
import pandas as pd

RAW_DIR = Path("data/raw")
STAGING_DIR = Path("data/staging")
STAGING_DIR.mkdir(exist_ok=True) 

csv_files = list(RAW_DIR.glob("*.csv"))

for file in csv_files:
    df = pd.read_csv(file)

    df.columns = df.columns.str.lower()

    if "elapsed_time" in df.columns:
        df = df.drop(columns=["elapsed_time"])

    output_file = STAGING_DIR / file.name
    df.to_csv(output_file, index=False)

    print(f"Nettoyage terminé : {output_file}")

print("Fichiers nettoyés dans data/staging")