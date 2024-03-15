import requests
from dotenv import load_dotenv
import os

url = "https://my-api.plantnet.org/v2/identify/all"

headers ={}

payload = {
    "api-key": os.getenv("plantnet_APIkey")
}

files = {
    "images": open("image1.jpg", "rb")
}

response = requests.post(url, headers=headers, params=payload, files=files)
response.status_code
response.json()

