import time
import threading
import os
import random
import string
import requests


class timer():
    def __init__(self, message):
        self.message = message

    def __enter__(self):
        self.start = time.time()
        return None

    def __exit__(self, type, value, traceback):
        elapsed_time = (time.time() - self.start)
        print(self.message.format(elapsed_time))


# 1. Потоки.
def fetch_pic(num_pic):
    url = 'https://picsum.photos/400/600'
    path = os.path.join(os.getcwd(), 'img')
    for _ in range(int(num_pic)):
        random_name = ''.join(random.choices(string.ascii_letters + string.digits, k=5))
        response = requests.get(url)
        if response.status_code == 200:
            with open(f'{path}/{random_name}.jpg', 'wb') as f:
                f.write(response.content)


def run_threads(func, data, workers):
    threads = [
        threading.Thread(target=func, args=(data / workers, ))
        for _ in range(workers)
    ]
    for t in threads:
        t.start()
    for t in threads:
        t.join()


with timer('fetch_pic() Executed in: {}s'):
    run_threads(fetch_pic, 10, 1)
