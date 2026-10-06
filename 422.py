with open("customer.txt","a") as file :
    file.write("Aung")
    file.write("\nMg Mg")

with open("customer.txt" , "r") as file :
    data = file.read()

print(data)