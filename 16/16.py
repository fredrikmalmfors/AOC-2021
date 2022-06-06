from math import prod
from time import perf_counter
fn = 'input.txt'

start = perf_counter()

with open(fn) as fl:
    hex_input = fl.read().splitlines()[0]

h_size = len(hex_input) * 4
inp = ( bin(int(hex_input, 16))[2:] ).zfill(h_size)
version_sum = 0

def take(i, to_int=False):
    global inp
    a = inp[:i]
    inp = inp[i:]
    if to_int:
        return int(a, 2)
    return a

def parse_packet():

    global inp
    global version_sum

    version = take(3, to_int=True)
    version_sum += version
    type_id = take(3, to_int=True)

    if type_id == 4:
        data = ''
        while True:
            has_next = take(1, to_int=True)
            data += take(4)
            if not has_next:
                break
        return int(data, 2)

    len_type_id = take(1)
    res = []

    if len_type_id == '0':
        bits_to_read = take(15, to_int=True)
        goal = len(inp) - bits_to_read
        while len(inp) > goal:
            res.append(parse_packet())
    else:
        num_of_sub = take(11, to_int=True)
        for _ in range(num_of_sub):
            res.append(parse_packet())

    match type_id:
        case 0: return sum(res)
        case 1: return prod(res)
        case 2: return min(res)
        case 3: return max(res)
        case 4: assert False
        case 5: return int(res[0] > res[1])
        case 6: return int(res[0] < res[1])
        case 7: return int(res[0] == res[1])

print(parse_packet())
print(version_sum)
end = perf_counter()
print('seconds:', end - start)

