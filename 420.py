balance = 50000

def deposit() :
    global balance 
    balance = balance + 20000
    return balance


def withdraw() :
    global balance
    balance = balance - 15000
    return balance

print(f"Balance : {balance}")

print(f"After Deposit : {deposit()}")

print(f"After withdraw: {withdraw()}")