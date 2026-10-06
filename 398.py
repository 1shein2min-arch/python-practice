repairs = [
    {"customer": "Aung", "final_fee": 50000},
    {"customer": "Mg Mg", "final_fee": 80000},
    {"customer": "Ko Ko", "final_fee": 120000},
    {"customer": "SheiN", "final_fee": 30000},
    {"customer": "Kyaw Kyaw", "final_fee": 200000}
]

result = filter(
    lambda repair : repair['final_fee'] > 100000, repairs
)

print(list(result))