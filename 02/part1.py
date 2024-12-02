import sys

safe = 0
for line in sys.stdin.readlines():
    report = [int(n) for n in line.strip().split(' ')]
    deltas = [a-b for a, b in zip(report, report[1:])]
    if not all(abs(d) >= 1 and abs(d) <= 3 for d in deltas):
        continue

    if all(d > 0 for d in deltas) or all(d < 0 for d in deltas):
        safe += 1

print(safe)
