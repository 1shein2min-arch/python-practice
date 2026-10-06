while True:

    name = input("Enter Name: ")
    length = len(name)

    if length < 4:
        print("Name Too Short")
    elif length <= 10:
        print("Valid Name")
    else:
        print("Name Too Long")

    total = 0
    count = 0

    for num in range(1, 6):

        marks = int(input("Enter Mark: "))

        if marks < 0 or marks > 100:
            print("Invalid Mark")

        elif marks < 40:
            print("Fail")
            total = total + marks
            count = count + 1

        elif marks < 60:
            print("Pass")
            total = total + marks
            count = count + 1

        elif marks < 80:
            print("Good")
            total = total + marks
            count = count + 1

        else:
            print("Excellent")
            total = total + marks
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

    again = input("Do you want to try again? (yes/no): ").lower()

    if again == "no":
        print("Goodbye")
        break
    elif again == "yes":
        continue
    else:
        print("Invalid Choice")