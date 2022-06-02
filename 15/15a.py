from collections import defaultdict
import sys
fn = 'input.txt'
with open(fn) as fl:
    all_lines = fl.read().splitlines()

grid = defaultdict(int)
for y, line in enumerate(all_lines):
    for x, char in enumerate(line):
        grid[(y,x)] = int(char)

best = {}
y_len = len(all_lines)
x_len = len(all_lines[0])

start = (0,0)
end = (y_len-1, x_len-1)

def in_bounds(pair):
    y, x = pair
    if 0 <= y < y_len and 0 <= x < x_len:
        return True
    return False

def traverse(curr, prev_cost=0):

    curr_cost = prev_cost+grid[(curr)]

    if curr in best:
        if curr_cost >= best[curr]:
            return
    
    best[curr] = curr_cost

    y, x = curr
    for n in [(y+1,x),(y,x+1),(y,x-1),(y-1,x)]:
        if not in_bounds(n):
            continue
        traverse(n, curr_cost)

traverse(start)

print(best)

# (y, x) --> Score
print(best[end] - grid[start])

