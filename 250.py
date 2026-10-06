accounts = {
    "Aung": 500000,
    "Ko Ko": 1200000,
    "Hla Hla": 750000,
    "Su Su": 1500000
}
def show_acc():
    for name,balance in accounts.items() :
        print(f"{name} : {balance}")

def show_bal() :
    for balance in accounts.values() :
        print(f"{balance}")

def show_exit() :
    print("Goodbye!")

while True :
    print("===== Bank System =====")

    print("1. Show Accounts")
    print("2. Check Balance")
    print("3. Exit")

    choice = int(input("Enter Choose :"))

    if choice == 1 :
        show_acc()

    elif choice == 2 :
        show_bal()

    elif choice == 3 :
        show_exit()
        break

    else :
        print("Invalid Choice")