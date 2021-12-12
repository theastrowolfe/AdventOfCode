#! /usr/bin/env python3

#####
# Data Processing
#####

with open("input", "r") as fp:
    data = list(map(lambda x: list(map(int, x)), fp.read().split('\n')[:-1]))

MIN = 0
MAX = 9

#####
# Helper Classes and Functions
#####

class Cell:
    def __init__(self, x, y, value):
        self.value = value
        self.x = x
        self.y = y

    def __repr__(self):
        return f'{self.value}'
    def __hash__(self):
        return hash((self.x, self.y))

    def __gt__(self, x):
        return self.value >  x
    def __ge__(self, x):
        return self.value >= x
    def __lt__(self, x):
        return self.value <  x
    def __le__(self, x):
        return self.value <= x
    def __eq__(self, x):
        return self.value == x
    def __ne__(self, x):
        return self.value != x

    def get_neighbors(self):
        n  = (self.x,   self.y-1)
        ne = (self.x+1, self.y-1)
        e  = (self.x+1, self.y)
        se = (self.x+1, self.y+1)
        s  = (self.x,   self.y+1)
        sw = (self.x-1, self.y+1)
        w  = (self.x-1, self.y)
        nw = (self.x-1, self.y-1)
        return n, ne, e, se, s, sw, w, nw

    def increment(self):
        self.value += 1

    def reset(self):
        self.value = 0

class Grid:
    def __init__(self, grid):
        self.grid = [[Cell(c,r,level) for c,level in enumerate(row)] for r,row in enumerate(grid)]
        self.height = len(grid)
        self.width = len(grid[0])
        self.flash_count = 0

    def __repr__(self):
        return pprint.pformat(self.grid, indent=4)

    def get_cell(self, coord):
        x, y = coord
        return self.grid[y][x]

    def is_valid_coord(self, coord):
        col, row = coord
        return col >= 0 and col < self.width and row >= 0 and row < self.height

    def flash(self, cell, flashed):
        if (cell in flashed):
            return
        flashed.add(cell)

        neighbors = [self.get_cell(coord) for coord in cell.get_neighbors() if self.is_valid_coord(coord)]
        for neighbor in neighbors:
            neighbor.increment()
            if (neighbor > MAX):
                self.flash(neighbor, flashed)

    def step(self):
        flashed = set()
        for row in self.grid:
            for cell in row:
                cell.increment()
                if (cell > MAX):
                    self.flash(cell, flashed)
        self.flash_count += len(flashed)
        for cell in flashed:
            cell.reset()
        return self

#####
# Part 1
#####

g = Grid(data)
for i in range(100):
    g.step()

print(f'Part 1: {g.flash_count}')

#####
# Part 2
#####

g = Grid(data)
for i in range(364):
    g.step()

print(f'Part 2: {i+1}')

