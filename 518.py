with open("repair.txt","r") as file :
    lines = file.readlines()

    for line in lines :
        model = line.split("-")[0].strip()

        print(model)

        