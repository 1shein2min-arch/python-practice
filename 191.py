products = {
    "Phone" : 500000 ,
    "Laptop" : 1200000 ,
    "Tablet" : 700000 ,
    "Watch" : 250000 ,
    "Camera" : 800000 ,
    "Mouse" : 150000
}

print("Product Names :")
for name in products.keys() :
    print(name)

print("Prices :")
for price in products.values() :
    print(price)

print("Expensive :")
for name,price in products.items() :
    if price >= 800000 :
        print(name)

print("Cheap :")
for name,price in products.items() :
    if price <= 250000 :
        print(name)

print(f"Total Products : {len(products)}")

names = []
for name in products.keys() :
    names.append(name)

names.sort()
print("Sorted Names :")
print(names)

highest_price = 0 
highest_name = ""

lowest_price = 9999999
lowest_name = ""

for name,price in products.items() :
    if price > highest_price :
        highest_price = price
        highest_name = name
    if price < lowest_price :
        lowest_price = price
        lowest_name = name

print(f"Highest : {highest_name} : {highest_price}")
print(f"Lowest : {lowest_name} : {lowest_price}")