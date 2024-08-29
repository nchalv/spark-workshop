from pyspark.sql import SparkSession


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

spark = SparkSession.builder \
    .appName("CrimeDataAnalytics - Query 2 - RDD - parquet") \
    .getOrCreate()

directory_path = "hdfs://controller:54310/user/ubuntu/data/la_crime_data/parquet"
# Read the files
df = spark.read.parquet(directory_path)
# Conver DataFrame to RDD
rdd = df.rdd
part_of_day = rdd.map(lambda x: [x['TIME OCC'], x['Premis Desc']]) \
    .filter((lambda x: x[1] == 'STREET')) \
    .map(lambda x: [time_to_part_of_day(x[0])])
result = part_of_day.map(lambda x: (x[0], 1)) \
    .groupByKey().map(lambda x: (x[0], sum(x[1]))) \
    .sortBy(lambda x: x[1], ascending=False)
# Won't show in standard output
print(result.collect())