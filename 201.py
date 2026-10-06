products = {
    "Phone": 500000,
    "Laptop": 1200000,
    "Tablet": 700000,
    "Watch": 250000,
    "Camera": 800000
}

print("===== Store Management =====")

print("Before :")
for name,price in products.items() :
    print(f"{name} : {price}")

products.update({"Phone" : 550000})
products.pop("Watch")
products.update({"Headphone" : 300000})

print("Phone Updated")
print("Watch Removed")
print("Headphone Added")

print("After :")
for name,price in products.items() :
    print(f"{name} : {price}")

print(f"Total Products : {len(products)}")

print("Expensive :")
for name,price in products.items() :
    if price >= 800000 :
        print(name)

print("Cheap :")
for name,price in products.items() :
    if price <= 300000 :
        print(name)

total =0
for price in products.values() :
    total =total + price
print(f"Total Price : {total}")

names = []
for name in products.keys() :
    names.append(name)

names.sort()
print("Sorted Name :")
print(names)

print(f"Phone Price : {products.get('Phone')}")
print(f"Mouse Price : {products.get('Mouse',0)}")

highest_name = ""
highest_price = 0

lowest_name = ""
lowest_price = 9999999

for name,price in products.items() :
    if price > highest_price :
        highest_price = price
        highest_name = name

    if price < lowest_price :
        lowest_price = price
        lowest_name = name

print(f"Highest : {highest_name} : {highest_price}")
print(f"Lowest : {lowest_name} : {lowest_price}")