balance = 1000 
while True :
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    choice = input("Choose")
    if choice == "1":
        print(balance)
    elif choice == "2" :
        deposit = int(input("Enter Deposit"))
        balance = balance + deposit
        print(balance)
    elif choice == "3" :
        withdraw = int(input("Enter Withdraw"))
        balance = balance - withdraw
        if withdraw > balance :
            print("Not Enough Balance")
        else:
            print(balance)
    elif choice == "4" :
        print("Goodbye")
        break
    elif choice == "0" :
        continue
    else :
        print("Invalid Choose")