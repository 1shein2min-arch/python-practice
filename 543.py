import re

phone = "09 123 456 789"
note = "Customer needs urgent repair"
text = "iPhone 11 costs 30000, Redmi 13 costs 50000"

clean_phone = re.sub(r"\s+","",phone)
is_urgent = re.search(r"urgent",note)
numbers = re.findall(r"[0-9]+",text)

print(clean_phone)
print(is_urgent.group())
print(numbers)