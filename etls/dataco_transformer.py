from pyspark.sql import SparkSession, DataFrame
# from pyspark.errors import PySparkException
from pyspark.sql.functions import col, year, month, dayofmonth, quarter, weekofyear, dayofweek, date_format, when, sha2, concat_ws, row_number
from pyspark.sql.window import Window

def stg_date(spark: SparkSession) -> DataFrame:
    try:
        date_range = spark.range(0, 365*3).selectExpr("date_add('2015-01-01', cast(id AS INT)) as full_date")
    
        dim_date = date_range.withColumn("date_key", date_format(col("full_date"), "yyyyMMdd").cast("int")) \
            .withColumn("day", dayofmonth(col("full_date"))) \
            .withColumn("month", month(col("full_date"))) \
            .withColumn("year", year(col("full_date"))) \
            .withColumn("quarter", quarter(col("full_date"))) \
            .withColumn("week_of_year", weekofyear(col("full_date"))) \
            .withColumn("day_of_week", dayofweek(col("full_date"))) \
            .withColumn("day_name", date_format(col("full_date"), "EEEE")) \
            .withColumn("is_weekend", when(dayofweek(col("full_date")).isin([1, 7]), True).otherwise(False)) 
    except Exception as e:
        print(f"Pyspark error while create dim_date {e}")
        
    return dim_date

def transform_data(df:DataFrame) -> DataFrame:
    df = df.withColumn("territory_id", sha2(concat_ws("_", col("Market"), col("Order Region"), col("Order Country"),col("Order State"), col("Order City")), 256))
    return df

def stg_territory(df:DataFrame) -> DataFrame:
    stg_territory = df.selectExpr(
        "territory_id",
        "Market as market",
        "`Order Region` as region",
        "`Order Country` as country",
        "`Order State` as state",
        "`Order City` as city"
    ).dropDuplicates()
    
    window_spec = Window.orderBy("territory_id")
    stg_territory = stg_territory.withColumn("territory_key", row_number().over(window_spec))
    return stg_territory

def stg_product(df:DataFrame) -> DataFrame:
    stg_product = df.selectExpr(
    "`Product Card Id` as product_id",
    "`Product Name` as product_name",
    "`Category Name` as category_name").dropDuplicates().dropna()
    
    window_spec = Window.orderBy("product_id")
    
    stg_product = stg_product.withColumn("product_key", row_number().over(window_spec))
    return stg_product

def stg_customer(df: DataFrame) -> DataFrame:
    stg_customer = df.selectExpr(
        "`Customer Id` as customer_id",
        "concat_ws(' ', `Customer Fname`, `Customer Lname`) as customer_name", 
        "`Customer Country` as customer_country",
        "`Customer State` as customer_state",
        "`Customer City` as customer_city",
        "`Customer Street` as customer_street"  
        ).dropDuplicates()
    return stg_customer