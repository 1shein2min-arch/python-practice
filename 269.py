while True :
    try :
        age = int(input("Enter Age :"))

        if age >= 18 :
            print("Adult") 

        else :
            print("Child")

    except ValueError :
        print("Please Enter a Vaild age")