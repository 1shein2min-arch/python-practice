repairs = [
    {"customer": "Aung", "final_fee": 80000},
    {"customer": "Mg Mg", "final_fee": 30000},
    {"customer": "Ko Ko", "final_fee": 150000}
]

result = max(
    repairs,key=lambda repair : repair['final_fee']
)

print(f"Customer : {result['customer']}")
print(f"Fee : {result['final_fee']}")