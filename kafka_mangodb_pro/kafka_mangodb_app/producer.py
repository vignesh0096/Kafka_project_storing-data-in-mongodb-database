import random
from kafka import KafkaProducer
from json import dumps
from .models import collection
from time import sleep


def kafka_producer():
    producer = KafkaProducer(bootstrap_servers=['localhost:9092'],value_serializer = lambda x:dumps(x).encode('utf-8'))
    url = "http://65.1.111.158:5000/produce?data=%28%28pass"
    topic = "mangodb_data"

    for i in range(0, 100):
        data = {
                "latitude": random.uniform(-90, 90),
                "longitude": random.uniform(-180, 180),
                "id": ("RID" + str(random.choice(range(1,100))))
                }
        producer.send(topic, value=data)
        collection.insert_one(data)
        sleep(0.5)

