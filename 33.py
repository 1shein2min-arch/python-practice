limit = int(input("Enter number"))
num = 1 
while num <= limit :
    if num % 3 == 0 and num % 5 == 0 :
        print(f"{num} - Three Five")
    elif num % 5 == 0 :
        print(f"{num} - Five")
    elif num % 3 == 0 :
        print(f"{num} - Three")
    else :
        print(f"{num} - other")
    num = num + 1
    