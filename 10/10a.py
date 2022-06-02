with open('input.txt') as fl:
    all_lines = fl.read().splitlines()

a = '('
b = '['
c = '{'
d = '<'
a_c = ')'
b_c = ']'
c_c = '}'
d_c = '>'

open_to_close = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'
}

point_map = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

illegals = []

for line in all_lines:
    stack = []

    good = True

    for i, ch in enumerate(line):

        # If open, add (closing) to stack
        if ch in [a, b, c, d]:
            stack.append(open_to_close[ch])

        # If close, check
        if ch in [a_c, b_c, c_c, d_c]:

            # Match --> Del
            if ch == stack[-1]:
                del stack[-1]
            else:
                print(f'{line} - at {i} - Expected {stack[-1]}, got {ch}.')
                illegals.append(ch)
                good = False
                break

        # stack_str = ' '.join(stack)
        # print(f'Stack --> {stack_str}')

points = sum([point_map[x] for x in illegals])
print(points)

    

