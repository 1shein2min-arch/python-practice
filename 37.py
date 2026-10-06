num = int(input("Enter Number"))

while num >= 1:
    if num != 7 :
        if num % 3 == 0 and num % 2 == 0 :
            print(f"{num} - Three Two")
        elif num % 3 == 0:
            print(f"{num} - Three")
        elif num % 2 == 0 :
            print(f"{num} -Two")
        else :
            print(f"{num} - other")
    num = num - 1
