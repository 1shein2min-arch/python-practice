phones = {
    "Phone" : 500000 ,
    "Laptop" : 1200000 ,
    "Watch" : 250000 ,
    "Camera" : 800000
}

def all(name,price) :
    print(f"{name} : {price}")

def phone_name() :
    name = input("Enter Name :")
    if name in phones :
        print("Phone Price :")
        print(f"{name} : {phones.get(name)}")
    else :
        print("Phone Not Found")

print("===== Phone Shop =====")

for name,price in phones.items() :
    all(name,price)

phone_name()