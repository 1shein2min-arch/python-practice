from datetime import datetime,timedelta

while True :
    
    date_text = input("Enter Date  DD/MM/YYYY :")

    try:
        repair_date = datetime.strptime(
            date_text,"%d/%m/%Y").date()
        break
    except ValueError :
        print("Invalid Date. Please Try Again")

due_date = repair_date + timedelta(days=7)

print(f"Repair Date : {repair_date}")
print(f"Due Date :{due_date}")
