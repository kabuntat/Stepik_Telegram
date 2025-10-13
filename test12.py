import asyncio
import time

import aiohttp
import requests as requests


async def blocking():
    resp = requests.get("https://ya.ru")
    print(resp.status_code)

async def async_http():
    async with aiohttp.ClientSession() as session:
        async with session.get("https://ya.ru") as resp:
            print(resp.status)
async def one():
    print("Start 1")
    await asyncio.sleep(1)
    print("Stop 1")

async def two():
    print("Start 2")
    await asyncio.sleep(2)
    print("Stop 2")

async def three():
    print("Start 3")
    await asyncio.sleep(3)
    print("Stop 3")

async def main():
    await asyncio.gather(*(async_http() for i in range(5)))

if __name__=="__main__":
    start = time.time()
    asyncio.run(main())
    print(time.time() - start)

def test():
    pass