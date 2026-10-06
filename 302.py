data = "Redmi Note 13 | 250000 "

result = data.split("|")

print(f"Product : {result[0].strip()}")
print(f"Price : {result[1].strip()}")