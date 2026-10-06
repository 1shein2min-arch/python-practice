from pathlib import Path

path = Path("test.txt")

path.write_text("Hello Python")

from pathlib import Path

path = Path("test.txt")

data = path.read_text()

print(data)