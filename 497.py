import requests

data = {
    "name": "Shein",
    "age": 24
}

response = requests.post(
    "https://jsonplaceholder.typicode.com/posts",
    json=data
)

print(response.status_code)

result = response.json()

print(result)

print("Git Practice")

print("Git diff practice")

print("Git Pull Practice")
