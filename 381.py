import requests 

response = requests.delete(
    "https://httpbin.org/delete"
)


data = response.json()

print("======= DELETE =======")

print(f"Status : {response.status_code}")