with open("customer.txt", "r") as file:
    data = file.readlines()

data.remove("Ko Ko")

with open("customer.txt", "w") as file:
    file.writelines(data)