import asyncio
import random


async def print_number(number):
    delay = random.random() * 5
    await asyncio.sleep(delay)
    print(f'Printed {number} after {delay:.2f} seconds')


if __name__ == '__main__':
    loop = asyncio.get_event_loop()

    loop.run_until_complete(
        asyncio.gather(*[print_number(i) for i in range(10)])
    )
