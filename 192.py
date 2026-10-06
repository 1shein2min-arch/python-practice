products = {
    "Phone" : 500000,
    "Laptop" : 1200000,
    "Tablet" : 700000,
    "Watch" : 250000,
    "Camera" : 800000
}

print("Before")
for name in products.keys() :
    print(name)

print("After:")
products.pop("Watch")
for name in products.keys() :
    print(name)

print(f"Total Products : {len(products)}")
