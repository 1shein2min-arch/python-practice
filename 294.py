with open ("students.txt","w") as file:
    file.write("Aung : 80\n")
    file.write("Ko Ko : 70\n")
    file.write("Su Su : 95")

print("Student List")

print("------------")

with open("students.txt","r") as file :
    data = file.read()

    print(data)