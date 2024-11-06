import requests
from dotenv import load_dotenv
import os

load_dotenv()
api = os.getenv("iconfinder_APIkey")
url = "https://api.iconfinder.com/v4/icons/search"

headers = {
    "accept": "application/json",
    "Authorization": api
}

payload ={
"querry": "arrow",
"count": "10"
}


response = requests.get(url, headers=headers, params=payload)
print(response.status_code)
#print(response.text)
print(response.json())