import re
import sys

total = 0
text = sys.stdin.read()
for m in re.finditer('mul\\((\\d+),(\\d+)\\)', text):
    a, b = m.group(1), m.group(2)
    total += int(a) * int(b)

print(total)
