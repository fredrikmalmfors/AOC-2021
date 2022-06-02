with open('input.txt') as fl:
    all_lines = fl.read().splitlines()

positions = [int(x) for x in all_lines[0].split(',')]

prev = 100000000000

for i in range(1500):
    a = sum([abs(x-i) for x in positions])
    if a < prev:
        print(i, a)
    prev =a

