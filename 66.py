total = 0
count = 0 
for num in range(1,101) :
    if num % 4 == 0 :
        total = total + num
        count = count + 1
average = total/count
print(f"Total {total}")
print(f"Count {count}")
print(f"Average {average}")
if average > 20 :
    print("Average is High")
else :
    print("Average is low")
