cheap_count = 0
normal_count = 0
expensive_count = 0

total = 0
count = 0

while True :

    name = input("Enter Food Name").lower()
    length = len(name)
    if length < 3 :
        print("Food Name Too short")
        continue
    if name == "exit" :
        print("Exit")
        break

    price = int(input("Enter Price"))
    if price <= 0 :
        print("Invalid Price")

    else :
        if price < 3000 :
            discount = price * 0
            cheap_count = cheap_count + 1
        elif price < 7000 :
            discount = price * 0.05
            normal_count = normal_count + 1
        else :
            discount = price * 0.1
            expensive_count = expensive_count +1

    quantity = int(input("Enter Quantity"))
    if quantity <= 0 :
        print("Invalid Quantity")

    else :
        subtotal = price * quantity
        subdiscount = discount * quantity
        final_price = subtotal - subdiscount

    print(f"Food = {name}")
    print(f"Price = {price}")
    print(f"Quantity = {quantity}")

    print(f"Subtotal = {subtotal}")
    print(f"Discount = {subdiscount}")
    print(f"Final Bill = {final_price}")

total = total + final_price
count = count + quantity

print(f"Cheap Count : {cheap_count}")
print(f"Normal Count : {normal_count}")
print(f"Expensive Count : {expensive_count}")

print(f"Total Sales : {total}")
print(f"Total Food Quantity : {count}")

if count > 0 :
    average = total/count 
    print(f"Average Bill : {average}")

    if average >= 10000 :
        print("Expensive Order")
    elif average >= 5000 :
        print("Normal Order")
    else :
        print("Cheap Order")

else :
    print("There is no Order")

