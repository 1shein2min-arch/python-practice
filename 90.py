names = []
short_names = []
valid_names = []

for num in range(1, 6):
    name = input("Enter Name: ")
    names.append(name)

for name in names:
    length = len(name)

    if length < 4:
        short_names.append(name)
    else:
        valid_names.append(name)

print(f"Names : {names}")
print(f"Short Names : {short_names}")
print(f"Valid Names : {valid_names}")