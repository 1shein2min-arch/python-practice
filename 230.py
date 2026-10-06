accounts = {
    "Aung" : 500000,
    "Ko Ko" : 1200000,
    "Hla Hla":750000,
    "Su Su" : 1500000
}

def acc (name,balance) :
    print(f"{name} : {balance}")

def status(name,balance) :
    if balance >= 1000000 :
        print("VIP")
    else:
        print("Normal")

def total_money():
    total = 0
    for balance in accounts.values() :
        total = total + balance
    print(f"Total Money : {total}")

def highest() :
    highest_balance = 0
    highest_name = ""

    for name,balance in accounts.items() :
        if balance > highest_balance :
            highest_balance = balance
            highest_name = name
    print(f"Highest : {highest_name} : {highest_balance}")

print("===== Bank System =====")

print("Accounts :")
for name,balance in accounts.items() :
    acc(name,balance)

print("Status :")
for name,balance in accounts.items() :
    status(name,balance)

total_money()
 
print("Highest Balance :")
highest()