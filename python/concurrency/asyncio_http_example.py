import asyncio
import time
import aiohttp


SYMBOLS = ("USD", "EUR", "PLN", "NOK", "CZK")
BASES = ("USD", "EUR", "PLN", "NOK", "CZK")


async def get_rates(session: aiohttp.ClientSession, base: str):
    async with session.get(f'https://api.vatcomply.com/rates?base={base}') as response:
        rates = (await response.json())['rates']
        rates[base] = 1.0
        return base, rates


async def present_result(base: str, rates: dict):
    print(f'Base: {base}')
    for symbol in SYMBOLS:
        print(f'1 {base} = {rates[symbol]} {symbol}')
    print()


async def main():
    async with aiohttp.ClientSession() as session:
        tasks = [get_rates(session, base) for base in BASES]
        results = await asyncio.gather(*tasks)
        for base, rates in results:
            await present_result(base, rates)


if __name__ == '__main__':
    start = time.time()
    asyncio.run(main())
    print(f'Took {time.time() - start:.2f} seconds')
