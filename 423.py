with open("customer.txt","w") as file :
    file.write("Aung")
    file.write("\nMg Mg")
    file.write("\nKo Ko")

with open("customer.txt","r") as file :
    data = file.read()

    print(data)