username = input("Enter Username")
if username !=  "admin" :
    print("Username not found")
else:
    password = int(input("Enter password"))
    if password != "python123":
        print("Wrong Password")
    else:
        print("Login successful")