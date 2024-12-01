import sys

list1 = []
list2 = []

for line in sys.stdin.readlines():
    first, second = line.strip().split('   ')
    list1.append(int(first))
    list2.append(int(second))

list1.sort()
list2.sort()

total = 0
for a, b in zip(list1, list2):
    total += abs(b - a)

print(total)
