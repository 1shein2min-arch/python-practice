problem2 = input("Enter Problem :")

with open("repair.txt","r") as file :
    for line in file :
        data = line.split("|")

        name = data[0].strip()
        phone = data[1].strip()
        problem = data[2].strip()

        if problem2 == problem :
            print(f"Name : {name}")
            print(f"Phone : {phone}")
            print()