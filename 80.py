cheap_count = 0
normal_count = 0
expensive_count = 0
total = 0
count = 0

while True :
    price = int(input("Enter Price"))
    if price == -1 :
        print("Exit")
        break
    elif price == 0 :
        print("Invalid Price")
        continue
    else :
        if price < 1000 :
            discount = price * 0.05
            final_price = price - discount
            cheap_count = cheap_count + 1
            print(f"Cheap Count : {cheap_count}")
        elif price < 5000 :
            discount = price * 0.1
            final_price = price - discount
            normal_count = normal_count + 1
            print(f"Normal Count : {normal_count}")
        else :
            discount = price * 0.15
            final_price = price - discount
            expensive_count = expensive_count + 1
            print(f"Expensive Count : {expensive_count}")
        
    print(f"Price = {price}")
    print(f"Discount = {discount}")
    print(f"Final Price = {final_price}")
    total = total + final_price
    count = count + 1
average = total/count
if average >= 5000 :
    print("Expensive Shopping")
elif average >= 2000 :
    print("Normal Shopping")
else :
    print("Cheap Shopping")
    