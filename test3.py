age = int(input("Enter your age: "))
show_time = input("Enter show time (matinee/night): ").lower()

# ၁။ အရင်ဆုံး အသက် သို့မဟုတ် ပြသချိန် အမှား စစ်ပါမည်
if age <= 0:
    print("Invalid Age!")
elif show_time != "matinee" and show_time != "night":
    print("Invalid Show Time!")

# ၂။ အမှားမရှိရင် လက်မှတ်ခ စတွက်ပါမည်
else:
    # အသက်အလိုက် မူလ လက်မှတ်ဈေး သတ်မှတ်ခြင်း
    if age <= 12:
        price = 5
    elif age >= 60:
        price = 6
    else:
        price = 10  # ၁၃ နှစ်မှ ၅၉ နှစ်ကြား

    # ပြသချိန် "matinee" ဖြစ်ခဲ့လျှင် $2 လျှော့ပေးခြင်း
    if show_time == "matinee":
        price = price - 2

    print(f"Ticket Price: ${price}")