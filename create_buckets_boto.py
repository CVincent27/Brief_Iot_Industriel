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

buckets = [
    "raw",
    "staging",
    "curated",
    "archive"
]

for bucket in buckets:
    existing = [b["Name"] for b in s3.list_buckets()["Buckets"]]

    if bucket not in existing:
        s3.create_bucket(Bucket=bucket)
        print(f"Bucket créé : {bucket}")
    else:
        print(f"Bucket existe déjà : {bucket}")