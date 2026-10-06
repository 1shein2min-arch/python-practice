from datetime import datetime, timedelta

now = datetime.now().date()

date = datetime.now().strftime("%d/%m/%Y")

time = datetime.now().strftime("%H:%M:%S")

result = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

today = datetime.now()

future = today + timedelta(days = 7)

print(f"Future Date : {future}") 