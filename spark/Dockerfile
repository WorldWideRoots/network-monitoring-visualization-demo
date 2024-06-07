# Dockerfile for Spark Streaming
FROM bitnami/spark:latest

COPY spark-streaming.py /opt/spark-apps/

CMD ["/opt/bitnami/scripts/spark/run.sh", "spark-submit", "/opt/spark-apps/spark-streaming.py"]
