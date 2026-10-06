import requests

response = requests.get("https://api.github.com")

print(response.status_code)

data = response.json()

print(data['user_url'])