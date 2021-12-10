#! /usr/bin/env python3

#####
# Data Processing
#####

with open("input", "r") as fp:
    data = fp.read().split('\n')[:-1]

OPENERS = '([{<'
CLOSERS = { ')':'(',
           ']':'[',
           '}':'{',
           '>':'<' }
ILLEGAL_POINTS = { ')': 3, ']': 57, '}': 1197, '>': 25137 }
AUTOCOMPLETE_POINTS = { ')': 1, ']': 2, '}': 3, '>': 4 }

#####
# Helper Functions
#####

def is_corrupt(line):
    stack = []
    for char in line:
        if (char in OPENERS):
            stack.append(char)
        else:
            if (CLOSERS[char] != stack.pop()):
                return True
    return False

def get_illegal_char(line):
    stack = []
    for char in line:
        if (char in OPENERS):
            stack.append(char)
        else:
            received = CLOSERS[char]
            expected = stack.pop()
            if (received != expected):
                return char

def complete_line(line):
    openers = { '(':')', '[':']', '{': '}', '<':'>' }
    stack = []
    for char in line:
        if (char in OPENERS):
            stack.append(char)
        else:
            stack.pop()
    return map(lambda char: openers[char], stack[::-1])

#####
# Part 1
#####

score = 0
for line in filter(is_corrupt, data):
    score += ILLEGAL_POINTS[get_illegal_char(line)]

print(f'Part 1: {score}')

#####
# Part 2
#####

scores = []
for line in filter(lambda x: not is_corrupt(x), data):
    score = 0
    autocomplete = complete_line(line)
    for char in autocomplete:
        score = (score * 5) + AUTOCOMPLETE_POINTS[char]
    scores.append(score)

print(f'Part 2: {sorted(scores)[len(scores)//2]}')

