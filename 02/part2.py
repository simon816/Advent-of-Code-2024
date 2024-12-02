import sys

def is_safe(report):
    deltas = [a-b for a, b in zip(report, report[1:])]
    if not all(abs(d) >= 1 and abs(d) <= 3 for d in deltas):
        return False

    return all(d > 0 for d in deltas) or all(d < 0 for d in deltas)

safe = 0
for line in sys.stdin.readlines():
    orig_report = [int(n) for n in line.strip().split(' ')]

    if is_safe(orig_report):
        safe += 1
        continue

    for i in range(len(orig_report)):
        if is_safe(orig_report[:i] + orig_report[i+1:]):
            safe += 1
            break

print(safe)
