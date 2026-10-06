low_salary = 0
medium_salary = 0
large_salary = 0
low_count = 0
medium_count = 0
large_count = 0
total = 0
count = 0
while True :
    name = input("Enter Employee Name")
    length = len(name)
    if length < 4 :
        print("Name Too Short")
    elif length < 10 : 
        print("Valid Name")
    else :
        print("Name Too Long")
    
    salary = int(input("Enter Salary"))
    if salary == -1 :
        print("Exit")
        break
    if salary < 0 :
        print("Invalid Salary")
        continue
    elif salary == 0 :
        print("Invalid Salary")
        continue
    else :
        if salary < 300000 :
            bonus = salary * 0.05
            low_salary = low_salary + salary
            low_count = low_count + 1
        elif salary < 50000 :
            bonus = salary * 0.1
            medium_salary = medium_salary + salary
            medium_count = medium_count + 1
        else :
            bonus = salary * 0.2
            large_salary = large_salary + salary
            large_count = large_count + 1

        final_salary = salary + bonus
    print(f"Salary : {salary}")
    print(f"Bonus : {bonus}")
    print(f"Final Salary :{final_salary}")


    total = total + final_salary
    count = count + 1
    
    print(f"Total final Salary {total}")
    print (f"Employee Count : {count}")
    average = total/count
    if average < 300000 :
        print("Low Average")
    elif average <500000 :
        print("Normal Average")
    else :
        print("High Average")




   
