import requests

data = {
    "name": "Shein",
    "age": 24
}

response = requests.post(
    "https://httpbin.org/post",
    json=data
)

response.raise_for_status()

data = response.json()

print(data['json']['age'])