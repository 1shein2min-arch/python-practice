file = open("students.txt" , "w")

file.write("Aung : 80\n")
file.write("Ko Ko : 70\n")
file.write("Su Su : 95\n")
file.write("Mg Mg : 85")

file.close()

file = open("students.txt" ,"r")

data1 = file.readline()
data2 = file.readline()

print(data1,end="")
print(data2,end="")

file.close()