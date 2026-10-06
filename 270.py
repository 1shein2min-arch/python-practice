balance = 500000

print("1. Check Balance")
print("2. Withdraw")
print("3. Exit")

while True:
    try:
        choice = int(input("Enter Choose :"))

        if choice == 1:
            print(f"Balance : {balance}")

        elif choice == 2:
            try:
                amount = int(input("Enter Amount :"))

                if amount <= balance:
                    balance = balance - amount
                    print(f"Remaining Balance : {balance}")
                else:
                    print("Insufficient Balance")

            except ValueError:
                print("Please Enter A Valid Amount")

        elif choice == 3:
            print("Goodbye !")
            break

        else:
            print("Invalid Choice")

    except ValueError:
        print("Enter A Valid Number")