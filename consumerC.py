from kafka import KafkaConsumer
consumer = KafkaConsumer('my_topic')

for msg in consumer:
    NotImplemented