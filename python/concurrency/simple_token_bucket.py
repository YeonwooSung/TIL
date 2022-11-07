from threading import Lock, Thread
import time
from queue import Queue, Empty

import requests


SYMBOLS = ("USD", "EUR", "PLN", "NOK", "CZK")
BASES = ("USD", "EUR", "PLN", "NOK", "CZK")

THREAD_POOL_SIZE = 4
THROTTLE_THRESHOLD = 10


class Throttle:
    def __init__(self, rate):
        self._consume_lock = Lock()
        self.rate = rate
        self.tokens = 0
        self.last = None
    
    def consume(self, amount):
        with self._consume_lock:
            now = time.time()

            # 시간 측정은 첫 번째 토큰에 대해 초기화함으로써 초기 부하를 줄인다.
            if self.last is None:
                self.last = now
            
            elapsed = now - self.last

            # 초과된 시간이 새로운 토큰을 추가할 만큼 충분히 긴지 확인한다.
            if elapsed * self.rate > 1:
                self.tokens = elapsed * self.rate
                self.last = now
            
            # 버킷을 초과해서 채우지 않는다.
            self.tokens = min(self.rate, self.tokens)

            # 마지막으로, 가능한 경우 토큰을 보낸다.
            if self.tokens >= amount:
                self.tokens -= amount
                return amount
            
            return 0


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

def worker(work_queue, result_queue, throttle):
    while not work_queue.empty():
        try:
            base = work_queue.get_nowait()
        except Empty:
            break
        
        while not throttle.consume(1):
            time.sleep(0.1)
        
        try:
            result = fetch_rates(base)
        except Exception as err:
            result_queue.put(err)
        else:
            result_queue.put(result)
        finally:
            work_queue.task_done()


def main():
    work_queue = Queue()
    results_queue = Queue()

    throttle = Throttle(THROTTLE_THRESHOLD)

    for base in BASES:
        work_queue.put(base)
    
    threads = [
        Thread(target=worker, args=(work_queue, results_queue, throttle))
        for _ in range(THREAD_POOL_SIZE)
    ]

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    while not results_queue.empty():
        result = results_queue.get()
        if isinstance(result, Exception):
            raise result
        present_result(*result)


if __name__ == '__main__':
    start = time.time()
    main()
    elapsed = time.time() - start
    print(f'Elapsed time: {elapsed:.2f} seconds')
