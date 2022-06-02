with open('input.txt') as fl:
    all_lines = fl.read().splitlines()

b = [[int(ch) for ch in row] for row in all_lines]
y_dim = len(b)
x_dim = len(b[0])

zum = 0

for y in range(y_dim):
    for x in range(x_dim):
        
        if x+1 < x_dim:
            if not (b[y][x] < b[y][x+1]):
                continue
        
        if x-1 >= 0:
            if not (b[y][x] < b[y][x-1]):
                continue

        if y+1 < y_dim:
            if not (b[y][x] < b[y+1][x]):
                continue
        
        if y-1 >= 0:
            if not (b[y][x] < b[y-1][x]):
                continue

        zum += (b[y][x] + 1)

print(zum)