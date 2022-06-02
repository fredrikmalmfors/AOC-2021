# Read file
with open('input.txt') as fl:
    all_lines = fl.read().splitlines()

# Takes a list --> returns chosen element based on bit condition
def func(lines, oxy, pos=0):
    if len(lines) == 1: return lines[0]
    ones = [x for x in lines if x[pos] == '1']
    zero = [x for x in lines if x[pos] == '0']
    choice = ones if (len(ones) < len(zero)) ^ oxy else zero
    return func(choice, oxy, pos+1)

a = int(func(all_lines, True), 2)
b = int(func(all_lines, False), 2)
print(a*b)
