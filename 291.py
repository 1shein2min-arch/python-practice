file = open("employees.txt" , "w")

file.write("Aung - Developer\n")
file.write("Ko Ko - Designer\n")
file.write("Su Su - Manager\n")
file.write("Mg Mg - Accountant\n")
file.write("Hla Hla - Engineer")

file.close()

file = open("employees.txt", "r")

data1 = file.readline()
data2 = file.readline()
data3 = file.readline()

print(data1,end="")
print(data2,end="")
print(data3,end="")

file.close()
