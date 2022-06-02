from collections import Counter, defaultdict

fn = 'input.txt'

with open(fn) as fl:
    all_lines = fl.read().splitlines()

rules = {}
for line in all_lines[2:]:
    ab, ins = line.split(' -> ')
    rules[ab] = ins

dd = defaultdict(int)

# Create initial
start = all_lines[0]
for i in range(len(start)-1):
    el = start[i:i+2]
    dd[el] += 1

print(dd)

print(rules)

for z in range(40):

    print(z)

    loc = defaultdict(int)
    for rkey, rval in rules.items():
        if rkey in dd:
            siz = dd[rkey]
            loc[rkey] -= siz
            loc[rkey[0]+rval] += siz
            loc[rval+rkey[1]] += siz
    
    # Add diff to dd
    for key, val in loc.items():
        dd[key] += val

print(dd)

c2 = defaultdict(int)
chars = set()

for pair, count in dd.items():
    c2[pair[1]] += count

c2['C'] += 1

print('C2')
print(c2)
print('')


# 10 steps with test:
#   {   
#       'B': 1749, 
#       'N': 865, 
#       'C': 298, 
#       'H': 161
#   }

ans = max(c2.values()) - min(c2.values())
print(ans)