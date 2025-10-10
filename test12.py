import asyncio
import time


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
    asyncio.create_task(one())
    asyncio.create_task(two())
    await asyncio.create_task(three())

if __name__=="__main__":
    start = time.time()
    asyncio.run(main())
    print(time.time() - start)