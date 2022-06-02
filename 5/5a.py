with open('input.txt') as fl:
    all_lines = fl.read().splitlines()

dim = 1000 # only for test

bigmap = [[0 for _ in range(dim)] for _ in range(dim)]

for i, line in enumerate(all_lines):

    if i % 100 == 0:
        print('Step')

    a, b = line.split(' -> ')
    x1, y1 = [int(x) for x in a.split(',')]
    x2, y2 = [int(x) for x in b.split(',')]

    points = []

    # If vertical
    if x1 == x2:
        points = [(x1, y) for y in range(min(y1, y2), max(y1, y2)+1)]

    # If horizontal
    elif y1 == y2:
        points = [(x, y1) for x in range(min(x1, x2), max(x1, x2)+1)]

    # Diagonal
    elif abs(x1-x2) == abs(y1-y2):
        x_step = 1 if x2 > x1 else -1
        x_list = [x for x in range(x1, x2+x_step, x_step)]

        y_step = 1 if y2 > y1 else -1
        y_list = [y for y in range(y1, y2+y_step, y_step)]

        points = [(x, y) for x, y in zip(x_list, y_list)]

    for point in points:
        x, y = point
        bigmap[x][y] += 1

# Count non zeros
zum = 0
for col in bigmap:
    for item in col:
        if item > 1:
            zum += 1

print(zum)

    
    


    