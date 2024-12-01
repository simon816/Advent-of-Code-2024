import sys
from collections import Counter

list1 = []
list2 = []

for line in sys.stdin.readlines():
    first, second = line.strip().split('   ')
    list1.append(int(first))
    list2.append(int(second))

counts = Counter(list2)

score = 0
for n in list1:
    score += n * counts[n]

print(score)
