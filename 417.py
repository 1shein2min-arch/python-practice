from datetime import datetime,timedelta

date_text = input("Enter Date DD/MM/YYYY :")

while True :
    try :
        repair_date = datetime.strptime(
            date_text,"%d/%m/%Y").date(
        )
        break
    except ValueError :
        print("Invalid Date.Please Try Again")

today = datetime.now().date()

due_date = repair_date + timedelta(days=7)

if today > due_date :
    print("Overdue")

elif today == due_date:
    print("Due Today")

else :
    print("Not Due Yet")