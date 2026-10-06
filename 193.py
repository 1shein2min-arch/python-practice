products = {
    "Phone" : 500000 ,
    "Laptop" : 1200000 ,
    "Watch" : 250000
}

print("Before :")
print(products)

products.update({"Phone" : 550000})
print("Phone Updated")
products.update({"Camera" : 800000})
print("Camera Added")
print("After Update :")
print(products)