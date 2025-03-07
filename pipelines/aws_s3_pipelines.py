import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from etls.aws_etl import connect_to_s3, upload_to_S3, create_bucket_if_not_exists
from utils.constants import AWS_BUCKET_NAME, LOCAL_DATA_DIR
def upload_s3_pipeline():
    s3 = connect_to_s3()
    create_bucket_if_not_exists(s3, AWS_BUCKET_NAME)
    
    try:
        for root, _, files in os.walk(LOCAL_DATA_DIR):
            for file in files:
                file_path = os.path.join(root, file)  
                upload_to_S3(s3,file_path, AWS_BUCKET_NAME, file)
    except Exception as e:
        print(e)
    