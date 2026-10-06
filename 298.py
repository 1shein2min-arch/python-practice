customer = input("Enter Customer :")
phone = input("Enter Phone :")
problem = input("Enter Problem :")

with open("repair.txt","a") as file :
    file.write("\n" + customer + "|" + phone + "|" + problem)

with open("repair.txt","r") as file :
    data = file.read()

    print("Repair Customer")

    print("---------------")

    print(data)