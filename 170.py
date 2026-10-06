products = {
    "Phone" : 500000 ,
    "Laptop" : 1200000 ,
    "Tablet" : 700000 ,
    "Watch" : 250000 ,
    "Camera" : 800000
}
print(f"Phone : {products['Phone']}")
print(f"Laptop : {products['Laptop']}")
print(f"Tablet : {products['Tablet']}")
print(f"Watch : {products['Watch']}")
print(f"Camera : {products['Camera']}")

print(len(products))
if "Laptop" in products :
    print("Laptop Found")

if "Mouse" in products :
    print("Mouse Found")
else :
    print("Mouse Not Found")

products_name = ["Phone","Laptop","Tablet","Watch","Camera"]

products_name.sort()

print(products_name)

print(f"First : {products_name[0]}")
print(f"Last : {products_name[-1]}")