test = False

if test:
    fn = 'text.txt'
    folds = [
        ('y', 7),
        ('x', 5)
    ]
else:
    fn = 'input.txt'
    folds = [
        ('x', 655),
        ('y', 447),
        ('x', 327),
        ('y', 223),
        ('x', 163),
        ('y', 111),
        ('x', 81),
        ('y', 55),
        ('x', 40),
        ('y', 27),
        ('y', 13),
        ('y', 6)
    ]

with open(fn) as fl:
    all_lines = fl.read().splitlines()

lines = []
for line in all_lines:
    x, y = line.split(',')
    lines.append((int(x), int(y)))

print(lines)
ll = set(lines)
print(ll)

def doo(oldset, dirz, coord):
    newset = set()
    for elem in oldset:
        x, y = elem
        if dirz == 'y':
            if y > coord:
                newset.add((x,2*coord-y))
            else:
                newset.add((x,y))
        else:
            if x > coord:
                newset.add((2*coord-x,y))
            else:
                newset.add((x,y))
    return newset

for fold in folds:
    dirz, coord = fold
    print(f'FOLDING {dirz} {coord}')
    print(len(ll))
    ll = doo(ll, dirz, coord)
    print(len(ll))

bb = [[' ' for _ in range(100)] for _ in range(100)]

for a in ll:
    x, y = a
    bb[x][y] = '#'

for a in bb:
    print(''.join(a))