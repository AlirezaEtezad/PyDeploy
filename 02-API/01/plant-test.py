import argparse
import requests
import cv2
import matplotlib.pyplot as plt
import os 
import dotenv
dotenv.load_dotenv()
plantnet_api_key = os.getenv("planetnet_APIkey")
generated_image = "downloaded_image.png"
plantnet_url = "https://my-api.plantnet.org/v2/identify/all"

def recognize_plant(generated_image):

    plant_headers = {}


    plant_payload = {
        "api-key": plantnet_api_key
    }

    plant_files = {
        "images": open(generated_image, "rb")
    }

    response = requests.post(plantnet_url, headers=plant_headers, params=plant_payload, files=plant_files)
    response.raise_for_status()
    print(f"plant status code is: {response.status_code}")

    plant_data = response.json()
    # print(plant_data)
    return plant_data["results"][0]["species"]["commonNames"][0]


try:
    # Generate image based on the flower/plant name
    # generated_image = generate_image(args.plant_name)

    recognized_plant_name = recognize_plant(generated_image)

    print("Recognized plant name:", recognized_plant_name)

except requests.exceptions.HTTPError as err:
    print("HTTP error occurred:", err)

except Exception as e:
    print("An error occurred:", e)
