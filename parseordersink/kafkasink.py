from parseordersink.parseordersink import ParseOrderSink
from kafka import KafkaProducer

import json

class KafkaSink(ParseOrderSink):
    def __init__(self, config):
        config["key_serializer"] = str.encode
        config["value_serializer"] = lambda v: json.dumps(v).encode('utf-8')
        c_copy = dict(config)
        topic = c_copy.pop("topic")
        self.producer = KafkaProducer(**c_copy)
        self.topic = topic

    def send(self, parseOrder):
        key = parseOrder.url
        value = {
                'url': parseOrder.url,
                'datetime': parseOrder.datetime.isoformat(),
        }
        future = self.producer.send(self.topic, key=key, value=value)
        future.get(timeout=10)
