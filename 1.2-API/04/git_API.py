import requests
print("This app will show you the number of github followers and followings!")
username = input("Enter username: ") 
url = f"https://api.github.com/users/{username}"
print("Loading...")


# user_data = requests.get(url)
# json_file = user_data.json()

# print("Number of followers:",json_file['followers'])
# print("Number of followings:",json_file['following'])


try:
    user_data = requests.get(url)
    user_data.raise_for_status()  # Raise an exception for 4XX/5XX status codes
    json_file = user_data.json()
    print("Number of followers:", json_file['followers'])
    print("Number of followings:", json_file['following'])
except requests.exceptions.RequestException as e:
    print("Failed to fetch data. Error:", e)