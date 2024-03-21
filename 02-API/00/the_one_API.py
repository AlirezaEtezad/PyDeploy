import requests
# from dotenv import load_dotenv
import os
import dotenv
dotenv.load_dotenv()

api = os.getenv("the_one_APIkey")
headers = { 
    "Authorization": api
}

response = requests.get("https://the-one-api.dev/v2/movie", headers=headers)
print(f"Status code is: {response.status_code}")
print("response is: ")
print(response.json())