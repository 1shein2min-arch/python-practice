prices = []
cheap_price = []
normal_price = []
expensive_price = []

for num in range (8) :
    price = int(input("Enter Price"))
    prices.append(price)

for price in prices :
    if price < 3000 :
        cheap_price.append(price)

    elif price < 7000 :
        normal_price.append(price)

    else :
        expensive_price.append(price)

cheap_total = 0
normal_total = 0
expensive_total = 0

for price in cheap_price :
    cheap_count = len(cheap_price)
    cheap_total = cheap_total + price

for price in normal_price :
    normal_count = len(normal_price)
    normal_total = normal_total + price

for price in expensive_price :
    expensive_count = len(expensive_price)
    expensive_total = expensive_total + price

total = 0
for price in prices :
    total =total + price

count = len(prices)

average = total/count

Highest = max(prices)
lowest = min(prices)

print(f"Prices : {prices}")
print(f"Cheap Prices : {cheap_price}")
print(f"Normal Prices : {normal_price}")
print(f"Expensive Prices : {expensive_price}")
print(f"Cheap Count : {cheap_count}")
print(f"Normal Count : {normal_count}")
print(f"Expensive Count : {expensive_count}")
print(f"Cheap Total : {cheap_total}")
print(f"Normal Total : {normal_total}")
print(f"Expensive Total : {expensive_total}")
print(f"Total : {total}")
print(f"Average : {average}")
print(f"Highest : {Highest}")
print(f"Lowest : {lowest}")
