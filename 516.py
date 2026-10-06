with open("repair.txt","w") as file :
    file.write("iPhone 11 - 30000\n")
    file.write("Redmi Note 13 - 50000\n")
    file.write("Samsung A52 - 80000\n")
 
with open("repair.txt","r") as file :
    for line in file:
        print(line.strip())