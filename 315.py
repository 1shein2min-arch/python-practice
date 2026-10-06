print("1. Search Phone")
print("2. Search Problem")

choice = input("Enter Choose :")

if choice == "1" :
    phone2 = input("Enter Phone :")

    try :
        with open ("repair.txt","r") as file :
            for line in file:

                data = line.split("|")

                name = data[0].strip()
                phone = data[1].strip()
                problem = data[2].strip()

                if phone2 == phone :
                    print(f"Customer : {name}")
                    print(f"Phone : {phone}")
                    print(f"Problem : {problem}")
                    print()

    except FileNotFoundError :
        print("File Not Found")

elif choice == "2" :
    problem2 = input("Enter Problem :")

    try :
        with open ("repair.txt", "r")as file :
            for line in file :
                data = line.split("|")

                name = data[0].strip()
                phone = data[1].strip()
                problem = data[2].strip()

                if problem2 == problem :

                    print(f"Customer : {name}")
                    print(f"Phone : {phone}")
                    print(f"Problem : {problem}")
                    print()

    except FileNotFoundError:
        print("File Not Found")

else :
    print("Invalid Choice")

