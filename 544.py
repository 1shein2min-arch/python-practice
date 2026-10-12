import re

text = "Phone: 0912345678"

print(re.match(r"09", text))
print(re.search(r"09", text))