import os
import requests
from dotenv import load_dotenv
import argparse
import json

# Load environment variables from .env file
load_dotenv()

# Parse command-line arguments for flower/plant name
parser = argparse.ArgumentParser(description='Generate and recognize plant images')
parser.add_argument('plant_name', type=str, help='Enter a flower or plant name')
args = parser.parse_args()

# Get API keys from environment variables
illusion_api_key = os.getenv("illusion_diffision_APIkey")
plantnet_api_key = os.getenv("planetnet_APIkey")


illusion_url = 'https://54285744-illusion-diffusion.gateway.alpha.fal.ai/'
plantnet_url = "https://my-api.plantnet.org/v2/identify/all"
# image_exist = False

# Generate image using Illusion Diffusion API
def generate_image(text):
    headers = {
        "Authorization": illusion_api_key,
        "Content-Type": "application/json"
    }

    payload = {
        "image_url": "https://storage.googleapis.com/falserverless/illusion-examples/checkers.png",
        "prompt": f"(masterpiece:1.4), (best quality), (detailed), {text}",
        "negative_prompt": "(worst quality, poor details:1.4), lowres, (artist name, signature, watermark:1.4)"
    }

    response = requests.post(illusion_url, headers=headers, json=payload)
    response.raise_for_status()

        # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
        image_url = data["image"]["url"]
        
        # Download the image
        image_response = requests.get(image_url)
        with open("downloaded_image.jpg", "wb") as image_file:
            image_file.write(image_response.content)
        
        print("Image downloaded successfully.")
        print("Waiting for plantnet response...")
        # image_exist = True
        return "downloaded_image.jpg"
    else:
        print("Failed to download the image. Status code:", response.status_code)




  #  return image_response.content

# Recognize plant name using PlantNet API
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
    print(plant_data)
    return plant_data["results"][0]["species"]["commonNames"][0]

try:
    # Generate image based on the flower/plant name
    generated_image = generate_image(args.plant_name)

    recognized_plant_name = recognize_plant(generated_image)

    print("Recognized plant name:", recognized_plant_name)

except requests.exceptions.HTTPError as err:
    print("HTTP error occurred:", err)

except Exception as e:
    print("An error occurred:", e)
