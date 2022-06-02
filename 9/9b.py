with open('input.txt') as fl:
    all_lines = fl.read().splitlines()

b = [[int(ch) for ch in row] for row in all_lines]
y_dim = len(b)
x_dim = len(b[0])

origins = []

# Find origins
for y in range(y_dim):
    for x in range(x_dim):
        
        if x+1 < x_dim:
            if not (b[y][x] < b[y][x+1]): continue
        if x-1 >= 0:
            if not (b[y][x] < b[y][x-1]): continue
        if y+1 < y_dim:
            if not (b[y][x] < b[y+1][x]): continue
        if y-1 >= 0:
            if not (b[y][x] < b[y-1][x]): continue

        # Store origin
        origins.append((y,x,))

def in_bounds(point):
    y, x = point
    return 0 <= y < y_dim and 0 <= x < x_dim

# Return checked
def srch(pos, p_val=None, old=[]):

    # Skip if pos not in bounds
    if not in_bounds(pos):
        return []

    # Skip if pos already checked
    if pos in old:
        return []

    y, x = pos
    val = b[y][x]

    # Skip if not larger then previoius val
    if p_val is not None:
        if not (val > p_val):
            return []

    # Skip if 9
    if val == 9:
        return []

    n = [pos]
    n.extend(srch((y, x+1), val, [*old, *n]))
    n.extend(srch((y, x-1), val, [*old, *n]))
    n.extend(srch((y+1, x), val, [*old, *n]))
    n.extend(srch((y-1, x), val, [*old, *n]))

    return n

three = []

for origin in origins:

    a = srch(origin)
    sz = len(a)

    if len(three) < 3:
        three.append(sz)
        continue

    for i in range(len(three)):
        if sz > three[i]:
            del three[i]
            three.append(sz)
            break


    """
    mask = [['.' for _ in range(x_dim)] for _ in range(y_dim)]

    for point in a:
        y, x = point
        mask[y][x] = b[y][x]

    print(' ')
    print('Size', len(a))
    print('----------')
    for row in mask:
        print(''.join([str(x) for x in row]))
    """

import math
print(three)
print(math.prod(three))

    