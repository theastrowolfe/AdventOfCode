#! /usr/bin/env python3

import enum

#####
# Data Processing
#####

with open("input", "r") as fp:
    data = fp.read().split('\n')[:-1]

#####
# Helper Functions and Classes
#####

class CaveType(enum.Enum):
    start = -1
    small = 0
    big   = 1
    end   = 2

class Cave:
    def __init__(self, name):
        self.id = name
        self.tunnels = set()
        if (name == 'start'):
            self.type = CaveType.start
        elif (name == 'end'):
            self.type = CaveType.end
        elif (name == name.upper()):
            self.type = CaveType.big
        elif (name == name.lower()):
            self.type = CaveType.small

    def __repr__(self):
        return f'{self.id}'
    def __hash__(self):
        return hash((self.id, self.type))

    def __eq__(self, cave):
        return self.id == cave

    def connect(self, cave):
        self.tunnels.add(cave)
        cave.tunnels.add(self)

    def isSmall(self):
        return self.type == CaveType.small

caves = []
for connection in data:
    start, end = connection.split('-')

    if (start not in caves):
        c1 = Cave(start) 
        caves.append(c1)
    else:
        c1 = caves[caves.index(start)]
    if (end not in caves):
        c2 = Cave(end)
        caves.append(c2)
    else:
        c2 = caves[caves.index(end)]

    c1.connect(c2)

START = caves[caves.index('start')]
END   = caves[caves.index('end')]

#####
# Part 1
#####

def paths1(cave, visited):
    if (cave == END):
        return 1
    if (cave.isSmall() and cave in visited):
        return 0
    
    out = 0
    for tunnel in filter(lambda t: t != START, cave.tunnels):
        out += paths1(tunnel, visited | {cave})

    return out

print(f'Part 1: {paths1(START, set())}')

#####
# Part 2
#####

def paths2(cave, visited, duplicate):
    if (cave == END):
        return 1
    if (cave.isSmall() and cave in visited):
        if (duplicate is None):
            duplicate = cave
        else:
            return 0

    out = 0
    for tunnel in filter(lambda t: t != START, cave.tunnels):
        out += paths2(tunnel, visited | {cave}, duplicate)

    return out

print(f'Part 2: {paths2(START, set(), None)}')

