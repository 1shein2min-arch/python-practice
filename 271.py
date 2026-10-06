price = 500000

print("1. Show Price")
print("2. Buy")
print("3. Exit")

while True :
    try :
        choice = int(input("Enter Choose :"))

        if choice == 1 :
            print(f"Price : {price}")

        elif choice == 2 :
            try :
                quantity = int(input("Enter Quantity :"))
                total = price * quantity
                if total >= 1000000 :
                    discount = total * 0.01 
                    final_price = total - discount
                    print(f"Final Price : {final_price}")
                else :
                    print(f"Final Price : {total}")

            except ValueError :
                print("Please Enter A Valid Quantity")

        elif choice == 3 :
            print("Goodbye !")
            break
    except ValueError :
        print("Please Enter A Valid Choice")


