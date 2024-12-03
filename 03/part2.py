import re
import sys

enable = True
total = 0
text = sys.stdin.read()
for m in re.finditer('mul\\((\\d+),(\\d+)\\)|(do\\(\\))|(don\'t\\(\\))', text):
    if m.group(3):
        enable = True
    elif m.group(4):
        enable = False
    elif enable:
        a, b = m.group(1), m.group(2)
        total += int(a) * int(b)

print(total)
