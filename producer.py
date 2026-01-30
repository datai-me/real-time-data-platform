import requests
import json
import time
from kafka import KafkaProducer

KAFKA_BROKER = "localhost:9092"
TOPIC = "exchange_rates"
API_URL = "https://api.exchangerate.host/latest?base=EUR"

producer = KafkaProducer(
    bootstrap_servers=KAFKA_BROKER,
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

def fetch_and_send_exchange_rate():
    response = requests.get(API_URL, timeout=10)
    response.raise_for_status()
    data = response.json()

    payload = {
        "rate": data["rates"]["MGA"],
        "timestamp": time.time()
    }

    producer.send(TOPIC, payload)
    producer.flush()

    print("✔ Exchange rate sent:", payload)
