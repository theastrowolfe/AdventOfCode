#! /usr/bin/env python3

from functools import reduce

#####
# Data Processing
#####

with open("input", "r") as fp:
    data = list(map(lambda x: list(map(int, x)), fp.read().split('\n')[:-1]))

HEIGHT = len(data)
WIDTH  = len(data[0])
MAX = 9

#####
# Helper Functions
#####

def get_value_at_coord(coord):
    try:
        row, col = coord
        return data[row][col]
    except:
        return MAX

def get_adjacent(coord):
    row, col = coord
    up, down, left, right = False, False, False, False
    if (row-1 >= 0):
        up = (row-1,col)
    if (row+1 < HEIGHT):
        down = (row+1,col)
    if (col-1 >= 0):
        left = (row,col-1)
    if (col+1 < WIDTH):
        right = (row,col+1)
    return up, down, left, right

def get_basin_helper(coord, visited, basin):
    if (coord in visited):
        return
    visited.add(coord)
    if (get_value_at_coord(coord) == MAX):
        return

    basin.add(coord)

    for coord in get_adjacent(coord):
        get_basin_helper(coord, visited, basin)

def get_basin(coord):
    basin = set()
    get_basin_helper(coord, set(), basin)
    return basin

#####
# Part 1
#####

low_points = []
for r,row in enumerate(data):
    for c,col in enumerate(row):
        if (col < min(map(get_value_at_coord, get_adjacent((r, c))))):
            low_points.append(col)

print(f'Part 1: {sum(low_points)+len(low_points)}')

#####
# Part 2
#####

basins = []
for r,row in enumerate(data):
    for c,col in enumerate(row):
        if (col < min(map(get_value_at_coord, get_adjacent((r, c))))):
            basins.append(get_basin((r, c)))

print(f'Part 2: {reduce(lambda x,y: x*y, sorted(map(len, basins))[-3:])}')

