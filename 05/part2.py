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
        orig = line.split(',')
        update = list(orig)
        change = True
        while change:
            change = False
            for i in range(len(update)):
                before = update[:i]
                page = update[i]
                rest = update[i+1:]
                if page in dependencies:
                    req = dependencies[page]
                    for r in req:
                        if r in rest:
                            idx = rest.index(r)
                            rest.insert(idx+1, page)
                            update = before + rest
                            change = True
                            break
        if update != orig:
            val += int(update[len(update)//2])
            print(','.join(orig), ','.join(update))
print(val)
