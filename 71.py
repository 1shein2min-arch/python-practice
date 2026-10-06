while True:

    username = input("Enter Username: ")

    if username != "admin":
        print("Wrong Username")

    else:
        password = input("Enter Password: ")
        length = len(password)

        if password != "python123":
            print("Wrong Password")

        elif length < 6:
            print("Password Too Short")

        else:
            print("Login Successful")

            total = 0
            count = 0

            for num in range(1, 6):

                mark = int(input("Enter Mark: "))

                if mark < 0 or mark > 100:
                    print("Invalid Mark")

                elif mark < 40:
                    print("Fail")
                    total = total + mark
                    count = count + 1

                elif mark < 60:
                    print("Pass")
                    total = total + mark
                    count = count + 1

                elif mark < 80:
                    print("Good")
                    total = total + mark
                    count = count + 1

                else:
                    print("Excellent")
                    total = total + mark
                    count = count + 1

            print(f"Total: {total}")
            print(f"Count: {count}")

            average = total / count

            print(f"Average: {average}")

            if average < 40:
                print("Failed")

            elif average < 60:
                print("Passed")

            elif average < 80:
                print("Good Student")

            else:
                print("Excellent Student")

    again = input("Do you want to login again? (yes/no): ").lower()

    if again == "yes":
        continue

    elif again == "no":
        print("Goodbye")
        break

    else:
        print("Invalid Choice")