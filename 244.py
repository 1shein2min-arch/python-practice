accounts = {
    "Aung": 500000,
    "Ko Ko": 1200000,
    "Hla Hla": 750000,
    "Su Su": 1500000
}
def acc() :
    for name,balance in accounts.items() :
        print(f"{name} : {balance}")

def deposit(balance,amount) :
    return balance + amount

print("===== Bank Deposit =====")

acc()

name = input("Enter Account :")
if name in accounts :
    amount = int(input("Enter Deposit Amount :"))
    total = deposit(accounts.get(name),amount)

    print(f"Deposit : {amount}")
    print(f"New Balance : {total}")
    if total >= 1000000:
        print("Status : VIP")
    else :
        print("Status : Normal")

else :
    print("Account Not Found")