num = int(input("Enter Number"))

while num >= 1:
    if num != 7:
        if num % 2 == 0:
            print(f"{num} - Even")
        else:
            print(f"{num} - Odd")

    num = num - 1