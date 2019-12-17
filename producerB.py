from kafka import KafkaProducer
import time

producer = KafkaProducer(bootstrap_servers='localhost:9092')

starttime = time.time()
i = -1
while True:
    i += 2
    producer.send('test',i)
    time.sleep(2.0 - ((time.time()-starttime)%2))