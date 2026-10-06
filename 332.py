repairs = [
    ("iPhone 11", "SheiN", 30000, "Done"),
    ("Redmi Note 13", "Aung", 50000, "Pending"),
    ("Vivo Y55", "Mg Mg", 25000, "Done"),
    ("Samsung A52", "Ko Ko", 80000, "Pending"),
    ("Redmi 12", "Aung", 35000, "Done")
]

def new_repair() :
    model = input("Enter Model :")
    name = input("Enter Name :")
    fee = int(input("Enter Fee :"))
    status = input("Enter Status :")

    item = (model,name,fee,status)

    repairs.append(item)

new_repair()

print(repairs)