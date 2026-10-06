num = 1
while num <= 50 :
    if num == 25 :
        print(num)
        break
    elif num % 4 == 0 :
        num = num + 1 
        continue
    elif num % 3 == 0:
        print(f"{num} - Three")
    elif num % 2 == 0:
        print(f"{num} - Even")
    else:
        print(f"{num} -Other")
    num = num + 1