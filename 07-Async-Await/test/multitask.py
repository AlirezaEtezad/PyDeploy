import time
import random
import asyncio


async def get():
    print("get start")
    r = random.randint(0, 10)
    await asyncio.sleep(r)
    print (f"get ended in {r} sec")
    return r


def extract():
    print("extract start")
    r = random.randint(0, 10)
    time.sleep(r)
    print (f"extract ended in {r} sec")
    return r



async def download():
    print("download start")
    a = await get()
    b = extract()
    print (f"down ended in {a+b} sec")




async def printer():
    print("print start")
    r = random.randint(0, 10)
    await asyncio.sleep(r)
    print (f"print ended in {r} sec")



async def ai():
    print("ai start")
    r = random.randint(0, 10)
    await asyncio.sleep(r)
    print (f"ai ended in {r} sec")



async def main():
    await asyncio.gather(download(), printer(), ai())
    print( "Main ended")




if __name__ == "__main__":
    start_time = time.perf_counter()
    asyncio.run(main())
    end_time = time.perf_counter()
    total_time = end_time - start_time
    print(f"Executed in {total_time} seconds")