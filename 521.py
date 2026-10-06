with open("repair.txt","r")as file:
    data = file.readlines()

    total = 0
    count = 0
    for line in data :
        fee = int(line.split("-")[1].strip())

        total += fee
        count += 1

    average = total/count

    print(f"Average Fee : {average}")
