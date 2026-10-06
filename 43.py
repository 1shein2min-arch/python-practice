while True :
    num = int(input("Enter Number"))
    if num == 0 :
        print("Exit")
        break
    elif num % 5 == 0 :
        num = num +1 
        continue
    elif num % 2 == 0 :
        print("Even")
    else :
        print("odd")