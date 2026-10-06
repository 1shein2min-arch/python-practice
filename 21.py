pin = int(input("Enter pin"))
if pin != 1234:
    print("Invalid Pin")
else:
    balance = int(input("Enter balance"))
    if balance >= 100000:
        print("Vip Customer")
    elif balance >=10000:
        print("Withdrawal Allowed")
    else:
        print("Insufficient Balance")