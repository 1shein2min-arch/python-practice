while True :
    username = input("Enter Username")
    if username == "q" :
        print("Exit")
        break
    elif username != "admin" :
        print("Wrong Username")
    else:
        password = int(input("Enter Password"))
        if password != 1234 :
            print("Wrong Password")
        else :
            print("Login Successful")