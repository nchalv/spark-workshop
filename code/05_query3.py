from pyspark.sql import SparkSession
from pyspark.sql.window import Window
from pyspark.sql.functions import col, to_date, count, desc, col, year, asc, expr, regexp_replace, length, dense_rank
from pyspark.sql.types import IntegerType, DoubleType

spark = SparkSession.builder \
    .appName("CrimeDataAnalytics - Query 3 - DF - parquet") \
    .getOrCreate()

# Read crime data files
directory_path = "hdfs://controller:54310/user/ubuntu/data/la_crime_data/parquet"
df = spark.read.parquet(directory_path)

# Read inverse geocoding data file
directory_path = "hdfs://controller:54310/user/ubuntu/data/la_crime_data/revgecoding.csv"
latlongzip = spark.read.option("header", "true").csv(directory_path)
latlongzip = latlongzip.withColumn("ZIPCode", expr("substr(ZIPCode, 1, 5)"))
# Read inverse income data file
directory_path = "hdfs://controller:54310/user/ubuntu/data/la_crime_data/LA_income_2015.csv"
# Process and convert columns into appropriate types
income = spark.read.option("header", "true").csv(directory_path) \
            .select(col("Zip Code").alias("ZIPCode"), "Estimated Median Income") \
            .withColumn("EMI", expr("substr(`Estimated Median Income`, 2, length(`Estimated Median Income`)-1)")) \
            .withColumn("EMI", regexp_replace(col("EMI"), ",", "")) \
            .withColumn("EMI", col("EMI").cast(IntegerType())) \
            .select("ZIPCode", "EMI")
# Read descent description file
directory_path = "hdfs://controller:54310/user/ubuntu/data/la_crime_data/descent-desc.csv"
descent_desc = spark.read.option("header", "true").csv(directory_path)

#   Vict Descent               Vict Descent Full
#0             A                     Other Asian
#1             B                           Black
#2             C                         Chinese
#3             D                       Cambodian
#4             F                        Filipino
#5             G                       Guamanian
#6             H          Hispanic/Latin/Mexican
#7             I  American Indian/Alaskan Native
#8             J                        Japanese
#9             K                          Korean
#10            L                         Laotian
#11            O                           Other
#12            P                Pacific Islander
#13            S                          Samoan
#14            U                        Hawaiian
#15            V                      Vietnamese
#16            W                           White
#17            X                         Unknown
#18            Z                     AsianIndian

df_15 = df.filter((year("DATE OCC") == 2015) & (col("Vict Descent")!="null")) \
          .select("Vict Descent", "LAT", "LON")
query = df_15.join(latlongzip, ["LAT", "LON"], "inner") \
             .join(income.hint("broadcast"), "ZIPCode", "inner") \
             .join(descent_desc.hint("broadcast"), "Vict Descent", "inner") \
             .select("ZIPCode", "Vict Descent Full", "EMI")
windowSpec = Window.orderBy(col("EMI").desc())
query_top3 = query.withColumn("EMI_rank", dense_rank().over(windowSpec)) \
                  .filter(col("EMI_rank") <= 3)
query_top3.groupBy("Vict Descent Full") \
          .agg(count("*").alias("count")) \
          .orderBy(desc("count")) \
          .show(100, False)
windowSpec = Window.orderBy(col("EMI").asc())
query_bot3 = query.withColumn("EMI_rank", dense_rank().over(windowSpec)) \
                  .filter(col("EMI_rank") <= 3)
query_bot3.groupBy("Vict Descent Full") \
          .agg(count("*").alias("count")) \
          .orderBy(desc("count")) \
          .show(100, False)
