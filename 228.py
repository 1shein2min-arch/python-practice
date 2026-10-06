products = {
    "Phone": 500000,
    "Laptop": 1200000,
    "Watch": 250000,
    "Camera": 800000,
    "Mouse": 150000
}

def product(name,price) :
    if price >= 800000 :
        print(f"{name} : Expensive")
    else :
        print(f"{name} : Cheap")

print("===== Product Check =====")
for name,price in products.items() :
    product(name,price)
