prices = {
    "Phone" : 450000 ,
    "Laptop" : 1500000 ,
    "Tablet" : 650000 ,
    "Watch" : 200000 ,
    "Camera" : 850000
}
print("Expensive :")
for name ,price in prices.items() :
    if price >= 850000 :
        print(name)

print("Cheap :")

for name,price in prices.items() :
    if price <= 200000 :
        print(name)

highest_price = 0
highest_name = ""

lowest_price = 9999999
lowest_name = ""

for name,price in prices.items() :
    if price > highest_price :
        highest_price = price
        highest_name = name
    if price < lowest_price :
        lowest_price = price
        lowest_name = name

print(f"Highest : {highest_name} : {highest_price}")
print(f"lowest : {lowest_name} : {lowest_price}")