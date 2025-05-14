from pyspark.sql import SparkSession
from pyspark.sql.functions import col, max, mean, min, lag, lead, row_number, lit, broadcast
from pyspark.sql.window import Window

# Initialize SparkSession
spark = SparkSession.builder \
    .appName("PySpark Example") \
    .getOrCreate()

# Sample DataFrame
data = [
    (1, "A", 100),
    (2, "B", 200),
    (3, "A", 300),
    (4, "B", 400),
    (5, "A", 500)
]
columns = ["id", "category", "value"]
df = spark.createDataFrame(data, columns)

# Aggregations: max, mean, min
agg_df = df.groupBy("category").agg(
    max("value").alias("max_value"),
    mean("value").alias("mean_value"),
    min("value").alias("min_value")
)

# Window Functions: lag, lead, row_number
window_spec = Window.partitionBy("category").orderBy("id")
df_with_window = df.withColumn("lag_value", lag("value").over(window_spec)) \
    .withColumn("lead_value", lead("value").over(window_spec)) \
    .withColumn("row_number", row_number().over(window_spec))

# Limit and Distinct
limited_df = df.limit(3)
distinct_df = df.select("category").distinct()

# Join and Broadcast Join
data2 = [
    ("A", "Group1"),
    ("B", "Group2")
]
columns2 = ["category", "group"]
df2 = spark.createDataFrame(data2, columns2)

# Regular Join
joined_df = df.join(df2, on="category", how="inner")

# Broadcast Join
broadcast_joined_df = df.join(broadcast(df2), on="category", how="inner")

# Repartition and Coalesce
repartitioned_df = df.repartition(4, "category")
coalesced_df = repartitioned_df.coalesce(2)

# WithColumn Example
df_with_new_column = df.withColumn("new_value", col("value") * 2)

# Show Results
print("Aggregations:")
agg_df.show()

print("Window Functions:")
df_with_window.show()

print("Limited Rows:")
limited_df.show()

print("Distinct Rows:")
distinct_df.show()

print("Joined DataFrame:")
joined_df.show()

print("Broadcast Joined DataFrame:")
broadcast_joined_df.show()

print("Repartitioned DataFrame:")
print(f"Number of partitions: {repartitioned_df.rdd.getNumPartitions()}")

print("Coalesced DataFrame:")
print(f"Number of partitions: {coalesced_df.rdd.getNumPartitions()}")

print("With New Column:")
df_with_new_column.show()

# Stop SparkSession
spark.stop()