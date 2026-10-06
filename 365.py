import requests 

response = requests.get("https://dummyjson.com/products")

data = response.json()

print("===== First Product =====")

print(f"Title : {data['products'][0]['title']}")
print(f"Price : {data['products'][0]['price']}")