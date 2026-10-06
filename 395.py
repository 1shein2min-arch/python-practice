repairs = [
    {"customer": "Aung", "final_fee": 80000},
    {"customer": "Mg Mg", "final_fee": 30000},
    {"customer": "Ko Ko", "final_fee": 150000}
]

result = sorted(repairs,key=lambda repair: repair["customer"])

for repair in result :
    print(f"{repair['customer']} {repair['final_fee']}")