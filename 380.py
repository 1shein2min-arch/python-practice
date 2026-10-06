import requests 

response = requests.patch(
    "https://httpbin.org/patch",
    json= {
        "status" : "Delivered"
    }
)

print(response.status_code)

data = response.json()

print("===== PATCH =====")
print(f"Status : {data['json']['status']}")