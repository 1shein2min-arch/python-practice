accounts = {
    "Aung": 500000,
    "Ko Ko": 1200000,
    "Hla Hla": 750000,
    "Su Su": 1500000
}

def show_acc() :
    for name,balance in accounts.items() :
        print(f"{name} : {balance}")

def deposit(balance,amount) :
    return balance + amount

def withdraw(balance,amount) :
    return balance - amount

def can_transfer(balance,amount) :
    if balance >= amount :
        return True
    else :
        return False

while True :
    print("===== Bank System =====")

    print("1. Show Accounts")
    print("2. Check Balance")
    print("3. Deposit")
    print("4. Withdraw")
    print("5. Transfer")
    print("6. Add Account")
    print("7. Remove Account")
    print("8. Exit")

    choice = int(input("Enter Choice :"))

    if choice == 1 :
        show_acc()

    elif choice == 2 :
        name = input("Enter Name :")
        if name in accounts :
            print(f"Balance : {accounts.get(name)}")
        else :
            print("Account Not Found")

    elif choice == 3 :
        name = input("Enter Name :")
        if name in accounts :
            amount = int(input("Enter Amount :"))
            total = deposit(accounts.get(name),amount)
            print(f"Deposit : {total}")
            accounts[name] = total
        else :
            print("Account Not Found")

    elif choice == 4 :
        name = input("Enter Name :")
        if name in accounts :
            amount = int(input("Enter Amount :"))
            if accounts.get(name) > amount :
                remain = withdraw(accounts.get(name),amount)
                accounts[name] = remain
                print(f"Remaining Balance : {remain}")
            else :
                print("Insufficient Balance")

        else :
            print("Account Not Found")

    elif choice == 6 :
        name = input("Enter Name :")
        if name not in accounts :
            balance = int(input("Enter Initial Balance :"))
            accounts.update({name} , balance)
            print("Account Added")
        else :
            print("Account Already Exists")

    elif choice == 7 :
        name = input("Enter Name :")
        if name in accounts :
            accounts.pop(name)
            print("Account Removed")
        else :
            print("Account Already Exists")

    elif choice == 8 :
        print("Goodbye !")
        break


