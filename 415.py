from datetime import datetime,timedelta

date_text = input("Enter Repair Date (DD/MM/YY) : ")

repair_date = datetime.strptime(
    date_text,
    "%d/%m/%Y").date()

due_date = repair_date + timedelta(days=7)

print(f"Repair Date : {repair_date}")
print(f"Due Date : {due_date}")