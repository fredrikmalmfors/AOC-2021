with open('input.txt') as fl:
    all_lines = fl.read().splitlines()

positions = [int(x) for x in all_lines[0].split(',')]

prev = 1000000000000

def fuel_cost(n):
    return (n*(n+1))/2

for i in range(1500):
    b = [fuel_cost(abs(x-i)) for x in positions]
    a = sum(b)
    if a < prev:
        print(i, a)
    prev =a

