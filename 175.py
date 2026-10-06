products = {
    "Phone" : 500000 ,
    "Laptop" : 1200000 ,
    "Tablet" : 700000 ,
    "Watch" : 250000 ,
    "Camera" :800000
}
for name in products :
    print(f"{name} :{products[name]}")

print(f"Total Products : {len(products)}")

if "Phone" in products :
    print("Phone Found")
if "Mouse" in products :
    print("Mouse Found")
else :
    print("Mouse Not Found")

prices = []
for name in products :
    prices.append(products[name])

prices.sort()
print(prices)

print(f"Highest Price : {prices[-1]}")
print(f"Lowest price : {prices[0]}")

print(f"500000 Count : {prices.count(500000)}")