from collections import deque
import time
import math
import bisect
fn = 'input.txt'
with open(fn) as fl:
    all_lines = fl.read().splitlines()

aaa = time.perf_counter()

grid = {}
best = {}
prevmap = {}
for y, line in enumerate(all_lines):
    for x, char in enumerate(line):
        grid[(y,x)] = int(char)
        best[(y,x)] = math.inf
        prevmap[(y,x)] = None

y_len = len(all_lines)
x_len = len(all_lines[0])

start = (0,0)
end = (y_len-1, x_len-1)

def in_bounds(pair):
    y, x = pair
    if 0 <= y < y_len and 0 <= x < x_len:
        return True
    return False

unvisited = deque([[elem, math.inf] for elem in grid.keys()])
unvisited[0] = [start, 0]
best[start] = 0
visited = set()

while len(unvisited):

    cpair, cscore = unvisited[0]
    y, x = cpair

    for n in [(y+1,x),(y,x+1),(y,x-1),(y-1,x)]:
        if not in_bounds(n) or n in visited:
            continue

        n_score = best[n]
        if cscore + grid[n] < n_score:
            i = unvisited.index([n, n_score])
            del unvisited[i]
            best[n] = cscore + grid[n]
            prevmap[n] = cpair
            bisect.insort(unvisited, [n, best[n]])

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

