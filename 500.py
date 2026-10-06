import requests

data = {
    "name": "Shein",
    "age": 25
}

response = requests.put(
    "https://httpbin.org/put",
    json=data
)

response.raise_for_status()

result = response.json()

print(result["json"]["age"])