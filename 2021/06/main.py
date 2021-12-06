#! /usr/bin/env python3

from functools import reduce

#####
# Data Processing
#####

with open("input", "r") as fp:
    data = list(map(int, fp.read().split(',')))

#####
# Helper Functions
#####

def timer_tick(timer):
    return timer - 1 if timer else 6

#####
# Part 1
#####

state = data.copy()
for i in range(0, 80):
    new_timers = reduce(lambda cnt, timer: cnt+1 if timer == 0 else cnt, state, 0)
    state = list(map(timer_tick, state))
    if (new_timers):
        state += [8]*new_timers

print(f'Part 1: {len(state)}')

#####
# Part 2
#####

fish = [data.count(i) for i in range(9)]
for i in range(256):
    new_timers = fish.pop(0)
    fish[6] += new_timers
    fish.append(new_timers)

print(f'Part 2: {sum(fish)}')

