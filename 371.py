import requests
import json

response = requests.post(
    "https://httpbin.org/post",
    data={
        "name" : "Aung",
        "phone" : "Redmi Note 13",
        "fee" : 50000
    }
)


data = response.json()
print(json.dumps(data,indent=4))

print("===== Customer =====")

print(f"Name : {data['form']['name']}")
print(f"Phone : {data['form']['phone']}")
print(f"Fee : {data['form']['fee']}")