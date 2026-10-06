marks = []
fail_marks = []
pass_marks = []
good_marks = []
excellent_marks = []

for num in range (10) :
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

marks_count = len(marks)
fail_count = len(fail_marks)
pass_count = len(pass_marks)
good_count = len(good_marks)
excellent_count = len(excellent_marks)

total = 0
fail_total = 0
pass_total = 0
good_total = 0
excellent_total = 0

for mark in marks :
    total = total + mark

for mark in fail_marks :
    fail_total = fail_total + mark

for mark in pass_marks :
    pass_total = pass_total + mark

for mark in good_marks :
    good_total = good_total + mark

for mark in excellent_marks :
    excellent_total = excellent_total + mark

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

print(f"Fail Total : {fail_total}")
print(f"Pass Total : {pass_total}")
print(f"Good Total : {good_total}")
print(f"Excellent Total : {excellent_total}")

print(f"Total : {total}")
print(f"Average : {average}")
print(f"Highest : {highest}")
print(f"Lowest : {lowest}")

if fail_total > pass_total and fail_total > good_total and fail_total > excellent_total :
    print("Highest Category : Fail ")

elif pass_total > fail_total and pass_total > good_total and pass_total > excellent_total :
    print("Highest Category : Pass")

elif good_total > fail_total and good_total > pass_total and good_total > excellent_total :
    print("Highest Category : Good")

else :
    print("Highest Category : Excellent")

if average >= 80 :
    print("Excellent Class")

elif average >= 60 :
    print("Good Class")

elif average >= 40 :
    print("Pass Class")

else :
    print("Fail Class")




