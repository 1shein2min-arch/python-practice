with open("repair.txt","r") as file :
    for line in file :
        data = line.split("|")

        name = data[0].strip()
        phone = data[1].strip()
        problem = data[2].strip()

        print(f"Customer : {name}")
        print(f"Phone : {phone}")
        print(f"Problem : {problem}")
        print()