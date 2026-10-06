balance = 10000

def check_balance () :
    print(balance)

def deposit_money () :
    amount = int(input("Enter Amount :"))
    total_balance = balance + amount
    print(f"Total Balance : {total_balance}")

def withdraw_money () :
    amount = int(input("Enter Amount :"))
    remain_balance = balance - amount
    print(f"Remaining Balance : {remain_balance}")

def goodbye() :
    print("Thank you for using ATM!")

while True :
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = int(input("Enter Choose :"))

    if choice == 1 :
        check_balance()

    elif choice == 2 :
        deposit_money()

    elif choice == 3 :
        withdraw_money()

    elif choice == 4 :
        goodbye()
        break