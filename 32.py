num = 1
while num <= 30 :
    if num % 3 == 0 and num % 5 == 0 :
        print(f"{num} - Three Five")
    elif num % 3 == 0 :
        print(f"{num} - Three")
    elif num % 5 == 0 :
        print(f"{num} - Five")
    else :
        print(f"{num} - Other")
    num = num + 2