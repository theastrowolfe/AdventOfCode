#! /usr/bin/env python3

with open("input", "r") as fp:
    data = fp.read().split('\n')[:-1]

def binary_to_decimal(binary):
    decimal = 0
    for i in range(len(binary)):
        bit = binary[i]
        decimal += 2**(len(binary)-1-i) if bit == '1' else 0
    return decimal

def bit_count(lst, position):
    count = {'0': 0, '1': 0}
    for number in lst:
        count[number[position]] += 1
    return count

def most_common_bit(lst, position):
    bc = bit_count(lst, position)
    return '0' if bc['0'] >= bc['1'] else '1'

def least_common_bit(lst, position):
    bc = bit_count(lst, position)
    return '0' if bc['0'] <= bc['1'] else '1'

# Part 1
gamma_rate_binary = ''
for position in range(len(data[0])):
    mcb = most_common_bit(data, position)
    gamma_rate_binary += mcb
gamma_rate = binary_to_decimal(gamma_rate_binary)

epsilon_rate_binary = ''.join(list(map(lambda x: '1' if x == '0' else '0',
        gamma_rate_binary)))
epsilon_rate = binary_to_decimal(epsilon_rate_binary)

power_consumption = gamma_rate * epsilon_rate
print(f"Part 1: {power_consumption}")

# Part 2
def oxygen_generator_rating_filter(lst, bit_position = 0):
    if (len(lst) == 1):
        return lst[0]
    if (len(lst) == 2):
        return list(filter(lambda x: x[bit_position] == '1', lst))[0]
    mcb = most_common_bit(lst, bit_position)
    return oxygen_generator_rating_filter(list(filter(lambda x: x[bit_position]
        == mcb, lst)), bit_position+1)
oxygen_generator_rating_binary = oxygen_generator_rating_filter(data)
oxygen_generator_rating = binary_to_decimal(oxygen_generator_rating_binary)

def c02_scrubber_rating_filter(lst, bit_position = 0):
    if (len(lst) == 1):
        return lst[0]
    if (len(lst) == 2):
        return list(filter(lambda x: x[bit_position] == '0', lst))[0]
    lcb = least_common_bit(lst, bit_position)
    return c02_scrubber_rating_filter(list(filter(lambda x: x[bit_position] ==
        lcb, lst)), bit_position+1)
c02_scrubber_rating_binary = c02_scrubber_rating_filter(data)
c02_scrubber_rating = binary_to_decimal(c02_scrubber_rating_binary)

life_support_rating = oxygen_generator_rating * c02_scrubber_rating
print(f"Part 2: {life_support_rating}")

