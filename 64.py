even_total = 0
odd_total = 0
even_count = 0
odd_count = 0
for num in range(1,51) :
    if num % 3 == 0 :
        if num %2 == 0 :
            even_total= even_total + num
            even_count= even_count + 1
        else :
            odd_total= odd_total + num 
            odd_count= odd_count + 1
print(f"Even Total : {even_total}")
print(f"Odd Total : {odd_total}")
print(f"Even Count : {even_count}")
print(f"Odd Count : {odd_count}")