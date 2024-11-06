import requests
import os
import dotenv

#user_input = input("Describe a plant or flower: ")
#print("Loading...")
url = 'https://54285744-illusion-diffusion.gateway.alpha.fal.ai/'

dotenv.load_dotenv()
api = os.getenv("illusion_diffision_APIkey")

user_input = input("Describe what you wanna see!: ")
print("Loading...")

headers = {
"Authorization": api,
"Content-Type": "application/json"
}
payload = {

    "image_url": "https://storage.googleapis.com/falserverless/illusion-examples/pattern.png",
    "prompt": f"(masterpiece:1.4), (best quality), (detailed), {user_input}",
    "negative_prompt": "(worst quality, poor details:1.4), lowres, (artist name, signature, watermark:1.4), bad-artist-anime, bad_prompt_version2, bad-hands-5, ng_deepnegative_v1_75t"
}

response = requests.post(url, headers=headers, json=payload)


# Check if the request was successful
if response.status_code == 200:
    data = response.json()
    image_url = data["image"]["url"]
    
    # Download the image
    image_response = requests.get(image_url)
    with open("downloaded_image.png", "wb") as image_file:
        image_file.write(image_response.content)
    
    print("Image downloaded successfully.")
else:
    print("Failed to download the image. Status code:", response.status_code)
