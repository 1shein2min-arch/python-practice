products = {
    "Phone": 500000,
    "Laptop": 1200000,
    "Watch": 250000,
    "Camera": 800000
}

print("===== Product Check =====")
print("Products :")
for name,price in products.items() :
    print(f"{name} : {price}")

print("Expensive :")
for name,price in products.items() :
    if price >= 800000 :
        print(name)

print("Cheap :")
for name,price in products.items() :
    if price <= 250000 :
        print(name)

print(f"Total Products : {len(products)}")

total = 0
for price in products.values() :
    total = total + price
print(f"Total Price : {total}")

highest_price = 0
highest_name = ""

for name,price in products.items() :
    if price > highest_price :
        highest_price = price
        highest_name = name

print("Highest :")
print(f"{highest_name} : {highest_price}")

lowest_price = 9999999
lowest_name = ""

for name,price in products.items() :
    if price < lowest_price :
        lowest_price = price
        lowest_name = name

print("Lowest :")
print(f"{lowest_name} : {lowest_price}")