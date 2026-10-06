small_count = 0
medium_count = 0
large_count = 0

total = 0
count = 0

while True:

    price = int(input("Enter Price: "))

    if price == -1:
        print("Exit")
        break

    elif price == 0:
        print("Invalid Price")
        continue

    if price < 1000:
        discount = price * 0.05
        small_count = small_count + 1

    elif price < 5000:
        discount = price * 0.10
        medium_count = medium_count + 1

    else:
        discount = price * 0.20
        large_count = large_count + 1

    final_price = price - discount

    total = total + final_price
    count = count + 1

    print(f"Original Price: {price}")
    print(f"Discount: {discount}")
    print(f"Final Price: {final_price}")


print(f"Small Count: {small_count}")
print(f"Medium Count: {medium_count}")
print(f"Large Count: {large_count}")

print(f"Total Sales: {total}")
print(f"Product Count: {count}")

average = total / count

print(f"Average Final Price: {average}")

if average >= 5000:
    print("High Sales")

elif average >= 2000:
    print("Normal Sales")

else:
    print("Low Sales")