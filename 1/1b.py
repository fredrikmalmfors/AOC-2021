inc = 0
four = [None, None, None, None]

with open('input.txt') as fl:
    while True:
        line = fl.readline()
        if not line:
            break
        num = int(line)

        # Slide
        four.append(num)
        del four[0]

        if None in four:
            continue

        if sum(four[1:4]) > sum(four[0:3]):
            inc += 1

print(inc)
