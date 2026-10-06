import requests

response = requests.get("https://httpbin.org/uuid")

data = response.json()

print(response.status_code)

print(type(data))

print(data["uuid"])