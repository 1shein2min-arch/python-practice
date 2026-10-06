file = open("employees.txt","w")

file.write("Aung - Developer\n")
file.write("Ko Ko - Designer\n")
file.write("Su Su - Manager \n")
file.write("Mg Mg - Accountant")

file.close()

print("Employees List")

print("--------------")

file = open("employees.txt","r")
data = file.read()
print(data)
file.close()

print("--------------")

print("Total Employees : 4")
