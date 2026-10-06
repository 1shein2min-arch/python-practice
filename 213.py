cart = {
    "Phone" : 500000,
    "Laptop" : 1200000,
    "Watch" : 250000,
    "Mouse" : 150000
}
def carts(name,price) :
    print(f"{name} : {price}")

def status(name,price) :
    if price >= 500000 :
        print(f"{name} : Expensive")
    else :
        print(f"{name} : Cheap")

def details(name,price) :
    print(f"{name} Price : {price}")

def group(name,price) :
    print("Expensive :")
    for name,price in cart.items() :
        if price >= 500000 :
            print(f"{name}")
    print("Cheap :")
    for name,price in cart.items() :
        if price < 500000 :
            print(f"{name}")

def summary(name,price) :
    print(f"Total Products : {len(cart)}")
    total = 0
    for price in cart.values() :
        total = total + price
    print(f"Total Price :{total}")

    highest_price = 0
    highest_name = ""

    lowest_price = 9999999
    lowest_name = ""

    for name,price in cart.items() :
        if price > highest_price :
            highest_price = price
            highest_name = name
        if price < lowest_price :
            lowest_price = price
            lowest_name = name

    print("Highest :")
    print(f"{highest_name} : {highest_price}")

    print("Lowest :")
    print(f"{lowest_name} : {lowest_price}")

print("===== Shopping Cart =====")

print("Products :")
for name,price in cart.items() :
    carts(name,price)

print("===== Product Status =====")

for name,price in cart.items() :
    status(name,price)

print("===== Product Details =====")
for name,price in cart.items() :
    details(name,price)

print("===== Price Groups =====") 
group(name,price)

print("===== Cart Summary =====")
summary(name,price)



