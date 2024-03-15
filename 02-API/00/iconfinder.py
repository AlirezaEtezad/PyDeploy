
import requests
from dotenv import load_dotenv
import os


url = "https://api.iconfinder.com/v4/icons/search?query=arrow&count=10"

headers = {
    "accept": "application/json",
    "Authorization": f"Bearer {os.getenv("iconfinder_API")} "
}

response = requests.get(url, headers=headers)
response.status_code
response.json()