import requests 

response = requests.get(
    "https://httpbin.org/get",
    params={"name" : {"SheiN"}}
)

data = response.json()

print(data["args"])


