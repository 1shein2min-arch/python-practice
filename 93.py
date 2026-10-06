number = []
positive_number = []
negative_number = []
zero_number = []

for num in range (7) :
    num = int(input("Enter Number"))
    number.append(num)

for num in number :
    if num > 0 :
        positive_number.append(num)
        positive_count = len(positive_number)
    elif num < 0 :
        negative_number.append(num)
        negative_count = len(negative_number)
    else :
        zero_number.append(num)
        zero_count = len(zero_number)

total =0
for num in number :
    total = total + num

count = len(number)

average = total/count

print(f"Number :{number}")
print(f"Positive Number : {positive_number}")
print(f"Negative Number : {negative_number}")
print(f"Zero Number :{zero_number}")
print(f"Positive Count :{positive_count}")
print(f"Negative Count : {negative_count}")
print(f"Zero Count : {zero_count}")
print(f"Total : {total}")
print(f"Average : {average}")