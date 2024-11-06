import asyncio

async def fn():
    print("one")
    await asyncio.sleep(1)
   # asyncio.create_task(fn2())
    gather_future = asyncio.gather(fn3(), fn2())
    await gather_future
    print("four")
    await asyncio.sleep(1)
    print("five")
    await asyncio.sleep(1)
    
async def fn2():
    print("two")
    await asyncio.sleep(1)
    print("three")
    await asyncio.sleep(1)

async def fn3():
    print("six")
    await asyncio.sleep(1)
    print("seven")




asyncio.run(fn())