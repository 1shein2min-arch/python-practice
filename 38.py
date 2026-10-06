num = 1
while num <= 3 :
    password = input("Enter password :")
    if password != "python123":
        print("Wrong Password")
    else :
        print("Login Successful")
        break
    num = num + 1