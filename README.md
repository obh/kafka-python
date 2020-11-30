# kafka-python

Start server - `python3 app.py`

Produce events
http://127.0.0.1:5000/produce

See logs to get all the consumed events. 

To view idempotency, close server and edit file KafkaController.py.

Comment out lines 22 and 23, and uncomment 21. Save file and restart server. 

Again hit `http://127.0.0.1:5000/produce`, and the consumer should only consume that one event


