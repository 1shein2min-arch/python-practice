import requests

response = requests.delete(
    "https://httpbin.org/delete"
)

response.raise_for_status()

result = response.json()

print(result["url"])