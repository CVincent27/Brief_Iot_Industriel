from pathlib import Path
import shutil
from datetime import datetime

RAW_DIR = Path("data/raw") 
ARCHIVE_RAW_DIR = Path("data/archive")
ARCHIVE_RAW_DIR.mkdir(parents=True, exist_ok=True) 

today = datetime.now().strftime("%Y-%m-%d")

for file in RAW_DIR.glob("*.csv"):
    archive_path = ARCHIVE_RAW_DIR / f"{today}_{file.name}"
    shutil.copy2(file, archive_path)

    print(f"Archivé : {file.name} dans {archive_path}")