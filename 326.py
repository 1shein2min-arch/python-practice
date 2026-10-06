repairs = [
    ("iPhone 11", "SheiN", 30000),
    ("Redmi Note 13", "Aung", 50000),
    ("Vivo Y55", "Mg Mg", 25000),
    ("Samsung A52", "Ko Ko", 80000)
]
for item in repairs :
    model,name,price = item

    if price >= 30000 :
        print(f"Model : {model}")
        print(f"Name : {name}")
        print(f"Fee : {price}")
        print()