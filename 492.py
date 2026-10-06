import requests

response = requests.get("https://api.github.com/users/abcef123456789")

print(response.raise_for_status())

data = response.json()

print(data["login"])