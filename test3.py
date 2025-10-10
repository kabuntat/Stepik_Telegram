import asyncio
import time


async def print1():
    print(1)

async def print2():
    await asyncio.sleep(5)
    print(2)

async def print3():
    print(3)

async def main():
    async with asyncio.TaskGroup() as tg:
        for i in range(1,16):
            tg.create_task(print1(i))

asyncio.run(main())