import requests

response = requests.patch(
    "https://httpbin.org/patch",
    json={
        "customer" : "Aung",
        "status" : "Done"
    }
)

print(response.status_code)

print(response.headers['Content-Type'])
data = response.json()

print("===== Patch Update =====")

print(f"Customer : {data['json']['customer']}")
print(f"Status : {data['json']['status']}")