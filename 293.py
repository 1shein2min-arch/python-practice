file = open("employees.txt","w")

file.write("Aung - Developer\n")
file.write("Ko Ko - Designer\n")
file.write("Su Su - Manager\n")
file.write("Mg Mg - Accountant\n")
file.write("Hla Hla - Engineer")

file.close()

file = open("employees.txt","r")

data = file.readlines()

print(data[2],end="")
print(data[3],end="")
print(data[4],end="")

file.close()