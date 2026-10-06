print("1. Calculate Salary")
print("2. Exit")

while True:

    try:
        choice = int(input("Enter Choose :"))

        if choice == 1:

            try:
                salary = int(input("Enter Salary :"))
                bonus = int(input("Enter Bonus :"))

                total = salary + bonus

                print(f"Total Salary : {total}")

                if total >= 1000000:
                    print("High Salary")
                else:
                    print("Normal Salary")

            except ValueError:
                print("Please Enter A Valid Salary or Bonus")

        elif choice == 2:
            print("Goodbye !")
            break

        else:
            print("Invalid Choice")

    except ValueError:
        print("Please Enter A Valid Choice")