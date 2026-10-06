file = open("repair.txt","r")

data = file.readlines()

repairs = []
for line in data :
    data1 = line.strip().split(",")

    model = data1[0]
    name = data1[1]
    fee = int(data1[2])
    status = data1[3]

    repairs.append((model,name,fee,status))
print(repairs)