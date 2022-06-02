lines = []

with open('input.txt') as fl:
    while True:
        line = fl.readline()
        if not line:
            break
        lines.append(line)

gamma = ''
epsilon = ''

# Iterate over the length of bits
for i in range(len(lines[0])-1):

    print(i)

    diff = 0
    for line in lines:
        if line[i] == '1':
            diff += 1
        else:
            diff -= 1

    if diff > 0:
        gamma += '1'
        epsilon += '0'
    else:
        gamma += '0'
        epsilon += '1'

a = int(gamma, 2)
b = int(epsilon, 2)
print(a*b)




