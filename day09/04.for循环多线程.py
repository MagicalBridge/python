import threading
import time


def run(n):
    print('task', n)
    time.sleep(2)


for i in range(50):
    t = threading.Thread(target=run, args=('t-%s' % i,))
    t.start()
