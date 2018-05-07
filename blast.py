with open('blaster.txt', 'r') as f:
    textdb = f.read().strip().split('\n')

num = int(textdb.pop(0))
sep = textdb.pop(0)

data = []
titles = {}

for line in textdb:
    id, title, diff, lv, dmg, deps, next, deleted, *_ = line.strip().split(sep)
    id = int(id)
    lv = int(lv)
    dmg = int(dmg)
    deps = [int(x) for x in deps.split(',')]
    next = int(next)
    if next == -1:
        next = None
    deleted = bool(int(deleted))
    if not deleted:
        titles[id] = title
        data.append([title, diff, lv, dmg, deps, next])

for row in data:
    row[4] = [titles[i] for i in row[4] if i in titles]
    row[5] = titles.get(row[5], None)

titles = [row[0] for row in data]

print(len(data))
print(sep)

for i, (title, diff, lv, dmg, deps, next) in enumerate(data):
    if deps:
        deps = ','.join(str(titles.index(d)) for d in deps)
    else:
        deps = -1
    if next is not None:
        next = titles.index(next)
    else:
        next = -1
    print(sep.join(map(str, (i, title, diff, lv, dmg, deps, next, 0))))
