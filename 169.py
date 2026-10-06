products = {
    "Phone" : 500000 ,
    "Laptop" : 120000 ,
    "Tablet" : 700000 ,
    "Watch" : 250000 ,
    "Camera" : 800000
}
print(len(products))
if "Phone" in products :
    print("Phone Found")

if "Mouse" in products :
    print("Mouse Found")
else :
    print("Mouse Not Found")

print(f"Phone Price : {products['Phone']}")
print(f"Camera Price : {products['Camera']}")

products["Laptop"] = 1100000 
print("Laptop Updated")
print(f"Laptop Price : {products['Laptop']}")

products_name = ["Phone","Laptop","Tablet","Watch","Camera"]

products_name.sort()
print(products_name)

print(f"First: {products_name[0]}")
print(f"Last : {products_name[-1]}")