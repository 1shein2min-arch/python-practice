products = ["Phone", "Laptop", "Headset", "Charger", "Mouse"]

def show_product() :
    for product in products :
        print(product)

def search_prodcut ():
    name = input("Enter Name :")
    if name in products :
        print("Product Found")
    else :
        print("Product Not Found")

def add_product () :
    name = input("Enter Name :")
    if name not in products :
        products.append(name)
        print("Product Added")
    else :
        print("Product Already Exists")

def goodbye() :
    print("Goodbye !")

while True :

    print("1. Show Products ")
    print("2. Search Product")
    print("3. Add Product")
    print("4. Exit")

    try :
        choice = int(input("Enter Choose :"))

        if choice == 1 :
            show_product()

        elif choice == 2 :
            search_prodcut()

        elif choice == 3 :
            add_product()

        elif choice == 4 :
            goodbye()
            break

        else :
            print("Invalid Choice ")

    except ValueError :
        print("Please Enter A Valid Choice")