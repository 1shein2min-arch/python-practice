repairs = [
    {"customer": "Aung", "final_fee": 50000},
    {"customer": "Mg Mg", "final_fee": 80000},
    {"customer": "Ko Ko", "final_fee": 120000},
    {"customer": "SheiN", "final_fee": 30000}
]

result = map(
    lambda repair: repair["final_fee"] * 1.10,
    repairs
)

print(list(result))