from kafka import KafkaConsumer
consumer = KafkaConsumer('test')

for msg in consumer:
    print(msg[6].decode('utf-8'))

