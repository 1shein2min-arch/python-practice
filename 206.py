products = {
    "Phone" : 500000,
    "Laptop" : 1200000,
    "Tablet" : 700000,
    "Watch" : 250000
}

while True :
    print("===== Product Menu =====")

    print("1. Show Products")
    print("2. Add Product")
    print("3. Update Product")
    print("4. Remove Product")
    print("5. Find Product")
    print("6. Exit")

    choice = int(input("Enter Choose :"))

    if choice == 1 :
        for name,price in products.items() :
            print(f"{name} : {price}")

    elif choice == 2 :
        name = input("Enter Product :")
        price = int(input("Enter Price :"))
        products.update({name:price})
        print(f"{name} Added")

    elif choice == 3 :
        name = input("Enter Product :")
        if name in products :
            price = int(input("Enter New Price :"))
            products.update({name:price})
            print(f"{name} Updated")
        else:
            print("Product Not Found")

    elif choice == 4 :
        name = input("Enter Product :")
        if name in products :
            products.pop(name)
            print(f"{name} Removed")
        else:
            print(f"Product Not Found")

    elif choice == 5 :
        name = input("Enter name :")
        if name in products :
            print(f"{name} : {products.get(name)}")
        else :
            print("Product Not Found")

    elif choice == 6 :
        print("Goodbye!")
        break

    else :
        print("Invalid choice")

    


    