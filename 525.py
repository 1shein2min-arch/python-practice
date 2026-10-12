numbers = [10, 20, 30]

try:
    index = int(input("Enter index: "))
    print(numbers[index])

except ValueError:
    print("Please enter a number")