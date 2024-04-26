import time
import random
import asyncio


async def ai_video():
    print("video start")
    r = random.randint(0, 5)
    await asyncio.sleep(r)
    print (f"video ended in {r} sec")
    return r


async def ai_audio():
    print("audio start")
    r = random.randint(0, 5)
    await asyncio.sleep(r)
    print (f"audio ended in {r} sec")
    return r

def mix():
    print("mix start")
    r = random.randint(0, 3)
    time.sleep(r)
    print (f"mix ended in {r} sec")
    return r



async def render():
    print("render start")
    await asyncio.gather(ai_audio(), ai_video())
    mix()
    print("render ended.")




if __name__ == "__main__":
    start_time = time.perf_counter()
    asyncio.run(render())
    end_time = time.perf_counter()
    total_time = end_time - start_time
    print(f"Executed in {total_time} seconds")