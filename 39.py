num = 1
while num<= 30 :
    if num == 7 :
        print(num)
        break
    elif num % 3 == 0 :
        num = num + 1
        continue
    else :
        print(num)
    num = num + 1