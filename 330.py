repairs = [
    ("iPhone 11", "SheiN", 30000),
    ("Redmi Note 13", "Aung", 50000),
    ("Vivo Y55", "Mg Mg", 25000),
    ("Samsung A52", "Ko Ko", 80000),
    ("Redmi 12", "Aung", 35000)
]
fees = 0
for item in repairs:
    model,name,fee = item
    if fee >= 50000 :
        fees = fees + fee
        print(f"Model : {model}")
        print(f"Name : {name}")
        print(f"Fee : {fee}")
        print()

print(f"Total High Fee :{fees}")