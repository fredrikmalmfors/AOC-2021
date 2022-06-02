from collections import deque, Counter

fn = 'input.txt'

with open(fn) as fl:
    all_lines = fl.read().splitlines()

template = deque(x for x in all_lines[0])

rules = {}
for line in all_lines[2:]:
    ab, ins = line.split(' -> ')
    a, b = [x for x in ab]
    rules[(a, b)] = ins

for z in range(40):
    i = 0
    while True:
        if i+1 == len(template):
            break
        el = template[i]
        nx = template[i+1]
        if (el, nx) in rules:
            template.insert(i+1, rules[(el, nx)])
            i += 1
        i += 1

    print(z)
    # print(''.join(list(template)))

count_dict = Counter(list(template))

ans = max(count_dict.values()) - min(count_dict.values())
print(ans)