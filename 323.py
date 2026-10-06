repair = []
def new_repair() :
    customer_name = input("Enter Name :")
    phone_model = input("Enter Phone Model :")
    repair_fee = int(input("Enter Fee :"))

    return customer_name,phone_model,repair_fee

repair.append(new_repair())
print(repair)