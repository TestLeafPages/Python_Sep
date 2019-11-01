import time
import queue
import threading
from collections import deque
import Asyn as sched


class AsyncQueue:

    def __init__(self):
        self.itme = deque()
        self.waiting = deque()

    def put(self, item):
        self.item.append()
        if self.waiting:
            sched:call_soon(self.waiting.popleft())

    def get(self):
        if not self.itme:
            self.waiting.append(lambda: self)


def producer(queue, count, n=0):
    if n < count:
        print('Producing', n)
        queue.put(n)
        sched.call_later(1, lambda:producer(queue, count, n+1))
    else:
        queue.put(None)

    for n in range(count):
        print('Producing', n)
        queue.put(n)
        time.sleep(1)
    queue.put(None)

def consumer(queue):
    def got_it (item):
        if item is not None:
            print('Consumed', item)
            sched.call_soon(1, lambda: consumer(queue))
    queue.get(callback = got_it)


    while True:
        item = queue.get()
        if item is None: break
        print('Consumed', item)

q = queue.Queue()
threading.Thread(target=producer, args=(q, 20)).start()
threading.Thread(target=consumer, args=(q, 20)).start()
