import requests

data = {
    "age": 26
}

response = requests.patch(
    "https://httpbin.org/patch",
    json=data
)

response.raise_for_status()

result = response.json()

print(result["json"]["age"])