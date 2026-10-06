accounts = {
    "Aung" : 500000,
    "Ko Ko" : 1200000,
    "Hla Hla" : 750000
}
def acc() :
    print("Accounts :")
    for name,balance in accounts.items() :
        print(f"{name} : {balance}")

def status() :
    print("Account Status :")
    for name,balance in accounts.items() :
        if balance >= 1000000 :
            print(f"{name} : VIP")
        else :
            print(f"{name} : Normal")

def vip() :
    print("VIP Accounts :")
    for name,balance in accounts.items() :
        if balance >= 1000000 :
            print(name)

def normal() :
    print("Normal Accounts :")
    for name,balance in accounts.items() :
        if balance < 1000000 :
            print(name)

def totals() :
    total = 0
    for balance in accounts.values() :
        total = total + balance 
    print(f"Total Money : {total}")

def total_acc() :
    print(f"Total Accounts : {len(accounts)}")

def highest() :
    highest_balance = 0 
    highest_name = ""
    for name,balance in accounts.items() :
        if balance > highest_balance :
            highest_balance = balance
            highest_name = name
    print("Highest :")
    print(f"{highest_name} : {highest_balance}")

def lowest() :
    lowest_balance = 9999999
    lowest_name = ""
    for name,balance in accounts.items() :
        if balance < lowest_balance :
            lowest_balance = balance
            lowest_name = name
    print("Lowest :")
    print(f"{lowest_name} : {lowest_balance}")

def sorted() :
    names = []
    for name in accounts.keys() :
        names.append(name)
    names.sort()
    print("Sorted Names :")
    print(names)

print("===== Bank Information =====")

acc() 

status()

vip()

normal()

totals()

total_acc()

highest()

lowest()

sorted()