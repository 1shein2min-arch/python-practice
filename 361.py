from datetime import datetime,timedelta

today = datetime.now().date()

display_today = today.strftime("%d/%m/%Y")

time = datetime.now().strftime("%H:%M:%S")

deadline = today + timedelta(days=10)

deadline_display = deadline.strftime("%d/%m/%Y")

day_remaining = deadline - today

print("===== Repair Deadline =====")

print(f"Today : {display_today}")
print(f"Time : {time}")
print(f"Deadline : {deadline_display}")
print(f"Days Remaining : {day_remaining.days}")