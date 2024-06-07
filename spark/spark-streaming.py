from pyspark.sql import SparkSession
from pyspark.sql.functions import explode, from_json, col
from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DoubleType

# Initialize Spark Session
spark = SparkSession.builder.appName("FlightDataProcessing").getOrCreate()
spark.sparkContext.setLogLevel("WARN")

# Kafka Configuration
kafka_bootstrap_servers = "kafka:9092"
kafka_topic = "flight-data"

# Schema for the incoming data
schema = StructType([
    StructField("time", StringType(), True),
    StructField("states", ArrayType(StructType([
        StructField("icao24", StringType(), True),
        StructField("callsign", StringType(), True),
        StructField("origin_country", StringType(), True),
        StructField("time_position", DoubleType(), True),
        StructField("last_contact", DoubleType(), True),
        StructField("longitude", DoubleType(), True),
        StructField("latitude", DoubleType(), True),
        StructField("baro_altitude", DoubleType(), True),
        StructField("on_ground", StringType(), True),
        StructField("velocity", DoubleType(), True),
        StructField("true_track", DoubleType(), True),
        StructField("vertical_rate", DoubleType(), True),
        StructField("sensors", StringType(), True),
        StructField("geo_altitude", DoubleType(), True),
        StructField("squawk", StringType(), True),
        StructField("spi", StringType(), True),
        StructField("position_source", StringType(), True),
    ])), True)
])

# Read data from Kafka
df = spark.readStream.format("kafka") \
    .option("kafka.bootstrap.servers", kafka_bootstrap_servers) \
    .option("subscribe", kafka_topic) \
    .load()

# Convert value to string
df = df.selectExpr("CAST(value AS STRING)")

# Parse JSON and explode the array
df = df.select(col("value").cast("string").alias("json")).select(from_json(col("json"), schema).alias("data")).select("data.*")
df = df.withColumn("state", explode(col("states"))).select("time", "state.*")

# Write to InfluxDB
df.writeStream \
    .outputMode("append") \
    .format("org.apache.spark.sql.influxdb.InfluxDBSinkProvider") \
    .option("url", "http://influxdb:8086") \
    .option("db", "flight_data") \
    .option("measurement", "flights") \
    .start() \
    .awaitTermination()
