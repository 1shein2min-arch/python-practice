balance = 1000
correct_pin = "1234"

pin = input("Enter your 4-digit PIN: ")

if pin != correct_pin:
    print("Incorrect PIN. Access Denied!")
else:
    print("\n--- Welcome to Mini Bank ---")
    print("1. Check Balance")
    print("2. Withdraw")
    print("3. Deposit")
    
    choice = int(input("Enter choice (1-3): "))

    # choice တွေကို elif နဲ့ စနစ်တကျ ချိတ်ပေးလိုက်ပါမယ်
    if choice == 1:
        print(f"Current Balance: ${balance}")
        
    elif choice == 2:
        amount = int(input("Enter amount to withdraw: "))
        if amount <= 0:
            print("Invalid Amount")
        elif amount > balance:
            print("Insufficient Balance")
        else:
            remain_balance = balance - amount
            print(f"Withdrawal Successful! Remaining Balance: ${remain_balance}")
            
    elif choice == 3:
        amount = int(input("Enter amount to deposit: "))
        if amount <= 0:
            print("Invalid Amount")
        else:
            remain_balance = balance + amount
            print(f"Deposit Successful! Total Balance: ${remain_balance}")
            
    else:  # 1, 2, 3 မဟုတ်တဲ့ choice မှန်သမျှကို ဒီမှာ တန်းဖမ်းလိုက်ပါမယ်
        print("Invalid Choice")