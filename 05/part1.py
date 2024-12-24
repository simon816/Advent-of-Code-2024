from collections import defaultdict
import sys

mode = 'ordering'

dependencies = defaultdict(list)

val = 0

for line in sys.stdin.readlines():
    line = line.strip()
    if not line:
        mode = 'updates'
        continue
    if mode == 'ordering':
        dep, page = line.split('|')
        dependencies[page].append(dep)
    elif mode == 'updates':
        invalid = False
        update = line.split(',')
        for i, page in enumerate(update):
            rest = update[i+1:]
            if len(dependencies[page]):
                deps = dependencies[page]
                for n in rest:
                    if n in deps:
                        invalid = True
        if not invalid:
            val += int(update[len(update)//2])

print(val)
