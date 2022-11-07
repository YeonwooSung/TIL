import time
from queue import Queue
from threading import Thread

import requests

SYMBOLS = ("USD", "EUR", "PLN", "NOK", "CZK")
BASES = ("USD", "EUR", "PLN", "NOK", "CZK")

THREAD_POOL_SIZE = 4

def fetch_rates(base):
    response = requests.get(
        f'https://api.vatcomply.com/rates?base={base}'
    )
    response.raise_for_status()
    rates = response.json()['rates']
    rates[base] = 1.0
    return base, rates

def present_result(base, rates):
    print(f'Base: {base}')
    for symbol in SYMBOLS:
        print(f'1 {base} = {rates[symbol]} {symbol}')
    print()

def worker(work_queue, result_queue):
    while not work_queue.empty():
        try:
            base = work_queue.get_nowait()
        except Exception as err:
            result_queue.put(err)
        else:
            result_queue.put(fetch_rates(base))
        finally:
            work_queue.task_done()

def main():
    work_queue = Queue()
    result_queue = Queue()

    for base in BASES:
        work_queue.put(base)

    threads = [
        Thread(target=worker, args=(work_queue, result_queue))
        for _ in range(THREAD_POOL_SIZE)
    ]

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    while not result_queue.empty():
        result = result_queue.get()
        if isinstance(result, Exception):
            raise result
        present_result(*result)


if __name__ == '__main__':
    start = time.time()
    main()
    elapsed = time.time() - start
    print(f'Elapsed time: {elapsed:.2f} seconds')
