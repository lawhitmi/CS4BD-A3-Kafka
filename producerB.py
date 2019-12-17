from kafka import KafkaProducer
import time

producer = KafkaProducer(bootstrap_servers='localhost:9092')

starttime = time.time()
i = -1
while True:
    i += 2
    print(i)
    producer.send('test',str.encode('Producer B: '+str(i),'utf-8'))
    time.sleep(2.0 - ((time.time()-starttime)%2))