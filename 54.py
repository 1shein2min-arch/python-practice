while True :
    price = int(input("Enter Price"))
    if price== 0 :
        print("Exit")
        break
    elif price < 100 :
        discount = 0
        print(f"Discount:{discount}")
        final_price = price - discount
        print(f"Final Price: {final_price}")
        break
    elif price < 500 :
        discount = price * 0.1
        print(f"Discount:{discount}")
        final_price = price - discount
        print(f"Final Price: {final_price}")
        break
    elif price < 1000 :
        discount = price *0.2
        print(f"Discount:{discount}")
        final_price = price - discount
        print(f"Final Price: {final_price}")
        break
    else :
        discount = price * 0.3
        print(f"Discount:{discount}")
        final_price = price - discount
        print(f"Final Price: {final_price}")
        break