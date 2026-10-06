def get_non_empty_text(message):
    while True :
        customer = input(message).strip()
        if customer == "" :
            print("Input Cannot Be Empty")
            continue
        break
    return customer
        

customer = get_non_empty_text("Enter Customer Name :")
