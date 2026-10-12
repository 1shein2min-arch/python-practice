import time

text = "08/10/2026"

result = time.strptime(text, "%d/%m/%Y")

print(result)