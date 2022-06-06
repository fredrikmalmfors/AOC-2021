import time
import math
from heapq import heapify, heappop, heappush
fn = 'input.txt'
with open(fn) as fl:
    all_lines = fl.read().splitlines()

aaa = time.perf_counter()
y_len = len(all_lines)
x_len = len(all_lines[0])
grid = {}
best = {}
# prevmap = {}
for y, line in enumerate(all_lines):
    for x, char in enumerate(line):
        risk = int(char)
        for j in range(5):
            for k in range(5):
                zooz = j+k
                grid[(y + (j*y_len), x + (k*x_len))] = ((risk + zooz - 1) % 9) + 1

best = {(y,x): math.inf for y,x in grid.keys()}
# prevmap = {(y,x): None for y,x in grid.keys()}

start = (0,0)
end = (y_len*5-1, x_len*5-1)

def in_bounds(pair):
    y, x = pair
    if 0 <= y < y_len*5 and 0 <= x < x_len*5:
        return True
    return False

unvisited = [(math.inf, elem) for elem in grid.keys()]
unvisited[0] = (0, start)
heapify(unvisited)
best[start] = 0
visited = set()

for aa in range(y_len*5):
    shi = ''
    for bb in range(x_len*5):
        shi += str(grid[(aa,bb)])
    # print(shi)

while len(unvisited):

    if len(unvisited) % 100 == 0:
        print(len(unvisited), '/', len(grid))

    cscore, cpair = heappop(unvisited)

    y, x = cpair

    for n in [(y+1,x),(y,x+1),(y,x-1),(y-1,x)]:
        if not in_bounds(n) or n in visited:
            continue

        n_score = best[n]
        if cscore + grid[n] < n_score:
            unvisited.remove((n_score, n))
            best[n] = cscore + grid[n]
            heappush(unvisited, (best[n], n))

    del unvisited[0]
    visited.add(cpair)

bbb = time.perf_counter()

print(bbb - aaa)
print(best[end])

# Backtrack
# a = end
# z = []
# while True:
#     print(a)
#     z.append(a)
#     if a == start:
#         break
#     a = grid[a][2]

# for y, line in enumerate(all_lines):
#     bish = ''
#     for x, char in enumerate(line):
#         if (y,x) in z:
#             bish += 'X'
#         else:
#             bish += ' '
#     print(bish)


# pprint(grid)

