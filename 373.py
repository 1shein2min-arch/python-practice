import requests

response = requests.post(
    "https://httpbin.org/post",
    json={
        "product" : "Redmi Note 13",
        "price" : 500000,
        "status" : "paid"
    }
)

data = response.json()


print(f"Product : {data['json']['product']}")
print(f"Price : {data['json']['price']}")
print(f"Status : {data['json']['status']}")
print(f"Content Type : {response.headers['Content-Type']}")