with open("repair.txt","r") as file :
    lines = file.readlines()

    for line in lines :
        fee = int(line.split("-")[1].strip())

        print(fee)