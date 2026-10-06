accounts = {
    "Aung": 500000,
    "Ko Ko": 1200000,
    "Hla Hla": 750000,
    "Mg Mg": 300000,
    "Su Su": 1500000
}
def show_accounts(name,balance) :
    print(f"{name} : {balance}")

def status(name,balance) :
    if balance >= 1200000 :
        print(f"{name} : VIP")
    else :
        print(f"{name} : Normal")

def vip(name,balance) :
    if balance >= 1200000 :
        print(name)

def normal(name,balance) :
    if balance < 1200000 :
        print(name)
def details(name,balance) :
    print(f"{name} Balance : {balance}")

def total(balance) :
    total = 0
    for balance in accounts.values() :
        total = total + balance
    print(f"Total Balance : {total}")

print("===== Bank Account =====")

print("Accounts :")
for name,balance in accounts.items() :
    show_accounts(name,balance)


print("===== Account Status =====")
for name,balance in accounts.items() :
    status(name,balance)

print("===== Vip Accounts =====")
for name,balance in accounts.items() :
    vip(name,balance)

print("===== Normal Accounts =====")
for name,balance in accounts.items() :
    normal(name,balance)

print("===== Account Details =====")
for name,balance in accounts.items() :
    details(name,balance)

print("===== Total Money =====")
total(balance)