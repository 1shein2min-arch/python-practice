while True :
    num = int(input("Enter Number"))
    if num == 0 :
        print("Exit")
        break
    elif num == 10:
        print("Ten")
    elif num % 3 == 0 :
        continue
    elif num % 2 == 0 :
        print("Even")
    else :
        print("odd")
    
