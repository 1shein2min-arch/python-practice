products = {
    "Phone" : 500000 ,
    "Laptop" : 1200000,
    "Tablet" : 700000 ,
    "Watch" : 250000 ,
    "Camera" : 800000 
}

print(len(products))
print(f"Phone Price : {products["Phone"]}")
print(f"Laptop Price : {products["Laptop"]}")

if "Tablet" in products :
    print("Tablet Found")

if "Headphone" in products :
    print("Headphone Found")
else :
    print("Headphone Not Found")

products["Laptop"] = 1100000
print("Laptop Updated")
print(f"Laptop Price : {'laptop'}")

products = ["Phone","Laptop","Tablet","Watch","Camera"]
products.sort()
print(products)

print(f"First : {products[0]}")
print(f"Last : {products[-1]}")