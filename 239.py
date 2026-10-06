accounts = {
    "Aung": 500000,
    "Ko Ko": 1200000,
    "Hla Hla": 750000,
    "Su Su": 1500000
}

def acc() :
    for name,balance in accounts.items() :
        print(f"{name} : {balance}")

def total(balance,withdraw) :
    return balance - withdraw

print("===== Bank Withdrawal =====")

print("Accounts :")
acc()

name = input("Enter Name :")
if name in accounts :
    amount = int(input("Enter Withdraw Amount :"))
    if amount <= accounts.get(name) :
        result = total(accounts.get(name),amount)
        print(f"Withdraw : {amount}")
        print(f"New Balance : {result}")

    else :
        print("Insufficient Balance")

else :
    print("Account Not Found")