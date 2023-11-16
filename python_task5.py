from time import sleep
from random import randint
from threading import Thread
from queue import Queue

producer_num=int(input("Enter Number of consumer : "))
consumer_num=int(input("Enter Number of producer : "))

def producer(queue):
    print('Producer: Running')
    for i in range(producer_num):
        value = i+1
        sleep(value)
        item = (i, value)
        queue.put(item)
        print("producer added {}".format(item))
    queue.put(None)
    print('Producer: Done')
def consumer(queue):
    print('Consumer: Running')
    for j in range(consumer_num):
        item = queue.get()
        if item is None:
            break
        sleep(0.2)
        print("consumer got {}".format(item))
    print('Consumer: Done')

queue = Queue()
producer = Thread(target=producer, args=(queue,))
producer.start()
consumer = Thread(target=consumer, args=(queue,))
consumer.start()
producer.join()
consumer.join()