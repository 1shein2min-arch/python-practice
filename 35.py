num = 30
while num >= 1:
    if num % 4 == 0 and num % 3 ==0 :
        print(f"{num} - FourThree")
    elif num % 4 == 0:
        print(f"{num} - Four")
    elif num % 3 == 0 :
        print(f"{num} - Three")
    else :
        print(f"{num} - other")
    num = num - 1