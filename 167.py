products = {
    "Phone" : 500000,
    "Laptop" : 1200000 ,
    "Tablet" : 700000 ,
    "Watch" : 250000
}

print(len(products))
print(products["Phone"])
print(products["Laptop"])

if "Tablet" in products :
    print("Tablet Found")

if "Camera" in products :
    print("Camera Found")
else :
    print("Camera Not Found")

products = ['Phone' , 'Laptop' , 'Tablet', 'Watch']
products.sort()
print(products)


print(f"First Product : {products[0]}")
print(f"Last Product : {products[-1]}")

products.sort(reverse=True)
print(products)
