# အသက်နဲ့ ရက်ကို User ဆီက တောင်းတာ
age = int(input("Enter your age: "))
day = input("Enter day of the week: ")

# အသက် မှားရိုက်မိရင် Invalid ထုတ်ပြဖို့ အရင်စစ်တာ
if age < 0:
    print("Invalid Age")
else:
    # ၁။ အသက်အလိုက် မူလဈေးနှုန်း (price) ကို အရင်သတ်မှတ်မယ်
    if age < 12:
        price = 5
    elif age <= 59:
        price = 10
    else:  # age >= 60
        price = 7

    # ၂။ ဗုဒ္ဓဟူးနေ့ ဖြစ်နေရင် $2 လျှော့ပေးမယ်
    # lower() လေးသုံးထားလို့ "Wednesday", "wednesday", "WEDNESDAY" ဘာရိုက်ရိုက် အလုပ်လုပ်ပါတယ်
    if day.lower() == "wednesday":
        price = price - 2  # သို့မဟုတ် price -= 2

    # နောက်ဆုံး ရလဒ်ကို ပြပေးတာ
    print(f"Ticket price: ${price}")