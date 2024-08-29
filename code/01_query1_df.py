from pyspark.sql import SparkSession
from pyspark.sql.functions import col, to_date, unix_timestamp, from_unixtime
from pyspark.sql.window import Window
from pyspark.sql.functions import year, month, dayofmonth, count, max, row_number, desc

spark = SparkSession.builder \
    .appName("CrimeDataAnalytics - Query 1 - DF - parquet") \
    .getOrCreate()
directory_path = "hdfs://controller:54310/user/ubuntu/data/la_crime_data/parquet"

# Read the files
df = spark.read.parquet(directory_path)
windowSpec  = Window.partitionBy("year").orderBy(desc("count"))
q1 = df.groupBy(year("DATE OCC").alias("year"), month("DATE OCC") \
    .alias("month")).agg(count("*").alias("count")).orderBy(["year", "month"]) \
    .withColumn("row_number", row_number().over(windowSpec)).where(col("row_number") <= 3)
q1.show(42)
