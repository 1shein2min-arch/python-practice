accounts = {
    "Aung": 500000,
    "Ko Ko": 800000,
    "Su Su": 1200000
}

def show_acc () :
    for name,balance in accounts.items() :
        print(f"{name} : {balance}")

def deposit(balance,amount) :
    return balance + amount

def goodbye () :
    print("Goodbye !")

while True :

    print("Show Accounts")
    print("Deposit")
    print("Exit")

    try :
        choice = int(input("Enter Choose :"))

        if choice == 1 :
            show_acc()

        elif choice == 2 :
            name = input("Enter Name :")
            if name in accounts :

                try :
                    amount = int(input("Enter Amount :"))
                    balance = accounts.get(name)
                    total = deposit(balance,amount)
                    accounts[name] = total

                    print(f"Old Balance : {balance}")
                    print(f"Deposit : {amount}")
                    print(f"New Balance : {total}")

                except ValueError:
                    print("Please Enter a Vaid Amount")

            else :
                print("Account Not Found")

        elif choice == 3 :
            goodbye()
            break

        else :
            print("Invalid Choice")

    except ValueError:
        print("Please Enter A Valid Choice")

                


