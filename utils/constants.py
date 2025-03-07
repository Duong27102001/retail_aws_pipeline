import configparser
import os
paser = configparser.ConfigParser()

config_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'config', 'config.conf')
paser.read(config_path)

#AWS
AWS_ACCESS_KEY_ID = paser.get('aws', 'aws_access_key_id')
AWS_SECRET_ACCESS_KEY = paser.get('aws', 'aws_secret_access_key')
AWS_REGION = paser.get('aws', 'aws_region')
AWS_BUCKET_NAME = paser.get('aws', 'aws_bucket_name')

#database
DATABASE_HOST = paser.get('database', 'database_host')
DATABASE_NAME = paser.get('database', 'database_name')
DATABASE_PORT = paser.get('database', 'database_port')
DATABASE_USERNAME = paser.get('database', 'database_username')
DATABASE_PASSWORD = paser.get('database', 'database_password')

#s3_buckets
S3_BUCKET_RAW = paser.get('s3_buckets', 's3_bucket_raw')
S3_BUCKET_PROCESSED = paser.get('s3_buckets', 's3_bucket_processed')

#local_path
LOCAL_DATA_DIR = paser.get('local_path', 'local_data_dir')