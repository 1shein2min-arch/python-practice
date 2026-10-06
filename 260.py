accounts = {
    "Aung": 500000,
    "Ko Ko": 1200000,
    "Hla Hla": 750000,
    "Su Su": 1500000
}

def show_acc() :
    for name,balance in accounts.items() :
        print(f"{name} : {balance}")

def check_bal() :
    name = input("Enter Name :")
    if name in accounts :
        print(accounts.get(name))

    else :
        print("Account Not Found")

def deposit(balance,amount) :
    return balance + amount
    
def withdraw () :
    name = input("Enter Name :")
    if name in accounts :
        old_balance = accounts.get(name)
        withdraw = int(input("Enter Withdraw :"))
        if withdraw > old_balance :
            print("Insufficient Balance")
        else :
            remain = old_balance - withdraw
            accounts[name] = remain
            
            print(f"Old Balance : {old_balance}")
            print(f"Withdraw : {withdraw}")
            print(f"New Balance : {remain}")
    else :
        print("Account Not Found")

def can_transfer () :
    sender = input("Enter From Account :")
    if sender in accounts :
        old_balance = accounts.get(sender)
        receiver = input("Enter To Account :")
        if receiver in accounts :
            old_balance2 = accounts.get(receiver)
            amount = int(input("Enter Amount :"))
            if amount < old_balance :
                transfer = old_balance - amount
                receive = old_balance2 + amount

                accounts[sender] = transfer
                accounts[receiver] = receive

                print(f"{sender} New Balance : {transfer}")
                print(f"{receiver} New Balance : {receive}")
            else :
                print("Insufficient Balance")
        else :
            print("Receiver Account Not Found")

    else :
        print("Sender Account Not Found")

def add_acc() :
    name = input("Enter Name :")
    if name not in accounts :
        balance = int(input("Enter Initial Balance :"))
        accounts[name] = balance
        print("Account Added")
    else :
        print("Account Already Exists")

def remove_acc() :
    name = input("Enter Name :")
    if name in accounts :
        accounts.pop(name)
        print("Account Removed")
    else:
        print("Account Not Found")

def goodbye() :
    print("Goodbye !")

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

    choice = int(input("Enter Choose :"))

    if choice == 1 :
        show_acc()

    elif choice == 2 :
        check_bal()

    elif choice == 3 :
        name = input("Enter Name :")
        if name in accounts :
            balance = accounts.get(name)
            amount = int(input("Enter Deposit :"))
            total = deposit(balance,amount)
            accounts[name] = total

            print(f"Old Balance : {balance}")
            print(f"Deposit : {amount}")
            print(f"New Balance : {total}")

        else :
            print("Account Not Found")

    elif choice == 4 :
        withdraw()

    elif choice == 5 :
        can_transfer()

    elif choice == 6 :
        add_acc()

    elif choice == 7 :
        remove_acc()

    elif choice == 8 :
        goodbye()
        break

    else :
        print("Invalid Choice")





