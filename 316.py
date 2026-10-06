while True :

    print("1. Add Repair")
    print("2. Show All Repairs")
    print("3. Search by Phone")
    print("4. Search by Problem")
    print("5. Exit")

    choice = input("Enter Choose :")

    if choice == "1" :
        customer = input("Enter Customer :")
        phone = input("Enter Phone :")
        problem = input("Enter Problem :")

        with open ("repair.txt","a") as file :
            file.write("\n" + customer +" | " + phone +" | "+problem)
            print("Repair Added")
        
    elif choice == "2" :
        print("Repair Records")
        print("--------------")

        try :

            with open ("repair.txt","r") as file :
                for line in file:
                    data = line.split("|")
                    name = data[0].strip()
                    phone = data[1].strip()
                    problem = data[2].strip()

                    print(f"Customer : {name}")
                    print(f"Phone : {phone}")
                    print(f"Problem : {problem}")
                    print()

        except FileNotFoundError:
            print("File Not Found")
            
    elif choice == "3" :
        phone2 = input("Enter Phone :")
        try :
            with open ("repair.txt","r") as file :
                for line in file :
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

    elif choice == "4" :
        problem2 = input("Enter Problem :")

        try :
            with open ("repair.txt","r") as file :
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

    elif choice == "5" :
        print("Goodbye")
        break

    else :
        print("Invalid Choice")