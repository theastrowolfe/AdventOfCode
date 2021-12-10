#! /usr/bin/env python3

#####
# Data Processing
#####

with open("input", "r") as fp:
    data = list(map(lambda x: list(map(lambda y: y.split(' '), x.split(' | '))), fp.read().split('\n')[:-1]))

#####
# Constants
#####

KNOWN_LENGTHS = {
        2 : 1,
        3 : 7,
        4 : 4,
        7 : 8
        }

#####
# Part 1
#####

cnt = 0
for line in data:
    pattern, output = line
    known_digits = filter(lambda x: len(x) in KNOWN_LENGTHS.keys(), output)
    cnt += len(list(known_digits))

print(f'Part 1: {cnt}')

#####
# Part 2
#####

def count_intersections(digit, partial):
    cnt = 0
    for char in partial:
        cnt += 1 if char in digit else 0
    return cnt

def is_partial_digit(digit, partial):
    if (not partial):
        return False
    is_partial = True
    for char in partial:
        is_partial = False if not char in digit else is_partial
    return is_partial

def is_equal_digits(digit1, digit2):
    is_equal = True
    if (len(digit1) != len(digit2)):
        is_equal = False
    else:
        for char in digit1:
            is_equal = False if not char in digit2 else is_equal
    return is_equal

output_values = []
for line in data:
    pattern, output = line
    key = { 1: None, 2: None, 3: None, 4: None, 5: None,
            6: None, 7: None, 8: None, 9: None, 0: None }

    for digit in pattern:
        if (len(digit) in KNOWN_LENGTHS.keys() and
            key[KNOWN_LENGTHS[len(digit)]] == None):
            key[KNOWN_LENGTHS[len(digit)]] = digit
    for digit in pattern:
        if(len(digit) == 5):
            if (is_partial_digit(digit, key[7])):
                key[3] = digit
            elif (count_intersections(digit, key[4]) == 3):
                key[5] = digit
            else:
                key[2] = digit
        elif(len(digit) == 6):
            if (is_partial_digit(digit, key[4])):
                key[9] = digit
            elif (is_partial_digit(digit, key[7])):
                key[0] = digit
            else:
                key[6] = digit

    unscrambled = ''
    key = {v: str(k) for k, v in key.items()}
    for digit in output:
        for k in key.keys():
            if (is_equal_digits(digit, k)):
                unscrambled += key[k]
    output_values.append(int(unscrambled))

print(f'Part 2: {sum(output_values)}')

