import requests

username = input("Enter username: ") 
url = f"https://api.github.com/users/{username}"
print("Loading...")
user_data = requests.get(url)
json_file = user_data.json()

print("Number of followers:",json_file['followers'])
print("Number of followings:",json_file['following'])