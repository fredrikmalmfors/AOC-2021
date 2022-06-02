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
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}

scores = []

for line in all_lines:
    stack = []

    broken = False

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
                broken = True
                break

    if broken:
        continue

    if len(stack) > 0:

        # Print reversed str stack for comparison
        # rev_stack_str = ''.join(reversed(stack))
        # print(rev_stack_str)
        score = 0
        for ch in reversed(stack):
            score = (score * 5) + point_map[ch]

        scores.append(score)

scores = sorted(scores)
mid_index = len(scores) // 2
print(scores[mid_index]) 

