account = {
    "Aung" : 500000,
    "Ko Ko" : 1200000,
    "Hla Hla" : 750000,
    "Su Su" : 1500000
}

def show_acc() :
    for name,balance in account.items() :
        print(f"{name} : {balance}")

def add_interest(balance) :
    if balance >= 1000000 :
        return  balance * 0.05
    else :
        return balance * 0.03

def show_vip() :
    for name,balance in account.items() :
        if balance >= 1000000 :
            print(f"{name} : {balance}")

def goodbye() :
    print("Goodbye !")

while True :
    print("1. Show Accounts")
    print("2. Add Interest")
    print("3. Show Vip")
    print("4. Exit")

    choice = int(input("Enter Choose :"))

    if choice == 1 :
        show_acc()

    elif choice == 2 :
        name = input("Enter Name :")
        if name in account :
            balance = account.get(name)
            interest = add_interest(balance)
            total = balance + interest
            account[name] = total
            print("Account Updated")
        else :
            print("Account Not Found")

    elif choice == 3 :
        show_vip()

    elif choice == 4 :
        goodbye()
        break

    else :
        print("Invalid Choice")
