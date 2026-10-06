even_total = 0
even_count = 0
odd_total = 0
odd_count = 0
while True :
    num = int(input("Enter Number"))
    if num == 0 :
        print("Exit")
        break
    if num % 2 == 0:
        print("Even")
        even_total = even_total + num
        even_count = even_count + 1
    else :
        print("odd")
        odd_total = odd_total + num
        odd_count = odd_count + 1
    length = len(str(num))
    print(f"{length} Digits")
even_average = even_total/even_count
odd_average = odd_total/odd_count
print(f"Even Total : {even_total}")
print(f"Even Count : {even_count}")
print(f"Even Average : {even_average}")

print(f"Odd Total : {odd_total}")
print(f"Odd Count : {odd_count}")
print(f"Odd Average : {odd_average}") 

if even_average > odd_average:
    print("Even Average is Higher")
elif even_average < odd_average:
    print("Odd Average is Higher")
else :
    print("Both Average are Equal")


