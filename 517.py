with open("repair.txt","a")as file:
    file.write("Vivo Y55 - 25000\n")
    file.write("Redmi 12 - 35000\n")

with open("repair.txt","r")as file:
    for line in file :
        print(line.strip())