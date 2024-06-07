import requests
import json
from kafka import KafkaProducer
import time

# Kafka Producer
producer = KafkaProducer(bootstrap_servers='kafka:9092',
                         value_serializer=lambda v: json.dumps(v).encode('utf-8'))

url = "https://opensky-network.org/api/states/all"

while True:
    response = requests.get(url)
    data = response.json()
    producer.send('flight-data', value=data)
    time.sleep(10)  # Fetch data every 10 seconds
