products = {
    "Phone" : 500000,
    "Laptop" : 1200000,
    "Watch" : 250000,
    "Camera" : 800000,
    "Mouse" : 150000
}
def product(name,price) :
    print(f"{name} : {price}")

def expensive(name,price) :
    if price >= 800000 :
        print(name)

def cheap(name,price) :
    if price <=250000 :
        print(name)

def total() :
    print(f"Total Product : {len(products)}")

def total_price() :
    total = 0
    for price in products.values() :
        total = total + price
    print(f"Total Price : {total}")

def highest() :
    highest_name = ""
    highest_price = 0

    for name,price in products.items() :
        if price > highest_price :
            highest_price = price
            highest_name = name
    print(f"Highest :")
    print(f"{highest_name} : {highest_price}")

def lowest() :
    lowest_name = ""
    lowest_price = 9999999
    for name,price in products.items() :
        if price < lowest_price :
            lowest_price = price
            lowest_name = name
    print(f"Lowest :")
    print(f"{lowest_name} : {lowest_price}")

print("===== Shopping Cart =====")

print("Products :")
for name,price in products.items() :
    product(name,price)

print("Expensive :")
for name,price in products.items() :
    expensive(name,price)

print("Cheap :")
for name,price in products.items() :
    cheap(name,price)

total()

total_price()

highest()

lowest()