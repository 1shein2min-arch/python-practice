even_total = 0
even_count = 0
odd_total = 0
odd_count = 0
for num in range(1,101) :
    if num % 3 == 0 :
        if num % 2 == 0 :
            even_total = even_total + num
            even_count = even_count + 1
        else :
            odd_total = odd_total + num
            odd_count = odd_count + 1 
even_average = even_total/even_count
print(f"Even Total {even_total}")
print(f"Even Count {even_count}")
print(f"Even Average {even_average}")

odd_average = odd_total/odd_count
print(f"Odd Total {odd_total}")
print(f"Odd Count {odd_count}")
print(f"Odd Average {odd_average}")
if even_average > odd_average :
    print("Even Average is Higher")
else :
    print("Odd Average is Higher")
