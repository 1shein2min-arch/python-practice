file = open("students.txt" , "w")

file.write("Aung : 80\n")
file.write("Ko Ko : 70\n")
file.write("Su Su : 95\n")
file.write("Mg Mg : 85")

file.close()

file = open("students.txt" , "r")

data = file.readlines()

print(data[0],end="")
print(data[1],end="")