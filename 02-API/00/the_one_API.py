import requests
from dotenv import load_dotenv
import os


headers = { 
    "Authorization": f"Bearer {os.getenv("the_one_APIkey")}"
}

response = requests.get("https://the-one-api.dev/v2/movie", headers=headers)
response.status_code
response.json()