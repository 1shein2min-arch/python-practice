number = int(input("Enter number"))
num = 1
while num <= number :
    if num % 2 == 0 and num % 3 == 0 :
        print(f"{num} - Even Three")
    elif num % 2 == 0 :
        print(f"{num} - Even")
    elif num % 3 == 0 :
        print(f"{num} - Three")
    else:
        print(num)
    num = num + 1