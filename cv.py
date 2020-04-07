# 1. MODULES

import pygame

# 2. DISPLAY CONSTANT

WIN_H = 600
WIN_W = 800

SURFACE = pygame.display.set_mode((WIN_W, WIN_H))

# 3. GENERAL PLAY CONSTANT

FPS = 30

START_SPEED = 0.4
SPEED_UP = 0.1

# 3. GAME BOARD CONSTANT

BOX_SIZE = 24

BOX_W = 10
BOX_H = 20

BOARD_WIDTH = BOX_W * BOX_SIZE
BOARD_HEIGHT = BOX_H * BOX_SIZE

BOARD_BORDER = 5

# 4. POSITION GAME BOARD CONSTANT

SIDE_MARGIN = WIN_W // 3.5
TOP_MARGIN = WIN_H // 8

# 5. COLORS

# 5.1 General colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DEEP_BLUE = (0, 0, 140)

# 5.2 Piece outside colors
RED = (180, 30, 30)
GREEN = (40, 140, 90)
ORANGE = (230, 160, 0)
PURPLE = (150, 0, 210)
SKY = (30, 150, 230)
PINK = (200, 70, 150)
GRASS = (30, 170, 30)
BLUE = (0, 0, 230)

# 5.3 Piece inside colors
RED_IN = (200, 50, 50)
GREEN_IN = (60, 160, 90)
ORANGE_IN = (250, 180, 20)
PURPLE_IN = (170, 20, 230)
SKY_IN = (50, 170, 250)
PINK_IN = (220, 90, 170)
GRASS_IN = (50, 200, 50)
BLUE_IN = (20, 20, 250)

# 5.4 Color lists

COLOR = ['0', '1', '2', '3', '4', '5', '6', '7']    # indexes for lists COLOR_OUT and COLOR_IN

COLOR_OUT = [RED, GREEN, ORANGE, PURPLE, SKY, PINK, GRASS, BLUE]
COLOR_IN = [RED_IN, GREEN_IN, ORANGE_IN, PURPLE_IN, SKY_IN, PINK_IN, GRASS_IN, BLUE_IN]

# 6 Types of Shapes

# 6.1 Construction of shapes

A_SHAPE = [['XXXX', '....', '....', '....'],
           ['.X..', '.X..', '.X..', '.X..']]

B_SHAPE = [['.XX.', '..XX', '....', '....'],
           ['..X.', '.XX.', '.X..', '....']]

C_SHAPE = [['..XX', '.XX.', '....', '....'],
           ['.X..', '.XX.', '..X.', '....']]

D_SHAPE = [['.XX.', '.XX.', '....', '....']]

E_SHAPE = [['.X..', '.XXX', '....', '....'],
           ['.XX.', '.X..', '.X..', '....'],
           ['.XXX', '...X', '....', '....'],
           ['..X.', '..X.', '.XX.', '....']]

F_SHAPE = [['..X.', 'XXX.', '....', '....'],
           ['.XX.', '..X.', '..X.', '....'],
           ['XXX.', 'X...', '....', '....'],
           ['.X..', '.X..', '.XX.', '....']]

G_SHAPE = [['.X..', 'XXX.', '....', '....'],
           ['.X..', '.XX.', '.X..', '....'],
           ['XXX.', '.X..', '....', '....'],
           ['..X.', '.XX.', '..X.', '....']]

# 6.2 List of shapes

SHAPES = {'A': A_SHAPE,
          'B': B_SHAPE,
          'C': C_SHAPE,
          'D': D_SHAPE,
          'E': E_SHAPE,
          'F': F_SHAPE,
          'G': G_SHAPE}

# 6.3 Indexes of shapes for loops

SHAPE_IND = [0, 1, 2, 3]
