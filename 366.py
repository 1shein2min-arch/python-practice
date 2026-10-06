import requests

response = requests.get("https://dummyjson.com/products")

data = response.json()

print("===== Product Rating =====")

print(f"Title : {data['products'][0]['title']}")
print(f"Rating : {data['products'][0]['rating']}")

if data['products'][0]['rating'] > 4.5 :
    print("Rating is High")
else :
    print("Rating is Low")