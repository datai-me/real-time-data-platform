from pyspark.sql import SparkSession
from pyspark.sql.functions import col, lag, abs
from pyspark.sql.window import Window
import sqlite3

spark = SparkSession.builder \
    .appName("ExchangeRateAnomalyDetection") \
    .master("local[*]") \
    .getOrCreate()

df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "exchange_rates") \
    .load()

rates = df.selectExpr("CAST(value AS STRING)") \
    .selectExpr(
        "json_extract(value, '$.rate') as rate",
        "json_extract(value, '$.timestamp') as timestamp"
    )

window = Window.orderBy("timestamp")

alerts = rates.withColumn(
    "prev_rate", lag("rate").over(window)
).withColumn(
    "variation",
    abs((col("rate") - col("prev_rate")) / col("prev_rate"))
).filter(col("variation") > 0.03)

def write_alerts(batch_df, batch_id):
    conn = sqlite3.connect("realtime.db")
    batch_df.select("timestamp", "rate", "variation") \
        .toPandas() \
        .to_sql("exchange_rate_alerts", conn, if_exists="append", index=False)
    conn.close()

query = alerts.writeStream.foreachBatch(write_alerts).start()
query.awaitTermination()
