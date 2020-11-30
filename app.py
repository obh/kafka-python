from flask import Flask
from flask import g
import KafkaController
app = Flask(__name__)

def get_kafka_controller():
    if 'kafka' not in g:
        g.kafka = KafkaController.KafkaController()

    return g.kafka


@app.route('/')
def hello():
    return "Hello World!"

@app.route('/produce')
def produce():
    kafka = get_kafka_controller()
    out = kafka.sendEvents()
    return {"eventsEmitted" : out}

@app.route('/initconsumer')
def initconsumer():
    kafka = get_kafka_controller()
    return "kafka consumer initialized"

@app.teardown_appcontext
def teardown_db(exception):
    kafka = g.pop('kafka', None)
    if kafka is not None:
        kafka.close()

if __name__ == '__main__':
    app.run()