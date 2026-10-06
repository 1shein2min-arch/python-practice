def new_repair() :
    name = input("Enter Name :")
    model = input("Enter Phone :")
    while True :
        try :
            fee = int(input("Enter Fee :"))
            if fee <= 0 :
                print("Fee Must Be Greater Than 0")
                continue
            break

        except ValueError :
            print("Please Enter Number")

    while True :
        status = input("Enter Status :").lower()
        if status != "done" and status != "pending" :
            print("Invalid Status")
            continue
        break


