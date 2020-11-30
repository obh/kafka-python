from kafka_producer import StreamProducer
from kafka_consumer import StreamConsumer
from logger import CustomLogger

class KafkaController:
    def __init__(self):
        self._producer = StreamProducer()
        self._producer.initialize()
        self._consumer = StreamConsumer()
        #starts consumer thread
        self._consumer.start()
        self._logger = CustomLogger().initlogger()

    def sendEvents(self):
        eventList = [
            "this is first message",
            "this is second message",
            "this is third message",
            "this is fourth message",
        ]
        #self._producer.publish(eventList[0:1])
        self._producer.publish(eventList[0:2])
        self._producer.publish(eventList[2:])
        return eventList


    def close(self):
        self._logger.info("Closing kafaConsumer...")
