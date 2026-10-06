total = 0
count = 0
for num in range (1,51) :
    if num % 3 ==0 :
        total = total + num
        count = count + 1
average = total/count
print(f"Total {total}")
print(f"Count {count}")
print(f"average {average}")