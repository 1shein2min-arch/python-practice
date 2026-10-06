largest = 0
smallest = 9999999
total = 0 
count = 0

while True :
    num = int(input("Enter Number"))
    if num == 0 :
        print("Exit")
        break
    if num > largest :
        largest = num
        total = total + num
        count = count + 1
    elif num < smallest :
        smallest = num
        total = total + num
        count = count + 1
average = total/count
print(f"Total : {total}")
print(f"Count : {count}")
print(f"Average : {average}")
print(f"largest : {largest}")
print(f"Smallest : {smallest}")