from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col, window
from pyspark.sql.types import StructType, FloatType, LongType


spark = SparkSession.builder \
.appName("KafkaSparkStreaming") \
.getOrCreate()


schema = StructType() \
.add("transaction_id", LongType()) \
.add("amount", FloatType()) \
.add("timestamp", FloatType())


kafka_df = spark.readStream \
.format("kafka") \
.option("kafka.bootstrap.servers", "kafka:9092") \
.option("subscribe", "transactions") \
.load()


parsed_df = kafka_df.select(
from_json(col("value").cast("string"), schema).alias("data")
).select("data.*")


agg_df = parsed_df \
.withWatermark("timestamp", "10 minutes") \
.groupBy(window(col("timestamp"), "1 minute")) \
.sum("amount")


query = agg_df.writeStream \
.format("jdbc") \
.option("url", "jdbc:postgresql://postgres:5432/realtime_db") \
.option("dbtable", "realtime_metrics") \
.option("user", "admin") \
.option("password", "admin") \
.option("checkpointLocation", "/tmp/checkpoints") \
.outputMode("complete") \
.start()


query.awaitTermination()