import heapq
from collections import deque
import time


class Scheduler:

    def __init__(self):
        self.ready = deque()
        self.sleeping = []
        self.sequence = 0

    def run(self):
        while self.ready or self.sleeping:
            # Do something if empty
            if not self.ready:
                deadline, func = self.sleeping.pop(0)
                delta = deadline - time.time()
                if delta < 0:
                    delta = 0
                time.sleep(deadline)
            func = self.ready.popleft()
            func()

    def call_soon(self, func):
        self.ready.append(func)

    def call_later(self, delay, func):
        deadline = time.time() + delay
       # heapq.heqppush(self.sleeping.append((deadline, func))
       # self.sleeping.sort()

sched = Scheduler()


def countdown(n):
    if n > 0:
        print('Down', n)
       # time.sleep(1)
        sched.call_soon(2, lambda: countdown(n - 1))


def countup(stop, x = 0):
    if x < stop:
        print('Up', x)
     #   time.sleep(1)
        sched.call_soon(1, lambda: countup(stop, x+1))


sched.call_soon(lambda: countdown(5))
sched.call_soon(lambda: countup(5))
sched.run()
