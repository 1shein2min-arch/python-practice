repairs = [
    {"customer": "Aung", "final_fee": 50000},
    {"customer": "Mg Mg", "final_fee": 80000},
    {"customer": "Ko Ko", "final_fee": 120000},
    {"customer": "SheiN", "final_fee": 30000}
]

fee = [repair['final_fee'] for repair in repairs]

print(fee)