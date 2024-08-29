from pyspark.sql import SparkSession


spark = SparkSession.builder \
    .appName("CrimeDataAnalytics - Query 1 - SQL - parquet") \
    .getOrCreate()

directory_path = "hdfs://controller:54310/user/ubuntu/data/la_crime_data/parquet"

# Read the files
df = spark.read.parquet(directory_path)

df.createOrReplaceTempView("crime_data")
q1_query = """
    SELECT * FROM (
        WITH aggregated_data AS (
            SELECT
                YEAR(`DATE OCC`) AS year,
                MONTH(`DATE OCC`) AS month,
                COUNT(*) AS count
            FROM
                crime_data
            GROUP BY
                year, month
            ORDER BY
                year, month
        )
        SELECT *, ROW_NUMBER() OVER (PARTITION BY year ORDER BY count DESC) AS row_num
        FROM
            aggregated_data)
    WHERE row_num <=3 
"""
q1 = spark.sql(q1_query)
q1.show(42)