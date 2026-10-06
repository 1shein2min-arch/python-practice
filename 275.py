accounts = {
    "Aung": 500000,
    "Ko Ko": 800000,
    "Su Su": 1200000
}

def show_acc() :
    for name , balance in accounts.items() :
        print(f"{name} : {balance}")

def withdraw (balance,amount) :
    return balance - amount

def show_vip(balance) :
    if balance >= 1000000 :
        return "VIP"
    else :
        return "Normal" 

def goodbye() :
    print("Goodbye !")

while True :

    print("1. Show Accounts")
    print("2. Withdraw")
    print("3. Show VIP")
    print("4. Exit")

    try :

        choice = int(input("Enter Choose :"))

        if choice == 1 :
            show_acc() 

        elif choice == 2 :
            name = input("Enter Name :")
            if name in accounts :
                try :
                    amount = int(input("Enter Withdraw :"))
                    balance = accounts.get(name)

                    if balance >= amount :
                        remain = withdraw(balance,amount)
                        accounts[name] = remain 
                        print(f"{name} : {remain}")

                    else :
                        print("Insufficient Balance")

                except ValueError :
                    print("Please Enter A Valid Amount")

            else :
                print("Account Not Found")

        elif choice == 3 :
            for name,balance in accounts.items() :
                print(f"{name} : {show_vip(balance)}")

        elif choice == 4 :
            goodbye()
            break

        else :
            print("Invalid Choice")

    except ValueError :
        print("Please Enter A Valid Choice")
                



