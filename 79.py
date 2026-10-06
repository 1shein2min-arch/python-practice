fail_count = 0
pass_count = 0
good_count = 0
excellent_count = 0
total = 0
count = 0
while True:
    mark = int(input("Enter Marks"))
    if mark == -1 :
        print("Exit")
        break
    elif mark < 0 :
        print("Invalid Mark")
        continue
    elif mark <= 100 :
        print("Valid")
    else :
        print("Invalid Mark")
        continue
    grade = int(input("Enter Grade"))
    if grade < 40 :
        print("Fail")
        fail_count = fail_count + 1
    elif grade < 60 :
        print("Pass")
        pass_count = pass_count + 1
    elif grade < 80 :
        print("Good")
        good_count = good_count + 1
    else :
        print("Excellent")
        excellent_count = excellent_count +1 
    total = total + mark
    count = count + 1
    print(f"Fail Count :{fail_count}")
    print(f"Pass Count : {pass_count}")
    print(f"Good Count : {good_count}")
    print(f"Excellent Count : {excellent_count}")
    print(f"Total : {total}")
    print(f"Count : {count}")
average = total/count
print(f"Average : {average}")
if average >= 80 :
    print("Excellent Class")
elif average >= 60 :
    print("Good Class")
elif average >= 40 :
    print("Pass Class")
else :
    print("Fail Class")
          
