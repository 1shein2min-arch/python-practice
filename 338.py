def load_repair() :
    repair = []

    file = open("repair.txt", "r")
    data = file.readlines()

    for line in data :
        data1 = line.strip().split(",")

        model = data1[0]
        name = data1[1]
        fee = int(data1[2])
        status = data1[3]

        repair.append((model,name,fee,status))
    file.close()

    return repair

repair = load_repair()

def save_repairs() :
    file = open("repair.txt","w")

    for item in repair :
        model,name,fee,status = item

        file.write(f"{model},{name},{fee},{status}\n")

    file.close()


def new_repair() :
    model = input("Enter Model :")
    name = input("Enter Name :")
    fee = int(input("Enter Fee :"))
    status = input("Enter Status :")

    repair.append((model,name,fee,status))
    save_repairs()

def update_fee() :
    name1 = input("Enter Name :")
    fees = int(input("Enter Fee :"))
    for i in range(len(repair)) :
        model,name,fee,status = repair[i]
        if name1 == name :
            fee = fees
            repair[i] = (model,name,fee,status)
            save_repairs()

def delete_repair() :
    name1 = input("Enter Name :")
    for i in range(len(repair)) :
        model,name,fee,status = repair[i]

        if name1 == name :
            repair.remove(repair[i])
            save_repairs()
            break

delete_repair() 


        




            
            



