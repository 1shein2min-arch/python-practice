import requests 

response = requests.get("https://dummyjson.com/products")

print(response.status_code)

print(response.headers['content-Type'])

data = response.json()

count = 0
for product in data['products'] :
    if product['price'] > 100 :
        count = count + 1

print("===== Product Count =====")
print(f"Expensive Products : {count}")

