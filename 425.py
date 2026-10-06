with open("customer.txt","r") as file:
    data = file.readlines()

data = [customer.replace("Aung","Aung Min")for customer in data]

with open("customer.txt","w") as file :
    file.writelines(data)