limit = int(input("Enter number: "))
num = 1
count = 0

while limit>= num :
    if num % 2 == 0:
        print(num)
        count = count + 1

    num = num + 1

print(f"Total Even = {count}")