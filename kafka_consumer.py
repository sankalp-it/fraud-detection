from kafka import KafkaConsumer, KafkaProducer
import requests
import json

consumer = KafkaConsumer(
    'transactions',
    bootstrap_servers='localhost:9092',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda x: json.dumps(x).encode('utf-8')
)

for message in consumer:
    transaction_data = message.value
    response = requests.post("http://model-service:8000/predict", json=transaction_data)
    prediction = response.json()

    result = {
        "transaction_id": transaction_data.get("transaction_id"),
        "is_fraud": prediction["prediction"]
    }

    producer.send('fraud_results', value=result)
