for num in range(1,51) :
    if num % 3 ==0 and num % 2 == 0 :
        print(f"{num} - Three Even")
    elif num % 3 == 0 :
        print(f"{num} - Three Odd")
    elif num % 2 == 0 :
        print(f"{num} - Even")
    else :
        print(f"{num} - Other")
    
