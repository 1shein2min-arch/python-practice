accounts = {
    "Aung": 500000,
    "Ko Ko": 1200000,
    "Hla Hla": 750000,
    "Su Su": 1500000
}

def show_acc() :
    for name,balance in accounts.items() :
        print(f"{name} : {balance}")

def show_bal() :
    name = input("Enter Name :")
    if name in accounts :
        balance = accounts.get(name)
        print(f"balance :{balance}")
    else :
        print("Account Not Found")

def deposit(balance,deposit) :
    return balance + deposit

def show_exit() :
    print("Goodbye!")

while True :
    print("1. Show Accounts")
    print("2. Check Balance")
    print("3. Deposit")
    print("4. Exit")

    choice = int(input("Enter Choose :"))

    if choice == 1 :
        show_acc()

    elif choice == 2 :
        show_bal()

    elif choice == 3 :
        name = input("Enter Account")
        if name in accounts:
            amount = int(input("Enter Deposit :"))
            total = deposit(accounts.get(name),amount)

            print(f"Old balance : {accounts.get(name)}")
            print(f"Deposit : {amount}")
            print(f"New Balance :{total}")
            accounts[name] = total

        else:
            print("Account Not Found")

    elif choice == 4 :
        show_exit()
        break

    else:
        print("Invalid Choice")