prices = {
    "Phone" : 500000 ,
    "Laptop" : 1200000 ,
    "Tablet" : 700000 ,
    "Watch" : 250000
}
total = 0
for price in prices.values() :
    print(price)
    total =total + price
print(f"Total : {total}")

print("Above 600000 :")
for price in prices.values() :
    if price >= 600000 :
        print(price)
