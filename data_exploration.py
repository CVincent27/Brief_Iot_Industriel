from pathlib import Path
import pandas as pd

RAW_DIR = Path("data/raw")

csv_files = list(RAW_DIR.glob("*.csv"))

datasets = {}

for file in csv_files:
    datasets[file.name] = pd.read_csv(file)

print(f"{len(datasets)} fichiers chargés")

for name, df in datasets.items():
    print(f"\n{name}")
    print(f"Lignes : {df.shape[0]}")


schemas = {
    name: set(df.columns)
    for name, df in datasets.items()
}

for name, df in datasets.items():
    print(f"\n{name}")
    print(df.dtypes)

    print(df.isna().sum())
    print(df.describe())