stock = 20 

print("1. Check Stock")
print("2. Sell Product")
print("3. Exit")

while True :
    try :
        choice = int(input("Enter Choose :"))

        if choice == 1 :
            print(f"Stock : {stock}")

        elif choice == 2 :
            try :
                quantity = int(input("Enter Quantity :"))
                if quantity == 0 or quantity < 0 :
                    print("Invalid Quantity")
                elif quantity > stock :
                    print("Insufficient Stock")
                else:
                    new_stock = stock - quantity
                    print(f"New Stock : {new_stock}")
            except ValueError :
                print("Please Enter Valid Quantity")

        elif choice == 3 :
            print("Goodbye")
            break

        else:
            print("Invalid Choice")

    except ValueError :
        print("Please Enter Valid Choice")