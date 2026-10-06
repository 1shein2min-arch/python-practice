customers = ["Aung", "Mg Mg", "Ko Ko", "SheiN"]

fees = [50000, 80000, 120000, 30000]

for customer,fee in zip(customers,fees) :
    print(f"{customer} : {fee}")