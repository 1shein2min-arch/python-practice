celsius = int(input("Enter temperature :"))
if celsius < 0:
    print("Freezing! Wear a heavy coat.")
elif celsius <=19:
    print("Cold! Wear a jacket.")
elif celsius <=30:
    print("Warm! Nice weather.")
else :
    print("Hot! Drink plenty of water.")