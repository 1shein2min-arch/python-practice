import requests

response = requests.post(
    "https://httpbin.org/post",
    json= {
        "customer" : "Aung",
        "model" : "Redmi Note 13",
        "fee" : 50000 ,
        "status" : "Pending"
    }
)

print(response.status_code)
data = response.json()

print(f"Customer : {data['json']['customer']}")
print(f"Model : {data['json']['model']}")
print(f"Fee : {data['json']['fee']}")
print(f"Status : {data['json']['status']}")