low_count = 0
normal_count = 0
high_count = 0
total = 0
employee_count = 0
while True :
    salary = int(input("Enter Salary"))
    if salary == -1 :
        print("Exit")
        break
    elif salary < 0 :
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

    print(f"Salary = {salary}")
    print(f"Bonus = {bonus}")
    print(f"Final Salary = {final_salary}")
    total = total + final_salary
    employee_count = employee_count + 1

average = total/employee_count

print(f"Low Count : {low_count}")
print(f"Normal Count : {normal_count}")
print(f"High Count : {high_count}")

print(f"Total Final Salary : {total}")
print(f"Employee Count : {employee_count}")
print(f"Average Final Salary : {average}")

if average >= 500000 :
    print("High Salary Average")
elif average >= 300000 :
    print("Normal Salary Average")
else :
    print("Low Salary Average")
     
        
    