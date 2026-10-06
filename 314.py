try :
    with open ("repair.txt","r") as file :
        data = file.read()

        print("Repair Records")

        print("--------------")

        print(data)

except FileNotFoundError :
    print("File Not Found")    