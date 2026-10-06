vehicle_type = input("Enter vehicle type (bike/car/bus): ").lower()
hours = int(input("Enter parking hours: "))

# ၁။ အရင်ဆုံး ဂဏန်းအမှား နှင့် ယာဉ်အမျိုးအစား အမှား စစ်ပါမည်
if hours <= 0:
    print("Invalid Hours!")
elif vehicle_type != "bike" and vehicle_type != "car" and vehicle_type != "bus":
    print("Invalid Vehicle Type!")

# ၂။ အမှားမရှိရင် တွက်ချက်မှု စပါမည်
else:
    # 1 နာရီ သို့မဟုတ် 1 နာရီအောက် ဆိုလျှင် အခမဲ့ (Free)
    if hours <= 1:
        fee = 0
    else:
        # ယာဉ်အမျိုးအစားအလိုက် 1 နာရီ ဈေးနှုန်းဖြင့် မြှောက်ခြင်း
        if vehicle_type == "bike":
            fee = hours * 500
        elif vehicle_type == "car":
            fee = hours * 1000
        elif vehicle_type == "bus":
            fee = hours * 2000

        # ၂၄ နာရီထက် ပိုပါက ၂၀၀၀ ကျပ် လျှော့ပေးခြင်း
        if hours > 24:
            fee = fee - 2000

    print(f"Parking Fee: {fee} Kyats")