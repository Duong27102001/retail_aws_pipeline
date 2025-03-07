from pyspark.sql import SparkSession

def create_spark_session(aws_access_key: str, aws_secret_key: str) -> SparkSession:
    
    try:
        spark = SparkSession.builder \
            .appName("Airflow-Spark-Test") \
            .master("spark://spark-master:7077") \
            .config("spark.hadoop.fs.s3a.access.key", aws_access_key) \
            .config("spark.hadoop.fs.s3a.secret.key", aws_secret_key) \
            .config("spark.hadoop.fs.s3a.endpoint", "s3.amazonaws.com") \
            .config("spark.jars", "/opt/bitnami/spark/jars/hadoop-aws-3.3.4.jar,"
                              "/opt/bitnami/spark/jars/aws-java-sdk-bundle-1.12.262.jar,"
                              "/opt/bitnami/spark/jars/jets3t-0.9.7.jar") \
        .getOrCreate()
        
        print("Spark session created successfully!")
        return spark

    except Exception as e:
        print(f"Failed to create spark session: {e}")
        return None
