from pathlib import Path
import boto3
import os
from dotenv import load_dotenv

load_dotenv()

s3 = boto3.client(
    "s3",
    endpoint_url=os.getenv("MINIO_ENDPOINT"),
    aws_access_key_id=os.getenv("MINIO_ACCESS_KEY"),
    aws_secret_access_key=os.getenv("MINIO_SECRET_KEY"),
)

bucket = "raw"

data_dir = Path("data/staging/")

for file in data_dir.glob("*.csv"):
    line_name = file.stem

    object_name = f"production_lines/{line_name}/{file.name}"

    s3.upload_file(
        str(file),
        bucket,
        object_name
    )

    print(f"Upload : {object_name}")