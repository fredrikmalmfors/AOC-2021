with open('input.txt') as fl:
    all_lines = fl.read().splitlines()

tot_sum = 0

for line in all_lines:
    input_list, output_list = [[''.join(sorted(x)) for x in a.split()] for a in line.split(' | ')]

    # actual --> wrong
    wiremap = {
        'a': None,
        'b': None,
        'c': None,
        'd': None,
        'e': None,
        'f': None,
        'g': None
    }

    # index = digit, value = signal
    digitmap = [None, None, None, None, None, None, None, None, None, None]

    # Lay out simple ones
    for elem in input_list:
        _len = len(elem)
        if _len == 2: digitmap[1] = elem
        if _len == 3: digitmap[7] = elem
        if _len == 4: digitmap[4] = elem
        if _len == 7: digitmap[8] = elem

    # The letter that is in 7 but not in 1 --> A
    for ch in digitmap[7]:
        if ch not in digitmap[1]:
            wiremap['a'] = ch

    # count the number of "f" and "c"
    ch0 = digitmap[1][0]
    ch1 = digitmap[1][1]
    count = len([x for x in input_list if ch0 in x])
    wiremap['c'] = ch0 if count == 8 else ch1
    wiremap['f'] = ch1 if count == 8 else ch0

    for elem in input_list:

        # Find digitmap for 2, 3 and 5 
        if len(elem) == 5:

            # 2
            if (wiremap['c'] in elem) and (wiremap['f'] not in elem):
                digitmap[2] = elem

            # 3
            if (wiremap['c'] in elem) and (wiremap['f'] in elem):
                digitmap[3] = elem

            # 5
            if (wiremap['c'] not in elem) and (wiremap['f'] in elem):
                digitmap[5] = elem

        # Find digitmap for 6
        if len(elem) == 6:

            # 6
            if (wiremap['c'] not in elem):
                digitmap[6] = elem
            
            # Elem is either 0 or 9
            else:
                for ch in digitmap[8]:
                    if ch not in elem:
                        # ch is either D or E
                        if ch in digitmap[4]:
                            digitmap[0] = elem
                        else:
                            digitmap[9] = elem

    # Done, now apply on output
    decode_str = ''
    for elem in output_list:
        digit = digitmap.index(elem)
        decode_str += str(digit)

    tot_sum = int(decode_str)

    # print('RES', res)
    # print('--- Digitmap ---')
    # print(digitmap)
    # print('--- Wiremap ---')
    # print(wiremap)

print(tot_sum)