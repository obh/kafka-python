from kafka import KafkaProducer

import json
import random
import string
from json import dumps
from logger import CustomLogger


def singleton(cls):
    instances = {}

    def get_instance():
        if cls not in instances:
            instances[cls] = cls()
        return instances[cls]
    return get_instance


@singleton
class StreamProducer:

    def __init__(self):
        self._logger = CustomLogger().initlogger()
        self._producer = None
        self._topic = "test-events"

    def initialize(self):
        try:
            self._producer = KafkaProducer(
                bootstrap_servers="127.0.0.1:9092",
                key_serializer=str.encode,
                value_serializer=lambda x: json.dumps(x).encode('utf-8')
            )
            self._logger.info("Initialized Kafka Producer")
        except Exception as e:
            self._logger.error("Exception in StreamProducer initialize :: " + str(e))

    def publish(self, valueList):
        try:
            for value in valueList:
                key = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(5))
                self._producer.send(self._topic, key=key, value=value)
            self._producer.flush()
        except Exception as e:
            self._logger.error("Exception in StreamProducer publish :: " + str(e))