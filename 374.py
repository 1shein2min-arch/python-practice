import requests

response = requests.put(
    "https://httpbin.org/put",
    json={
        "model" : "Redmi Note 13",
        "customer" : "Aung",
        "status" : "Done",
        "fee" : 50000
    }
)

data = response.json()

print("===== Repair Update =====")

print(f"Model : {data['json']['model']}")
print(f"Customer : {data['json']['customer']}")
print(f"Status : {data['json']['status']}")
print(f"Fee : {data['json']['fee']}")