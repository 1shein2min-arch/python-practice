marks = []
fail_marks = []
pass_marks = []
good_marks = []
excellent_marks = []

for num in range (8) :
    mark = int(input("Enter Marks"))
    marks.append(mark)

for mark in marks :
    if mark < 40 :
        fail_marks.append(mark)

    elif mark < 60 :
        pass_marks.append(mark)

    elif mark < 80 :
        good_marks.append(mark)

    else :
        excellent_marks.append(mark)

fail_count = len(fail_marks)
pass_count = len(pass_marks)
good_count = len(good_marks)
excellent_count = len(excellent_marks)

total = 0
for mark in marks :
    total = total + mark

count = len(marks)
average = total/count

highest = max(marks)
lowest = min(marks)


print(f"Marks : {marks}")
print(f"Fail Marks : {fail_marks}")
print(f"Pass Marks : {pass_marks}")
print(f"Good Marks : {good_marks}")
print(f"Excellent Marks : {excellent_marks}")

print(f"Fail Count : {fail_count}")
print(f"Pass Count : {pass_count}")
print(f"Good Count : {good_count}")
print(f"Excellent Count : {excellent_count}")

print(f"Total : {total}")
print(f"Average : {average}")
print(f"Highest : {highest}")
print(f"Lowest : {lowest}")

if average >= 80 :
    print("Excellent Class")
elif average >= 60 :
    print("Good Class")
elif average >= 40 :
    print("Pass Class")
else :
    print("Fail Class")