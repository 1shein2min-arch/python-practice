username = input("Enter username")
length = len(username)
if length < 4 :
    print("Too 'Short")
elif length <= 10 :
    print("Valid Username")
else :
    print("Too Long")
