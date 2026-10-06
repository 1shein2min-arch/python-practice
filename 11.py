amount = int(input("Enter amount"))
if amount<=0 :
    print("invalid amount")
elif amount<=1000:
    print("Withdrawl Successful")
else:
    print("Insufficient Balance")