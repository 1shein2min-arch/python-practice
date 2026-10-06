product = []
while True :
    name = input("Enter Name :")

    if name == "done" :
        break
    product.append(name)
    
print(f"Students : {product}")
print(f"Total Student : {len(product)}")
    