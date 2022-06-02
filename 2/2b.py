x = 0
y = 0
aim = 0

with open('input.txt') as fl:
    while True:
        line = fl.readline()
        if not line:
            break

        cmd, num = line.split()
        num = int(num)

        if cmd == 'forward':
            x += num
            y += (num * aim)
        elif cmd == 'up':
            #y -= num
            aim -= num
        elif cmd == 'down':
            #y += num
            aim += num
        else:
            print('WTF')
            break

        print(x, y, aim)

print(x*y)
