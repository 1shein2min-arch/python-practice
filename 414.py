from datetime import datetime,timedelta

repair_date = datetime(2026, 9 , 15).date()

today = datetime.now().date()

overdue_date = repair_date + timedelta(days=7)

if today > overdue_date :
    print("Repair Is Over")
else :
    print("Repair Is Not Over")