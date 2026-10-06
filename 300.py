with open("sales.txt","w") as file :
    file.write("Aung | 15000 \n")
    file.write("Ko Ko | 25000\n")
    file.write("Su Su | 18000\n")
    file.write("Mg Mg | 30000\n")
    file.write("Hla Hla | 12000")

with open("sales.txt","r") as file :
    for line in file :
        print(line,end="")

print("Total Sales : 100000")
print("Highest Sale : Mg Mg | 30000")