unit = int(input("Enter units :"))
if unit<=0:
    print("Invalid Units")
elif unit<=100:
    print("1 ယူနစ်လျှင် 50 ကျပ်")
elif unit<=200:
    print("1 ယူနစ်လျှင် 100 ကျပ်")
elif unit<=300:
    print("1 ယူနစ်လျှင် 150 ကျပ်")
else :
    print("1 ယူနစ်လျှင် 200 ကျပ်")

total_Electricity_bill = unit+500

print(f"Total Electricity bill is {total_Electricity_bill} kyats")