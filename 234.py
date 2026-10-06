products = {
    "Phone" : 500000 ,
    "Laptop" : 1200000 ,
    "Watch" : 250000 ,
    "Mouse" : 150000
}

def product(name,price) :
    print(f"{name} : {price}")

def pro() :
    name = input("Enter Product :")
    if name in products :
        quantity = int(input("Enter Quantity :"))
        print("Product :")
        print(f"{name} : {products.get(name)}")

        print(f"Quantity :{quantity}")

        total = products.get(name) * quantity
        print(f"Total Price : {total}")
    else :
        print("Product Not Found")

print("===== Shop =====")

for name,price in products.items() :
    product(name,price)

pro() 
    