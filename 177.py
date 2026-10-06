products = {
    "Phone" : 500000,
    "Laptop" : 1200000,
    "Tablet" : 700000,
    "Watch" : 250000,
    "Camera" : 800000
}
for name , price in products.items() :
    print(name,price)

print("Expensive :")
for name , price in products.items() :
    if price >= 800000 :
        print(name)

print("Cheap :")
for name,price in products.items() :
    if price <= 250000 :
        print(name)




