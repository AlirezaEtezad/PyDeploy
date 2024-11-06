import time
import random
import asyncio


async def marriage(name):

    r = random.randint(0, 10)
    await asyncio.sleep(r)
    print(f"{name} after {r} years")




async def main():
    await asyncio.gather(marriage("ch1"), marriage("ch2"), marriage("ch3"), marriage("ch4"))


    # for child in ["ch1" , "ch2", "ch3", "ch4"]:
    #     asyncio.create_task(marriage(child))




if __name__  == "__main__":
    start_time = time.perf_counter()
    asyncio.run(main())
    end_time = time.perf_counter()
    total_time = end_time - start_time
    print(f"Executed in {total_time} seconds")