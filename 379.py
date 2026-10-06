import requests

response = requests.put(
    "https://httpbin.org/put",
    json= {
        "customer" : "Aung" ,
        "model" : "Redmi Note 13" ,
        "fee" : 55000 ,
        "status" : "Done"
    }
)

print(response.status_code)

data = response.json()

print("===== POST =====")

print(f"Customer : {data['json']['customer']}")
print(f"Model : {data['json']['model']}")
print(f"Fee : {data['json']['fee']}")
print(f"status : {data['json']['status']}")