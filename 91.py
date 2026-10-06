numbers = []
even_numbers = []
odd_numbers = []

for num in range (1,6) :
    num = int(input("Enter Number"))
    numbers.append(num)

for num in numbers :
    if num % 2 == 0 :
        even_numbers.append(num)

    else :
        odd_numbers.append(num)

total = 0
for num in numbers :
    total = total + num
count = len(numbers)

average = total/count

highest = max(numbers)
lowest = min(numbers)

print(f"Numbers : {numbers}")
print(f"Even Numbers : {even_numbers}")
print(f"Odd Numbers : {odd_numbers}")

print(f"Total : {total}")
print(f"Average : {average}")
print(f"Highest : {highest}")
print(f"Lowest : {lowest}")
    