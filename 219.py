products = {
    "Phone" : 500000,
    "Laptop" : 1200000,
    "Watch" : 250000
}
def product() :
    for name,price in products.items() :
        print(f"{name} : {price}")

def total_product() :
    print(f"Total Products : {len(products)}")

def total_price() :
    total = 0
    for price in products.values() :
        total = total + price
    print(f"Total Price : {total}")

def highest() :
    highest_price = 0
    highest_name = ""
    for name,price in products.items() :
        if price > highest_price :
            highest_price = price
            highest_name = name
    print("Highest :")
    print(f"{highest_name} : {highest_price}")

def lowest() :
    lowest_price = 9999999
    lowest_name = ""
    for name,price in products.items() :
        if price < lowest_price :
            lowest_price = price
            lowest_name = name
    print("Lowest :")
    print(f"{lowest_name} : {lowest_price}")

print("===== Product Information =====")

product()

total_product()

total_price()

highest()

lowest()
