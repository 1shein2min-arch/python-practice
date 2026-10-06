repairs = [
    ("iPhone 11", "SheiN", 30000),
    ("Redmi Note 13", "Aung", 50000),
    ("Vivo Y55", "Mg Mg", 25000),
    ("Samsung A52", "Ko Ko", 80000)
]

total = 0
for item in repairs:
    model,name,fee = item

    total = total + fee
print(f"Total Repair Fee :{total}")

count = len(repairs)
print(f"Number of Repairs : {count}")

average = total/count

print(f"Average Repair Fee : {average}")