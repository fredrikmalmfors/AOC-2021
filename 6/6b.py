with open('input.txt') as fl:
    all_lines = fl.read().splitlines()

old_state = [int(x) for x in all_lines[0].split(',')]

state = [0] * 9
# Build initial state
for elem in old_state:
    state[elem] += 1

print('----')
print(state)

for i in range(256):

    """
    Shift list to left
    Append leftover to 6s and 8s
    """
    left = state.pop(0)
    state.append(left)
    state[6] += left

print(sum(state))

