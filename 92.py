marks = []
fail_marks = []
pass_marks = []
excellent_marks = []

for num in range (5) :
    mark = int(input("Enter marks :"))
    marks.append(mark)

for mark in marks :
    if mark < 40 :
        fail_marks.append(mark)
    elif mark < 80 :
        pass_marks.append(mark)
    else :
        excellent_marks.append(mark)

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
print(f"Excellent Marks : {excellent_marks}")

print(f"Total : {total}")
print(f"Average : {average}")
print(f"Highest : {highest}")
print(f"Lowest : {lowest}")