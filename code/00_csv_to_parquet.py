from pyspark.sql import SparkSession
from pyspark.sql.functions import col, to_date
from pyspark.sql.types import IntegerType, DoubleType

spark = SparkSession.builder \
    .appName("csv to parquet - optional") \
    .getOrCreate()

path = "hdfs://controller:54310/home/ubuntu/data/la_crime_data/CrimeData_10-19.csv"
df = spark.read.csv(path, header=True, inferSchema=True)
date_format = "MM/dd/yyyy hh:mm:ss a"
df = df.withColumn("Date Rptd", to_date("Date Rptd", date_format)) \
    .withColumn("DATE OCC", to_date("DATE OCC", date_format)) \
    .withColumn("LAT", col("LAT").cast(DoubleType())) \
    .withColumn("LON", col("LON").cast(DoubleType())) \
    .withColumn("Vict Age", col("Vict Age").cast(IntegerType()))
# Write DataFrame to Parquet
df.write \
    .parquet("hdfs://controller:54310/home/ubuntu/data/la_crime_data/")