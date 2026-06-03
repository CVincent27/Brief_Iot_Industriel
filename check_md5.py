import hashlib
import os
from pathlib import Path
import boto3
from dotenv import load_dotenv

load_dotenv()

s3 = boto3.client(
    "s3",
    endpoint_url=os.getenv("MINIO_ENDPOINT"),
    aws_access_key_id=os.getenv("MINIO_ACCESS_KEY"),
    aws_secret_access_key=os.getenv("MINIO_SECRET_KEY"),
)

bucket = "raw"

data_dir = Path("data")


def md5_file(path):
    h = hashlib.md5()

    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            h.update(chunk)

    return h.hexdigest()


for file in data_dir.glob("*.csv"):
    line_name = file.stem

    key = f"production_lines/{line_name}/{file.name}"

    response = s3.head_object(
        Bucket=bucket,
        Key=key
    )

    etag = response["ETag"].replace('"', '')
    local_md5 = md5_file(file)

    print(f"\n{file.name}")
    print(f"Local  : {local_md5}")
    print(f"MinIO  : {etag}")

    if local_md5 == etag:
        print("✓ Intégrité OK")
    else:
        print("✗ Hash différent")

response = s3.list_objects_v2(
    Bucket="raw",
    Prefix="production_lines/"
)

for obj in response.get("Contents", []):
    print(obj["Key"])