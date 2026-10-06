with open("repair.txt","r")as file:
    data = file.readlines()

    for line in data :
        fee = int(line.split("-")[1].strip())

        if fee >= 50000 :
            print(line)