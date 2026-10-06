orders = {
    "Phone" : 3 ,
    "Laptop" : 5 ,
    "Tablet" : 2 ,
    "Watch" : 7 ,
    "Camera" : 4 
}
for name in orders :
    print(f"{name} : {orders[name]}")

print(len(orders))
if "Laptop" in orders:
    print("Laptop Found")

if "Mouse" in orders:
    print("Mouse Found")
else :
    print("Mouse Not Found")

orders_name = []
for name in orders :
    orders_name.append(name)

orders_name.sort()
print(orders_name)

score = []
for name in orders:
    score.append(orders[name])

score.sort()

print(f"Highest Order :{score[-1]}")
print(f"Lowest Order : {score[0]}")