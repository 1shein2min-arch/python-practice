import requests

response = requests.get(
    "https://httpbin.org/get",
    params={"name" : "SheiN","city" : "Yangon","job" : "Developer"}
)

data = response.json()

print("===== User Info =====")

print(f"Name : {data["args"]["name"]}")
print(f"City : {data["args"]["city"]}")
print(f"Job : {data["args"]["job"]}")

