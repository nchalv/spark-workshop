from pyspark.sql import SparkSession
from pyspark.sql.functions import col, to_date
from pyspark.sql.types import IntegerType, DoubleType

spark = SparkSession.builder \
    .appName("csv to parquet - optional") \
    .getOrCreate()
#Set the path to the data source
path = "hdfs://controller:54310/user/ubuntu/data/la_crime_data/CrimeData_10-19.csv"
df = spark.read.option("header", "true").csv(path)
date_format = "MM/dd/yyyy hh:mm:ss a"
df = df.withColumn("Date Rptd", to_date("Date Rptd", date_format)) \
    .withColumn("DATE OCC", to_date("DATE OCC", date_format)) \
    .withColumn("LAT", col("LAT").cast(DoubleType())) \
    .withColumn("LON", col("LON").cast(DoubleType())) \
    .withColumn("Vict Age", col("Vict Age").cast(IntegerType()))
# Write DataFrame to Parquet - in contrast to csv, it can also store data types
df.write \
    .parquet("hdfs://controller:54310/user/ubuntu/data/la_crime_data/parquet")