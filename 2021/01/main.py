#! /usr/bin/env python3

with open("input", "r") as fp:
    data = list(map(lambda x: int(x), fp.read().split('\n')[:-1]))

# Part 1
cnt = 0
for i in range(1, len(data)):
    cnt += 1 if data[i] > data[i-1] else 0
print(f'Part 1: {cnt}')

# Part 2
cnt = 0
for i in range(1, len(data)-2):
    prev_three_sum = sum(data[i-1: i-1+3])
    cur_three_sum  = sum(data[i: i+3])
    cnt += 1 if cur_three_sum > prev_three_sum else 0
print(f'Part 2: {cnt}')

