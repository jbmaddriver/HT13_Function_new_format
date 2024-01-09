import time
import multiprocessing
import multiprocess
import random


class timer():
    def __init__(self, message):
        self.message = message

    def __enter__(self):
        self.start = time.time()
        return None

    def __exit__(self, type, value, traceback):
        elapsed_time = (time.time() - self.start)
        print(self.message.format(elapsed_time))


lst = []
DATA_SIZE = 1000000
workers = 2


def fill_data(n):
    while n > 0:
        n -= 1
        lst.append(random.randint(1, 100))


# with timer('fill_data() Executed in: {}s'):
    # fill_data(DATA_SIZE)

if __name__ == '__main__':
    # The following line is specific to Windows
    multiprocessing.freeze_support()

    # with timer('Elapsed: {}s'):
    #     with ThreadPool(workers) as pool:
    #         input_data = [DATA_SIZE // workers for _ in range(workers)]
    #         result = pool.map(fill_data, input_data)
    #
    # print(len(lst), lst[:50])

    with timer('Elapsed: {}s'):
        with multiprocess.Pool(workers) as pool:
            input_data = [DATA_SIZE // workers for _ in range(workers)]
            pool.map(fill_data, input_data)

    print(len(lst), lst[:50])