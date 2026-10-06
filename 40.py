num = 1
while num <= 50 :
    if num % 5 == 0 :
        num = num + 1
        continue
    elif num == 20 :
        break
    else:
        if num % 2 == 0 :
            print(num)
    num = num + 1
    
