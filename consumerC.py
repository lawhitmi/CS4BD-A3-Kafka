from kafka import KafkaConsumer
consumer = KafkaConsumer('test')

for msg in consumer:
    #print(msg[6].decode('utf-8'))
    message = msg[6].decode('utf-8')
    print('Producer '+message[0]+': '+message[3:])

