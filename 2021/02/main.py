#! /usr/bin/env python3

with open("input", "r") as fp:
    data = list(map(lambda x: x.split(' '), fp.read().split('\n')[:-1]))

# Part 1
position = {'horizontal': 0, 'depth': 0}
for move in data:
    direction = move[0]
    units = int(move[1])
    if   direction == 'forward':
        position['horizontal'] += units
    elif direction == 'down':
        position['depth'] += units
    elif direction == 'up':
        position['depth'] -= units
print(f"Part 1: {position['horizontal'] * position['depth']}")

# Part 2
position = {'aim': 0, 'horizontal': 0, 'depth': 0}
for move in data:
    direction = move[0]
    units = int(move[1])
    if   direction == 'down':
        position['aim'] += units
    elif direction == 'up':
        position['aim'] -= units
    elif direction == 'forward':
        position['horizontal'] += units
        position['depth'] += position['aim'] * units
print(f"Part 2: {position['horizontal'] * position['depth']}")

