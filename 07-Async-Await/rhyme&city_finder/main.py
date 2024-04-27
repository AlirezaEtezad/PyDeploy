import requests
import asyncio
import dotenv
import os

dotenv.load_dotenv()
rhyme_api = os.getenv("ryhme_APIkey")


word = input("یک کلمه جهت یافتن قافیه وارد کنید: ")
state = input("نام یک استان را وارد کنید: ")
city = input("نام یک شهر را وارد کنید: ")


async def rhyme_finder():

    url = f"https://rhyming.ir/api/rhyme-finder?api={rhyme_api}&w={word}&sb=1&mfe=2&eq=1"
    response = requests.request("GET", url)
    data = response.json()
    print(f"هم قافیه های :{word}")
    for item in data["data_items"]:
        print(item["word"])

async def get_states():
    url = "https://iran-locations-api.ir/api/v1/fa/states"
    response = requests.request("GET", url)
    data = response.json()
    print("نام استان های ایران:")
    for item in data:
        for key, value in item.items():
            print(f"{key}: {value}")
        print()


async def get_cities():


    response = requests.get(f"https://iran-locations-api.ir/api/v1/fa/cities?state={state}")
    data = response.json()
   # print(data)
    for key, value in data.items():
        if key == 'cities':
            print(f"{key}:")
            for city in value:
                print(city['name'])
        else:
            print(f"{key}: {value}")
            

    cities = data['cities']
    for cit in cities:
        if cit['name'] == city:
            print(cit)


async def get_coordiantes():
    await get_states()
    await get_cities()


async def main():
    asyncio.gather(rhyme_finder(), get_coordiantes() )

asyncio.run(main())