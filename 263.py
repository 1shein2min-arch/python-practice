products = {
    "Phone": 10,
    "Laptop": 5,
    "Watch": 20,
    "Camera": 3
}

def show_product() :
    for name,stock in products.items() :
        print(f"{name} : {stock}")

def check_stock() :
    name = input("Enter Name :")
    if name in products :
        print(products.get(name))
    else :
        print("Product Not Found")

def add_stock(stock) :
    return 0 + stock

def sell_product () :
    name = input("Enter Name :")
    if name in products :
        stock = int(input("Enter Stock :"))
        old_stock = products.get(name)
        if stock > old_stock :
            print("Insufficient Stock")
        else :
            remain = old_stock - stock
            products[name] = remain
            print("Sell Product")
    else :
        print("Product Not Found")

def low_stock() :
    for name,stock in products.items() :
        if stock <= 5 :
            print(f"{name} : {stock}")

def goodbye() :
    print("Goodbye !")

while True:

    print("1. Show Products")
    print("2. Check Stock")
    print("3. Add Stock")
    print("4. Sell Product")
    print("5. Low Stock")
    print("6. Exit")

    choice = int(input("Enter Choose :"))

    if choice == 1 :
        show_product()

    elif choice == 2 :
        check_stock()

    elif choice == 3 :
        name = input("Enter Name :")
        if name not in products :
            stock = int(input("Enter Stock :"))
            add_stock(stock)
            products[name] = stock
            print("Product Added")
        else :
            print("Product Already Exists")

    elif choice == 4 :
        sell_product() 

    elif choice == 5 :
        low_stock()

    elif choice == 6 :
        goodbye()
        break

    else :
        print("Invalid Choice")
