import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from etls.dataco_extract import extract_data_from_S3
from etls.dataco_transformer import stg_customer, stg_product, stg_territory, stg_date, transform_data
from etls.dataco_load import write_to_s3
from utils.constants import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, S3_BUCKET_RAW, S3_BUCKET_PROCESSED
from utils.spark_session import create_spark_session

def staging_pipeline():
    
    spark = create_spark_session(AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY)
    dataCo = extract_data_from_S3(S3_BUCKET_RAW + "DataCoSupplyChainDataset.csv", spark)
    dataCo = transform_data(dataCo)
    customer = stg_customer(dataCo)
    write_to_s3(customer, S3_BUCKET_PROCESSED + "stg_customer")
    
    produt = stg_product(dataCo)
    write_to_s3(produt, S3_BUCKET_PROCESSED + "stg_product")
    
    territory = stg_territory(dataCo)
    write_to_s3(territory, S3_BUCKET_PROCESSED + "stg_territory")
    
    date = stg_date(spark)
    write_to_s3(date, S3_BUCKET_PROCESSED + "stg_date")
    