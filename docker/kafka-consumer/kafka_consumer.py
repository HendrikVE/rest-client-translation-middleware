#!/usr/bin/env python3
from time import sleep

from kafka import KafkaConsumer
from json import loads

consumer = KafkaConsumer(
    'numtest',
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='my-group',
    value_deserializer=lambda x: loads(x.decode('utf-8')))

while True:
    for message in consumer:
        print(message.value)

    sleep(1)
