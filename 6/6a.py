with open('input.txt') as fl:
    all_lines = fl.read().splitlines()

state = [int(x) for x in all_lines[0].split(',')]

for i in range(80):

    # Dec all
    dec = [fish-1 for fish in state]

    count = 0
    for pos, fish in enumerate(dec):
        if fish == -1:
            count += 1
            dec[pos] = 6

    for _ in range(count):
        dec.append(8)

    state = dec

print(len(state))

