numbers = [10, 20, 30]

try:
    print(numbers[10])

except IndexError:
    print("ဒီ index မရှိပါဘူး")

print("Program continues")