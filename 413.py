from datetime import datetime,timedelta

now = datetime.now().date()

after_7_days = now + timedelta(days=7)

print(f"Today :{now}")

print(f"After 7 Days : {after_7_days}")