import json
from time import sleep
from kafka import KafkaConsumer


def kafka_consumer():
    topic = "mangodb_data"
    consumer = KafkaConsumer(topic,bootstrap_servers=['localhost:9092'],auto_offset_reset='latest',
                             value_deserializer=lambda y: json.loads(y.decode('utf-8')))
    for message in consumer:
        print(message.value)
        sleep(0.5)

