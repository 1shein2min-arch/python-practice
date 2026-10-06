products = {
    "Phone" : 500000 ,
    "Laptop" : 1200000,
    "Tablet" : 700000 ,
    "Watch" : 250000 ,
    "Camera" : 800000
}
print("Product Names :")
for name in products.keys() :
    print(name)

print("Prices :")
for price in products.values() :
    print(price)

print("Phone Details :")
for name,price in products.items() :
    print(f"{name} : {price}")

print(f"Total Products : {len(products)}")

print("Expensive Products :")
for name,price in products.items() :
    if price >= 800000 :
        print(name)

print("Cheap Products :")
for name,price in products.items() :
    if price <= 250000 :
        print(name)

total = 0
for name,price in products.items() :
    total =total + price

print(f"Total Price : {total}")

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