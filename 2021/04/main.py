#! /usr/bin/env python3

#####
# Data Processing
#####

with open("input", "r") as fp:
    data = list(filter(lambda x: x, fp.read().split('\n')))
    data[0] = list(map(int, data[0].split(',')))
    for i in range(1, len(data)):
        data[i] = list(map(int, filter(lambda x: x, data[i].split(' '))))

NUMBERS = data[0]
BOARDS = []
for i in range(1, len(data), 5):
    BOARDS.append(data[i:i+5])

#####
# Helper Functions
#####

def transpose(array):
    new_array = []
    for i in range(len(array[0])):
        new_row = []
        for j in range(len(array)):
            new_row.append(array[j][i])
        new_array.append(new_row)
    return new_array

def any(array):
    for ele in array:
        if ele == True:
            return True
    return False

def all(array):
    for ele in array:
        if ele != True:
            return False
    return True

def is_winning_vertical(board):
    return is_winning_horizontal(transpose(board))

def is_winning_horizontal(board):
    return any(list(map(all, board)))

def is_winning_board(board):
    return is_winning_horizontal(board) or is_winning_vertical(board)

def score_board(board, last_number):
    unmarked_sum = 0
    for row in board:
        unmarked_sum += sum(filter(lambda x: type(x) == int,row))
    return unmarked_sum * last_number

#####
# Part 1
#####

boards = BOARDS
winning_board = False
winning_number = False
for number in NUMBERS:
    boards = list(map(lambda board: list(map(lambda row: list(map(lambda num:
        True if num == number else num, row)), board)), boards))
    for board in boards:
        if (is_winning_board(board)):
            winning_board = board
            winning_number = number
            break
    if (winning_board):
        break

print(f"Part 1: {score_board(winning_board, winning_number)}")

#####
# Part 2
#####

boards = BOARDS
winning_order = []
losing_board = False
losing_number = False
for number in NUMBERS:
    boards = list(map(lambda board: list(map(lambda row: list(map(lambda num:
        True if num == number else num, row)), board)), boards))
    for i in range(len(boards)):
        if (i in winning_order):
            continue
        if (is_winning_board(boards[i])):
            winning_order.append(i)
    if (len(winning_order) == len(boards)):
        losing_board = boards[winning_order[-1]]
        losing_number = number
        break

print(f"Part 2: {score_board(losing_board, losing_number)}")

