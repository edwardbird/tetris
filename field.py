# 1. MODULES

import random
import cv

# 2. GAME BOARD

# Create figure


def generate_shape():
    get_shape = random.choice(list(cv.SHAPES.keys()))                  # 'A'
    var_shape = random.randint(0, len(cv.SHAPES[get_shape]) - 1)       # SHAPES['A'] = A_SHAPE
    new_shape = {'type': get_shape,                   # 'A'
                 'var': var_shape,                 # index list of A_SHAPE: 0 - 3
                 'color': random.randint(0, len(cv.COLOR) - 1),   # '0', '1', '2' etc.
                 'x': (cv.BOX_W // 2) - 2,
                 'y': -4}
    return new_shape

# Add figure on game board


def add_shape(board, shape):
    new_board = board
    for x in cv.SHAPE_IND:
        for y in cv.SHAPE_IND:
            if cv.SHAPES[shape['type']][shape['var']][y][x] == 'X':
                total_x = shape['x'] + x
                total_y = shape['y'] + y
                if total_x < cv.BOX_W and total_y < cv.BOX_H:
                    if total_x >= 0 and total_x >= 0:
                        new_board[total_x][total_y] = shape['color']
    return new_board


# 3. LINE CHANGED

# Find full line


def line_complete(board):
    complete = 0
    for y in range(cv.BOX_H):
        x = 0
        while x < cv.BOX_W:
            if board[x][y] == '.':
                break
            elif x == cv.BOX_W - 1:
                complete += 1
                x += 1
            else:
                x += 1
    return complete

# Delete full line and move down lines above it


def line_clean(board):
    for y in range(cv.BOX_H):
        x = 0
        while x < cv.BOX_W:
            if board[x][y] == '.':
                break
            elif x == cv.BOX_W - 1:
                # find complete line
                for i in range(cv.BOX_W):
                    for j in range(y, -1, -1):
                        if j == 0:
                            board[i][j] = '.'
                        else:
                            board[i][j] = board[i][j - 1]
                x += 1
            else:
                x += 1


# 4. CHECKING GAME BOARD


def free_place(board, shape, move_x=0, move_y=0):
    for x in cv.SHAPE_IND:
        for y in cv.SHAPE_IND:
            tot_x = x + shape['x'] + move_x
            tot_y = y + shape['y'] + move_y
            if tot_y < 0 or cv.SHAPES[shape['type']][shape['var']][y][x] == '.':
                continue
            if tot_y >= cv.BOX_H or tot_x >= cv.BOX_W or tot_x < 0 or tot_y < 0:
                return False
            if board[tot_x][tot_y] != '.':
                return False
    return True


def check_game(board, game_over):
    if not game_over:
        for x in range(cv.BOX_W):
            if board[x][0] != '.':
                return True
    return False
