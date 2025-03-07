import os, sys

import botocore.exceptions
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import boto3
import botocore
from utils.constants import AWS_SECRET_ACCESS_KEY, AWS_ACCESS_KEY_ID, AWS_REGION
def connect_to_s3() -> boto3.client:
    try:
        s3 = boto3.client(
        's3',
        aws_access_key_id = AWS_ACCESS_KEY_ID,
        aws_secret_access_key = AWS_SECRET_ACCESS_KEY,
        region_name = AWS_REGION)
    except Exception as e:
        print(e)
    return s3

def create_bucket_if_not_exists(s3: boto3.client, bucket_name: str) -> None:
    try:
        existing_buckets = [bucket['Name'] for bucket in s3.list_buckets().get('Buckets', [])]
        if bucket_name in existing_buckets:
            print(f"Bucket {bucket_name} already exists.")
            return
        else:
            s3.create_bucket(Bucket = bucket_name, CreateBucketConfiguration={"LocationConstraint": AWS_REGION} )
            print(f"Bucket {bucket_name} has been successfully created!")
    except Exception as e:
        print(e)
        
def upload_to_S3(s3: boto3.client, file_path: str, bucket_name: str, s3_file_name: str) -> None:
    s3_key = f"raw/{s3_file_name}"
    try:
        s3.head_object(Bucket=bucket_name, Key=s3_key)
        print(f"File {s3_key} already exists. Skipping upload.")
        return
    except botocore.exceptions.ClientError as e:
        if e.response['Error']['Code'] == 404:
            try:
                s3.upload_file(file_path, bucket_name, s3_key)
                print(f"Upload successfully: {file_path} -> s3://{bucket_name}/{s3_key}")
            except Exception as e:
                print(f"error while uploading file: {e}")
    except Exception as e:
        print(e)