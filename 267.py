sales = {
    "Aung": 500000,
    "Ko Ko": 1200000,
    "Hla Hla": 750000,
    "Su Su": 1500000
}
def show_sale():
    for name,sale in sales.items() :
        print(f"{name} : {sale}")

def add_sale(sale,add):
    return sale + add

def vip() :
    for name,sale in sales.items() :
        if sale >= 1000000 :
            print(f" {name} :VIP")

def count() :
    vip = 0
    normal = 0
    for name,sale in sales.items() :
        if sale >= 1000000 :
            vip += 1
        else :
            normal += 1
    print(f"VIP count : {vip}")
    print(f"Normal count : {normal}")

def highest() :
    high = 0
    high_name = ""
    for name,sale in sales.items() :
        if sale > high :
            high = sale
            high_name = name

    print(f"Highest Name {high_name} : Highest Sale : {high}")

def goodbye() :
    print("Goodbye !")

while True :

    print("1. Show Sales")
    print("2. Add Sale")
    print("3. Show VIP")
    print("4. Count")
    print("5. Highest Sale")
    print("6. Exit")

    choice = int(input("Enter Choose :"))

    if choice == 1 :
        show_sale()

    elif choice == 2 :
        name = input("Enter Name :")
        if name in sales:
            sale = sales.get(name)
            add = int(input("Enter Sale :"))
            total = add_sale(sale,add)
            sales[name] = total
            print("Sale Added")
        else :
            print("Name Not Found")

    elif choice == 3 :
        vip()

    elif choice == 4 :
        count()

    elif choice == 5 :
        highest()

    elif choice == 6 :
        goodbye()
        break

    else:
        print("Invalid Choice")
