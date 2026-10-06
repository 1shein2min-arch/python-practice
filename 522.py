with open("repair.txt","r")as file:
    data = file.readlines()

    result = []

    for line in data:
        fee = int(line.split("-")[1].strip())

        if fee >= 50000 :
            result.append(line)

    for lines in result :
        print(lines.strip())
