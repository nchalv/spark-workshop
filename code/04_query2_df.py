from pyspark.sql import SparkSession
from pyspark.sql.functions import col, to_date, udf, count, desc, col
from pyspark.sql.types import IntegerType, DoubleType, StringType

def time_to_part_of_day(x):
    hour = int(x[:2])
    if  (5<=hour) and (hour<=11):
        return 'Morning'
    elif  (12<=hour) and (hour<=16):
        return 'Afternoon'
    elif  (17<=hour) and (hour<=20):
        return 'Evening'
    else :
        return 'Night'

time_to_part_of_day_udf = udf(time_to_part_of_day, StringType())

spark = SparkSession.builder \
    .appName("CCrimeDataAnalytics - Query 2 - DF - parquet") \
    .getOrCreate()

# Read the files
directory_path = "hdfs://controller:54310/user/ubuntu/data/la_crime_data/parquet"
# Read the files
df = spark.read.parquet(directory_path)

part_of_day = df.select('TIME OCC') \
    .filter(col('Premis Desc')=='STREET') \
    .withColumn("PoD", time_to_part_of_day_udf(col("TIME OCC"))) \
    .groupBy('PoD') \
    .agg(count('*') \
         .alias('count')) \
    .orderBy(desc('count'))
part_of_day.show()
