accounts = {
    "Aung": 500000,
    "Ko Ko": 1200000,
    "Hla Hla": 750000,
    "Su Su": 1500000
}
def show_acc () :
    for name,balance in accounts.items() :
        print(f"{name} : {balance}")

def check_bal () :
    name = input("Enter Name :")
    if name in accounts :
        print(f"Balance : {accounts.get(name)}")
    else :
        print("Account Not Found")

def deposit(balance,amount) :
    return balance + amount

def add_acc() :
    name = input("Enter Name :")
    if name not in accounts :
        amount = int(input("Enter Initial Balance :"))
        accounts[name] = amount
        print("Account Added")
    else :
        print("Account Already Exists")

def remove_acc() :
    name = input("Enter Name :")
    if name in accounts :
        accounts.pop(name)
        print("Account Removed")
    else :
        print("Account Not Found")

def show_exit() :
    print("Goodbye !")

while True :
    print("1. Show Accounts")
    print("2. Check Balance")
    print("3. Deposit")
    print("4. Add Account")
    print("5. Remove Account")
    print("6. Exit")

    choice = int(input("Enter Choose :"))
    
    if choice == 0 :
        print("Skiped")
        continue
    
    elif choice == 1 :
        show_acc() 

    elif choice == 2 :
        check_bal()

    elif choice == 3 :
        name = input("Enter Name :")
        if name in accounts :
            amount = int(input("Enter Deposit Amount :"))
            total = deposit(accounts.get(name),amount)
            accounts[name] = total
        else :
            print("Account Not Found")

    elif choice == 4 :
        add_acc()

    elif choice == 5 :
        remove_acc()

    elif choice == 6 :
        show_exit()
        break

    else :
        print("Invalid Choice")