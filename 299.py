name = input("Enter Customer :")
phone = input("Enter Phone :")
problem = input("Enter Problem :")
price = input("Enter Price :")

with open("repair.txt","a") as file :
    file.write("\n" + name + " | " + phone + " | " + problem + " | " + price)

print("Phone Repair Records")

print("--------------------")

with open("repair.txt","r") as file :
    data = file.read()

    print(data)

