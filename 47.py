while True :
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    choice = input("Choose")
    if choice == "1" :
        print("Balace: 1000 ")
    elif choice == "2" :
        print("Deposit Selected")
    elif choice == "3" :
        print("Withdraw Selected")
    elif choice == "4" :
        print("Goodbye")
        break
    elif choice == "0" :
        continue 
    else :
        print("Invalid Choice")