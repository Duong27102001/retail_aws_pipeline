from pyspark.sql import SparkSession, DataFrame
# from pyspark.errors import PySparkException

def extract_data_from_S3(path: str, spark: SparkSession) -> DataFrame:
    try:
        df = spark.read.csv(path, header= True, inferSchema= True)
        df.cache()
        df.count() 
    except Exception as e:
        print(f"Pyspark error while reading S3: {e}")
    return df