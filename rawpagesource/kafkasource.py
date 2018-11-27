from kafka import KafkaConsumer
from rawpagedata import RawPageData
from rawpagesource.rawpagesource import RawPageSource

import datetime
import json

class KafkaSource(RawPageSource):

    '''
    Provides continouus stream of RawPageData objects
    from Kafka
    '''

    def _parseRawPageData(bytes):
        base = json.loads(bytes.decode('utf-8'))
        base['datetime'] = datetime.datetime.fromisoformat(base['datetime'])
        return RawPageData(**base)

    def __init__(self, config):

        
        '''
        Setup an instance of KafkaSource
        :param **config: Configuration passed to KafkaConsumer
        '''
        config["key_deserializer"] = lambda k: k.decode('utf-8')
        config["value_deserializer"] = KafkaSource._parseRawPageData
        topic = config.pop("topic")
        self.consumer = KafkaConsumer(topic, **config)

    def getPage(self):
        msg = next(self.consumer)
        assert isinstance(msg.value, RawPageData)
        return msg.value
