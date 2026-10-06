numbers = []
even_num = []
odd_num = []

for num in range (10) :
    num = int(input("Enter Number"))
    numbers.append(num)

for num in numbers :
    if num % 2 == 0 :
        even_num.append(num)

    else :
        odd_num.append(num)

even_count = len(even_num)
odd_count = len(odd_num)

even_total = 0
odd_total = 0

for num in even_num :
     even_total = even_total + num
for num in odd_num :
     odd_total = odd_total + num

even_average = even_total/even_count
odd_average = odd_total/odd_count

highest = max(numbers)
lowest = min(numbers)

print(f"Even Number : {even_num}")
print(f"Odd Number : {odd_num}")
print(f"Even Count : {even_count}")
print(f"Odd Count : {odd_count}")
print(f"Even Total : {even_total}")
print(f"Odd Total : {odd_total}")
print(f"Even Average : {even_average}")
print(f"Odd Average : {odd_average}")
print(f"Highest Number : {highest}")
print(f"Lowest Number : {lowest}")

if even_average > odd_average :
    print("Even Average is Higher")

elif even_average < odd_average :
    print("Odd Average is Higher")

else :
    print("Both Average are Equal")

