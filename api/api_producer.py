import requests
import json
import time
from kafka import KafkaProducer

producer = KafkaProducer(
    bootstrap_servers="kafka:9092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

API_URL = "https://api.exchangerate.host/latest?base=EUR"
TOPIC = "exchange_rates"

while True:
    response = requests.get(API_URL).json()

    payload = {
        "base": response["base"],
        "rates": response["rates"],
        "timestamp": time.time()
    }

    producer.send(TOPIC, payload)
    print("Données envoyées à Kafka")

    time.sleep(3600)  # toutes les heures
