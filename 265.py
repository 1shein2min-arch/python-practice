products = {
    "Phone": 500000,
    "Laptop": 1200000,
    "Watch": 250000,
    "Camera": 800000
}

def show_product() :
    for name,price in products.items() :
        print(f"{name} : {price}")

def check_product():
    name = input("Enter Name :")
    if name in products :
        price = products.get(name)
        print(f"Price : {price}")
    else :
        print("Product Not Found")

def add_product() :
    name = input("Enter Name :")
    if name not in products:
        price = int(input("Enter Price :"))
        products[name] = price
        print("Product Added")
    else :
        print("Product Already Exists")

def update_price() :
    name = input("Enter Name :")
    if name in products :
        price = int(input("Enter Price :"))
        products[name] = price
        print("Price Updated")
    else :
        print("Product Not Found")

def remove_product() :
    name = input("Enter Name :")
    if name in products :
        products.pop(name)
        print("Product Removed")
    else :
        print("Product Not Found")

def buy_product() :
    name = input("Enter Name :")
    if name in products :
        price = products.get(name)
        quantity = int(input("Enter Quantity :"))
        total = price * quantity
        if total >= 1000000 :
            discount = total * 0.1 
            final_price = total - discount
            print(f"Final Price : {final_price}")
        else :
            discount = 0 
            final_price = total - discount
            print(f"Final Price : {final_price}")

    else :
        print("Product Not Found")

def vip() :
    for name,price in products.items() :
        if price >= 1000000 :
            print(f"{name} :VIP ")

def count() :
    product_count = 0
    for name,price in products.items() :
        product_count += 1
    print(f"Product Count: {product_count}")

def  goodbye():
    print("Goodbye !")

while True :
    print("===== Product Management =====")

    print("1. Show Products")
    print("2. Check Product")
    print("3. Add Product")
    print("4. Update Product")
    print("5. Remove Product")
    print("6. Buy Product")
    print("7. Check VIP Products")
    print("8. Product Count")
    print("9. Exit")

    choice = int(input("Enter Choose :"))

    if choice == 1 :
        show_product()

    elif choice == 2 :
        check_product()

    elif choice == 3 :
        add_product() 

    elif choice == 4 :
        update_price()

    elif choice == 5 :
        remove_product()

    elif choice == 6 :
        buy_product()

    elif choice == 7 :
        vip()

    elif choice == 8 :
        count()

    elif choice == 9 :
        goodbye()
        break

    else :
        print("Invalid Choice")