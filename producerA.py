from kafka import KafkaProducer
import time

producer = KafkaProducer(bootstrap_servers='localhost:9092')

starttime = time.time()
i = 0
while True:
    i += 2
    print(i)
    producer.send('test',str.encode('Producer A: '+str(i),'utf-8'))
    time.sleep(1.0 - ((time.time()-starttime)%1))