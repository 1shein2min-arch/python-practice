def get_positive_num (message) :
    while True:
        try: 
            part_fee = int(input(message))
            if part_fee < 0 :
                print("Number Cannot Be Negative")
                continue
            break
        except ValueError :
            print("Please Enter A Number")
    return part_fee

parts_fee = get_positive_num("Enter Fee :")
