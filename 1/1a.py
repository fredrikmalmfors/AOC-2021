increases = 0
prev = None

with open('input.txt') as fl:
    prev = int(fl.readline())
    while True:
        line = fl.readline()
        if not line:
            break
        num = int(line)
        if num > prev:
            increases += 1
        prev = num

print(increases)
