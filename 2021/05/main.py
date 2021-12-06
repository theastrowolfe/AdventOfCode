#! /usr/bin/env python3

from functools import reduce

#####
# Data Processing
#####

def process_line(line):
    return list(map(lambda x: tuple(map(int, x.split(','))), line.split(' -> ')))

with open("input", "r") as fp:
    data = list(map(process_line, fp.read().split('\n')[:-1]))

#####
# Helper Functions
#####

def is_horizontal_line(pair):
    return pair[0][1] == pair[1][1]

def is_vertical_line(pair):
    return pair[0][0] == pair[1][0]

def is_straight_line(pair):
    return is_horizontal_line(pair) or is_vertical_line(pair)

def is_diagonal_line(pair):
    return not is_straight_line(pair)

def pair_to_coord(pair):
    p1, p2 = pair
    x1, y1 = p1
    x2, y2 = p2
    return (x1, y1, x2, y2)

def horizontal_line(pair):
    x1, y1, x2, y2 = pair_to_coord(pair)
    if (x1 > x2):
        x1, x2 = x2, x1
        y1, y2 = y2, y1
    return list(map(lambda x: (x, y1), range(x1, x2+1)))

def vertical_line(pair):
    x1, y1, x2, y2 = pair_to_coord(pair)
    if (y1 > y2):
        x1, x2 = x2, x1
        y1, y2 = y2, y1
    return list(map(lambda y: (x1, y), range(y1, y2+1)))

def diagonal_line(pair):
    x1, y1, x2, y2 = pair_to_coord(pair)
    if (x1 > x2):
        x1, x2 = x2, x1
        y1, y2 = y2, y1

    line = []
    for i,x in enumerate(range(x1, x2+1)):
        line.append((x, y1-i if y1 > y2 else y1+i))
    return line

def line(pair):
    if is_horizontal_line(pair):
        return horizontal_line(pair)
    elif is_vertical_line(pair):
        return vertical_line(pair)
    else:
        return diagonal_line(pair)

def count_overlapping_coords(state):
    return sum(list(map(lambda row: reduce(lambda cnt, i: (cnt + 1) if i > 1 else cnt, row, 0), state)))

#####
# Constants
#####

MAX_X = 0
MAX_Y = 0
for pair in data:
    x1, y1, x2, y2 = pair_to_coord(pair)
    MAX_X = x1 if x1 > MAX_X else x2 if x2 > MAX_X else MAX_X
    MAX_Y = y1 if y1 > MAX_Y else y2 if y2 > MAX_Y else MAX_Y

#####
# Part 1
#####

state = [[0] * (MAX_X+1) for _ in range(MAX_Y+1)]
for i, pair in enumerate(filter(is_straight_line, data)):
    l = line(pair)
    for coord in l:
        x, y = coord
        state[y][x] += 1
print(f'Part 1: {count_overlapping_coords(state)}')

#####
# Part 2
#####

state = [[0] * (MAX_X+1) for _ in range(MAX_Y+1)]
for pair in data:
    l = line(pair)
    for coord in l:
        x, y = coord
        state[y][x] += 1
print(f'Part 2: {count_overlapping_coords(state)}')

