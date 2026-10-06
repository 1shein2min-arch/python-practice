gpa = float(input("Enter GPA (0.0 - 4.0): "))

# ၁။ အရင်ဆုံး GPA မှန်/မမှန် စစ်ပါမည်
if gpa < 0.0 or gpa > 4.0:
    print("Invalid GPA")
else:
    # GPA မှန်မှသာ Income ကို မေးပါမည်
    monthly_income = int(input("Enter monthly income ($): "))
    
    if monthly_income <= 0:
        print("Invalid income")
    elif gpa >= 3.8 and monthly_income < 1000:
        print("Congratulations! You get Full Scholarship! 🎓")
    elif gpa >= 3.5 and monthly_income < 2000:
        print("You get 50% Half Scholarship! 📚")
    else:
        print("Sorry, you are not eligible for any scholarship.")
        