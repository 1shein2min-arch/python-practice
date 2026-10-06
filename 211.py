products = {
    "Phone": 500000,
    "Laptop": 1200000,
    "Tablet": 700000,
    "Watch": 250000,
    "Camera": 800000
}

def show_products() :
    for name,price in products.items() :
        print(f"{name} : {price}")

def add_product() :
    name = input("Enter Name :")
    if name not in products :
        price = int(input("Enter Price"))
        products.update({name : price})
        print(f"{name} Added")
    else :
        print("Name Already Exists")

def update_product() :
    name = input("Enter Name :")
    if name in products :
        price = int(input("Enter New Price :"))
        products.update({name : price})
        print(f"{name} Updated")
    else:
        print("Name Not Found")

def remove_product() :
    name = input("Enter Name :")
    if name in products :
        products.pop(name)
        print(f"{name} Removed")
    else :
        print("Name Not Found")

def find_product() :
    name = input("Enter Name :")
    if name in products :
        print(f"{name} Price : {products.get(name)}")
    else :
        print("Product Not Found")

def expensive () :
    print("Expensive :")
    for name,price in products.items() :
        if price >= 800000 :
            print(name)

def cheap () :
    print("Cheap :")
    for name,price in products.items() :
        if price <= 300000 :
            print(name)

def highest() :
    print("Highest :")
    highest_price = 0
    highest_name = ""
    for name,price in products.items() :
        if price > highest_price :
            highest_price = price
            highest_name = name
    print(f"{highest_name} :{highest_price}")

def lowest() :
    print("Lowest :")
    lowest_price = 9999999
    lowest_name = ""
    for name,price in products.items() :
        if price < lowest_price :
            lowest_price = price
            lowest_name = name
    print(f"{lowest_name} : {lowest_price}")

def total() :
    total = 0
    for price in products.values() :
        total =total + price
    print(f"Total Price : {total}")

def goodbye() :
    print("Goodbye!")

while True :
    print("===== Store Management =====")

    print("1. Show Products")
    print("2. Add Product")
    print("3. Updated Product")
    print("4. Remove Product")
    print("5. Find Product")
    print("6. Show Expensive Products")
    print("7. Show Cheap Products")
    print("8. Show Highest Price")
    print("9. Show Lowest Price")
    print("10. Total Price")
    print("11. Exit")

    choice = int(input("Enter Choose :"))

    if choice == 1 :
        show_products()

    elif choice == 2 :
        add_product()

    elif choice == 3 :
        update_product()

    elif choice == 4 :
        remove_product()

    elif choice == 5 :
        find_product()

    elif choice == 6 :
        expensive()

    elif choice == 7 :
        cheap()

    elif choice == 8 :
        highest()

    elif choice == 9 :
        lowest()

    elif choice == 10 :
        total()

    elif choice == 11 :
        goodbye()
        break

    else :
        print("Invalid Choice")