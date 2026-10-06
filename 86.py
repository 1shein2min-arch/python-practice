low_count = 0
normal_count = 0
high_count = 0

total = 0
count = 0
while True :
    name = input("Enter Employee Name :").lower()
    if name == "exit" :
        print("Exit")
        break
    else :
        length = len(name)
        if length < 3 :
            print("Name Too Short")
            continue
    salary = int(input("Enter Salary :"))
    if salary <= 0 :
        print("Invalid Salary")
        continue
    elif salary < 300000 :
        bonus = salary * 0.05  
        low_count = low_count + 1
    elif salary < 500000 :
        bonus = salary * 0.1
        normal_count = normal_count + 1
    else :
        bonus = salary * 0.15
        high_count = high_count + 1

    final_salary = salary + bonus

    total = total + final_salary
    count = count + 1

    print(f"Name = {name}")
    print(f"Salary = {salary}")
    print(f"Bonus = {bonus}")
    print(f"Final Salary = {final_salary}")

if count > 0 :
    average = total/count
    if average >= 500000 :
        print("Hige Salary Company")

    elif average >= 300000 :
        print("Normal Salary Company")

    else :
        print("Low Salary Company")

print(f"Low Count : {low_count}")
print(f"Normal Count : {normal_count}")
print(f"High Count : {high_count}")

print(f"Total Salary : {total}")
print(f"Employee Count : {count}")
print(f"Average Final Salary : {average}")








