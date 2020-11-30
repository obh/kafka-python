import os
import sys

from kafka import KafkaConsumer
from json import loads
from multiprocessing.dummy import Pool
from logger import CustomLogger
import threading, logging, time


class StreamConsumer(threading.Thread):

    def __init__(self):
        super().__init__()
        self._topic = "test-events"
        #self._consumer = self._initialize_with_topic(self._topic)
        self._logger = CustomLogger().initlogger()

    def run(self):
        consumer = KafkaConsumer(
            self._topic,
            bootstrap_servers="127.0.0.1:9092",
            value_deserializer=lambda x: loads(x.decode('utf-8')),
            key_deserializer=lambda x: x.decode('utf-8'),
            auto_offset_reset="earliest",
            group_id="reconsvcmongo",
            max_poll_records=2
        )
        self._logger.info("Initialized Kafka Consumer for topic :: " + self._topic)
        for message in consumer:
            print("in _consume")
            print(message)
            consumer.commit()

        consumer.close()



