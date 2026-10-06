def get_positive_number () :
    while True :
        try :
            fee = int(input("Enter Fee :"))
            if fee <= 0 :
                print("Fee Must Be Greater Than 0")
                continue
            break
        except ValueError :
            print("Please Enter Number")

    return fee