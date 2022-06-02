with open('input.txt') as fl:
    all_lines = fl.read().splitlines()

output = [x.split(' | ')[1].split() for x in all_lines]

zum = 0
for line in output:
    for elem in line:
        if len(elem) in [2, 3, 4, 7]:
            zum += 1

print(zum)
"""
0: ABC EFG
1:   C  F
2: A CDE G
3: A CD FG
4:  BCD F
5: AB D FG
6: AB DEFG
7: A C  F
8: ABCDEFG
9: ABCD FG
"""

# 2, 3, 4, 7

