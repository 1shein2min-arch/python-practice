repairs = [
    ("iPhone 11", "SheiN", 30000),
    ("Redmi Note 13", "Aung", 50000),
    ("Vivo Y55", "Mg Mg", 25000),
    ("Samsung A52", "Ko Ko", 80000)
]
highest_fee = 0
highest_name = ""
highest_model = ""

print("Highest Repair Fee")
for item in repairs:
    model,name,fee = item
    if fee >= highest_fee:
        highest_fee = fee
        highest_name = name
        highest_model = model

print(f"Model : {highest_model}")
print(f"Name : {highest_name}")
print(f"Fee : {highest_fee}")
    