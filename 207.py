accounts = {
    "Aung" : 500000 ,
    "Ko Ko" : 300000 ,
    "Hla Hla" : 800000
}
while True :
    print("===== Bank Menu =====")
    print("1. Show Accounts")
    print("2. Add Account")
    print("3. Update Balance")
    print("4. Remove Account")
    print("5. Check Balance")
    print("6. Total Money")
    print("7. Exit")

    choice = int(input("Enter Choose :"))

    if choice == 1 :
        for name,balance in accounts.items() :
            print(f"{name} : {balance}")

    elif choice == 2 :
        name = input("Enter Name :")
        balance = int(input("Enter Balance :"))
        accounts.update({name : balance})
        print(f"{name} Added")

    elif choice == 3 :
        name = input("Enter Name :")
        if name in accounts :
            new_balance = int(input("Enter New Balance :"))
            accounts.update({name : new_balance})
            print(f"{name} Updated")

    elif choice == 4 :
        name = input("Enter Name :")
        if name in accounts :
            accounts.pop(name)
            print(f"{name} Removed")

    elif choice == 5 :
        name = input("Enter Name")
        if name in accounts :
            print(f"{name} : {accounts.get(name)}")

    elif choice == 6 :
        total = 0
        for balance in accounts.values() :
            total = total + balance
        print(f"Total Money : {total}")

    elif choice == 7 :
        print("GoodBye!")
        break


    


