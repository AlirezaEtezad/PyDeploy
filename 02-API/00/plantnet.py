import requests
from dotenv import load_dotenv
import os
load_dotenv()
api = os.getenv("plantnet_APIkey")

url = "https://my-api.plantnet.org/v2/identify/all"

headers ={}

payload = {
    "api-key": api
    }

files = {
    "images": open("image1.jpg", "rb")
}

response = requests.post(url, headers=headers, params=payload, files=files)
print(response.status_code)
print(response.json())

