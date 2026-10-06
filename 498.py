import requests
from pprint import pprint
data = {
    "name": "Shein",
    "age": 24
}

response = requests.post(
    "https://httpbin.org/post",
    json=data
)

print(response.status_code)

result = response.json()

pprint(result)

print(result["data"]["name"])