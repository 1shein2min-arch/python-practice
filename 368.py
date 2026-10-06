from datetime import datetime,timedelta

now = datetime.now().date()
display_now = now.strftime("%d/%m/%Y")

time = datetime.now()
display_time = time.strftime("%H:%M:%S")

deadline = now + timedelta(days=14)
display_deadline = deadline.strftime("%d/%m/%Y")

remain = deadline - now

print("===== Delivery =====")

print(f"Today : {display_now}")
print(f"Time : {display_time}")
print(f"Deadline : {display_deadline}")
print(f"Days Remaining : {remain.days}")

