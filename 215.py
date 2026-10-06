accounts = {
    "Aung": 500000,
    "Ko Ko": 1200000,
    "Hla Hla": 750000,
    "Mg Mg": 300000,
    "Su Su": 1500000
}


def show_account():
    print("Accounts :")

    for name, balance in accounts.items():
        print(f"{name} : {balance}")


def add_account():
    name = input("Enter Name : ")

    if name not in accounts:
        balance = int(input("Enter Balance : "))
        accounts.update({name: balance})
        print(f"{name} Added")
    else:
        print("Account Already Exists")


def update_balance():
    name = input("Enter Name : ")

    if name in accounts:
        balance = int(input("Enter New Balance : "))
        accounts.update({name: balance})
        print(f"{name} Updated")
    else:
        print("Account Not Found")


def remove_account():
    name = input("Enter Name : ")

    if name in accounts:
        accounts.pop(name)
        print(f"{name} Removed")
    else:
        print("Account Not Found")


def check_balance():
    name = input("Enter Name : ")

    if name in accounts:
        print(f"{name} : {accounts.get(name)}")
    else:
        print("Account Not Found")


def vip_account():
    print("VIP Accounts :")

    for name, balance in accounts.items():
        if balance >= 1000000:
            print(name)


def normal_account():
    print("Normal Accounts :")

    for name, balance in accounts.items():
        if balance < 1000000:
            print(name)


def highest():
    highest_balance = 0
    highest_name = ""

    for name, balance in accounts.items():
        if balance > highest_balance:
            highest_balance = balance
            highest_name = name

    print("Highest :")
    print(f"{highest_name} : {highest_balance}")


def lowest():
    lowest_balance = 9999999
    lowest_name = ""

    for name, balance in accounts.items():
        if balance < lowest_balance:
            lowest_balance = balance
            lowest_name = name

    print("Lowest :")
    print(f"{lowest_name} : {lowest_balance}")


def total_money():
    total = 0

    for balance in accounts.values():
        total = total + balance

    print(f"Total Money : {total}")


def total_account():
    print(f"Total Accounts : {len(accounts)}")


def sorted_name():
    names = []

    for name in accounts.keys():
        names.append(name)

    names.sort()

    print("Sorted Names :")
    print(names)


def goodbye():
    print("Goodbye!")


while True:

    print()
    print("===== Bank Management =====")

    print("1. Show Accounts")
    print("2. Add Account")
    print("3. Update Balance")
    print("4. Remove Account")
    print("5. Check Balance")
    print("6. Show VIP Accounts")
    print("7. Show Normal Accounts")
    print("8. Show Highest Balance")
    print("9. Show Lowest Balance")
    print("10. Total Money")
    print("11. Total Accounts")
    print("12. Sorted Names")
    print("13. Exit")

    choice = int(input("Enter Choose : "))

    if choice == 1:
        show_account()

    elif choice == 2:
        add_account()

    elif choice == 3:
        update_balance()

    elif choice == 4:
        remove_account()

    elif choice == 5:
        check_balance()

    elif choice == 6:
        vip_account()

    elif choice == 7:
        normal_account()

    elif choice == 8:
        highest()

    elif choice == 9:
        lowest()

    elif choice == 10:
        total_money()

    elif choice == 11:
        total_account()

    elif choice == 12:
        sorted_name()

    elif choice == 13:
        goodbye()
        break

    else:
        print("Invalid Choice")