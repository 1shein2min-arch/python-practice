with open("sales.txt" , "r") as file :
    for line in file :
        data = line.split("|")

        name = data[0].strip()
        price = data[1].strip()

        print(name + " : " + price)