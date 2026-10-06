import requests 

response = requests.get(
    "https://httpbin.org/get",
    params= {
        "customer" : "Aung",
        "city" : "Yangon"
    }
)

print(response.status_code)
data = response.json()

print(f"Customer : {data['args']['customer']}")
print(f"City : {data['args']['city']}")

