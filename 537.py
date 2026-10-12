import time

now = time.localtime()

formatted = time.strftime("%d/%m/%Y" , now)

print(formatted)