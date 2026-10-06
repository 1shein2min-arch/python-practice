numbers = []
positive_num = []
negative_num = []
zero_num = []

for num in range (10) :
    num = int(input("Enter Numbers"))
    numbers.append(num)

for num in numbers :
    if num > 0 :
        positive_num.append(num)

    elif num < 0 :
        negative_num.append(num)

    else :
        zero_num.append(num)

positive_count = len(positive_num)
negative_count = len(negative_num)
zero_count = len(zero_num)

positive_total = 0
negative_total = 0
total = 0

for num in positive_num :
    positive_total = positive_total + num

for num in negative_num :
    negative_total = negative_total + num

for num in numbers :
    total = total + num

total_count = len(numbers)

average = total/total_count

highest = max(numbers)
lowest = min(numbers)

print(f"Numbers : {numbers}")
print(f"Positive Numbers : {positive_num}")
print(f"Negative Numbers : {negative_num}")
print(f"Zero Numbers : {zero_num}")
print(f"Positive Count : {positive_count}")
print(f"Negative Count : {negative_count}")
print(f"Zero Count : {zero_count}")
print(f"Positive Total : {positive_total}")
print(f"Negative Total : {negative_total}")
print(f"Total : {total}")

print(f"Average : {average}")
print(f"Highest : {highest}")
print(f"Lowest : {lowest}")

if average >= 50 :
    print("Good Numbers")
elif average >= 0 :
    print("Normal Numbers")
else :
    print("Negative Numbers")


    


