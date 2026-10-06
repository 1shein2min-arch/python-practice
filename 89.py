numbers = []
even_numbers = []
odd_numbers = []

for num in range(5):
    number = int(input("Enter Number: "))
    numbers.append(number)

for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)
    else:
        odd_numbers.append(number)

print(f"Numbers : {numbers}")
print(f"Even Numbers : {even_numbers}")
print(f"Odd Numbers : {odd_numbers}")