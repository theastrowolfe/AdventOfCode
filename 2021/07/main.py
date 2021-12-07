#! /usr/bin/env python3

with open("input", "r") as fp:
    data = list(map(int, fp.read().split(',')))

#####
# Part 1
#####

sums = []
for i in range(min(data), max(data)+1):
    sums.append(sum(map(lambda x: abs(x-i), data)))
print(f'Part 1: {min(sums)}')

#####
# Part 2
#####

sums = []
for i in range(min(data), max(data)+1):
    sums.append(sum(map(lambda x: sum(range(abs(x-i)+1)), data)))
print(f'Part 2: {min(sums)}')

