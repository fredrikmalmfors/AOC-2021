with open('input.txt') as fl:
    all_lines = fl.read().splitlines()

b = [[int(ch) for ch in row] for row in all_lines]

def reset_f():
    return [[False for _ in row] for row in all_lines]

f = reset_f()
y_dim = len(b)
x_dim = len(b[0])

tot = 0

def print_board():
    global b
    print('-------------')
    for row in b:
        row_str = ''.join([str(x) for x in row])
        print(row_str)

def in_bounds(y, x):
    return 0 <= y < y_dim and 0 <= x < x_dim

def flash(y, x):
    global b
    global f
    global tot

    if not in_bounds(y, x):
        return

    b[y][x] += 1

    if b[y][x] < 10:
        return

    if f[y][x]:
        return

    # Flash
    tot += 1

    ring = [
        (y-1, x-1),
        (y-1, x),
        (y-1, x+1),
        (y, x+1),
        (y+1, x+1),
        (y+1, x),
        (y+1, x-1),
        (y, x-1)
    ]

    f[y][x] = True

    for point in ring:
        flash(*point)


def step():
    global b
    global f

    f = reset_f()

    # Increase all by one:
    b = [[x+1 for x in row] for row in b]

    # Flash
    for y in range(y_dim):
        for x in range(x_dim):
            if b[y][x] == 10:
                flash(y, x)

    for y in range(y_dim):
        for x in range(x_dim):
            if b[y][x] > 9:
                b[y][x] = 0

print_board()
for i in range(100):
    step()
print_board()
print(tot)

