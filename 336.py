file = open("repair.txt","w")

file.write("iphone 11,SheiN,30000,Done\n")
file.write("Redmi Note 13,Aung,50000,Pending\n")

file.close()

print("--- Saved Repairs ---")
file = open("repair.txt","r")

data = file.read()

print(data)

file.close()