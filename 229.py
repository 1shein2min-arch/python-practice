shop = {
    "Redmi Note 13 Pro" : 550000,
    "Samsung S24 Ultra" : 4500000 ,
    "Vivo Y55A" : 350000 ,
    "iPhone 15" : 3200000
}

def phone(name,price):
         print(f"{name} : {price}")

def expensive(name,price) :
    if price >= 1000000 :
        print(name)

def cheap(name,price) :
    if price < 1000000 :
        print(name)

def total() :
    print(f"Total Phones : {len(shop)}")

def most_expensive() :
    most_expensive_price = 0
    most_expensive_name = ""

    for name,price in shop.items() :
        if price > most_expensive_price :
            most_expensive_price = price 
            most_expensive_name = name
    print("Most Expensive :")
    print(f"{most_expensive_name} : {most_expensive_price}")

print("===== Phone Shop =====")

for name,price in shop.items() :
    phone(name,price)

print("Expensive Phones :")
for name,price in shop.items() :
    expensive(name,price)

print("Cheap Phones :")
for name,price in shop.items() :
    cheap(name,price)

total()

most_expensive()