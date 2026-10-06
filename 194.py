products = {
    "Phone" : 500000,
    "Laptop" : 1200000,
    "Watch" : 250000,
    "Camera" : 800000
}
print("Before :")
for name,price in products.items() :
    print(f"{name} : {price}")

products.update({"Phone" : 550000})
products.pop("Watch")
products.update({"Tablet" : 700000})

print("After :")
for name,price in products.items() :
    print(f"{name} : {price}")

print(f"Total Products :{len(products)}")