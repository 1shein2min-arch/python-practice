customer = "Aung"
balance = 50000

def after_payment() :
    global balance 
    balance = balance - 20000

after_payment()

print(f"Customer : {customer}")
print(f"Balance : {balance}")