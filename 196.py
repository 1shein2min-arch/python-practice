products = {
    "Phone" : 500000,
    "Laptop" : 1200000,
    "Tablet" : 700000
}
products.get("Camera" , 0)
products.get("Watch" , 0)

print(f"Phone Price :{products.get('Phone')}")
print(f"Camera Price : {products.get('Camera', 0)}")
print(f"Watch Price : {products.get('Watch', 0)}")