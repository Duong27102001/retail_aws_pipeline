from pyspark.sql import DataFrame
# from pyspark.errors import PySparkException

def write_to_s3(df: DataFrame, s3_path: str):
    try:
        df.write.mode("overwrite").parquet(s3_path)
        print(f"Data sucessfully uploaded to {s3_path}")
    except Exception as e:
        print(f"Error uploading data to S3: {e}")
    