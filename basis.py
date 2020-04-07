# 1. MODULES

import pygame
import cv


# 2. INITIALIZATION


def level(score):
    level_is = score // 10 + 1
    return level_is


def level_freq(score):
    frequency = cv.START_SPEED / (1 + ((score // 10) * cv.SPEED_UP))
    return frequency


# 3. GAME BOARD


def game_display():
    # 1. Game surface - display border + place for border
    pygame.draw.rect(cv.SURFACE, cv.DEEP_BLUE,
                     (cv.SIDE_MARGIN - 6, cv.TOP_MARGIN - 6, cv.BOARD_WIDTH + 15, cv.BOARD_HEIGHT + 15))
    # 2. Game display
    pygame.draw.rect(cv.SURFACE, cv.WHITE,
                     (cv.SIDE_MARGIN - 1, cv.TOP_MARGIN - 1, cv.BOARD_WIDTH + 5, cv.BOARD_HEIGHT + 5))


def game_board():
    board = []
    for i in range(cv.BOX_W):
        board.append(['.'] * cv.BOX_H)
    return board


def game_boxes(board):
    for x in range(cv.BOX_W):
        for y in range(cv.BOX_H):
            if board[x][y] != '.':
                # + 1 is offset frame game display
                box_x = cv.SIDE_MARGIN + x * cv.BOX_SIZE + 1
                box_y = cv.TOP_MARGIN + y * cv.BOX_SIZE + 1
                # Draw boxes
                pygame.draw.rect(cv.SURFACE, cv.COLOR_OUT[int(board[x][y])],
                                 (box_x + 1, box_y + 1, cv.BOX_SIZE - 1, cv.BOX_SIZE - 1))
                # Stylization boxes
                pygame.draw.rect(cv.SURFACE, cv.COLOR_IN[int(board[x][y])],
                                 (box_x + 4, box_y + 4, cv.BOX_SIZE - 7, cv.BOX_SIZE - 7))


def game_fall(figure):
    for y in cv.SHAPE_IND:
        for x in cv.SHAPE_IND:
            if cv.SHAPES[figure['type']][figure['var']][y][x] != '.':
                box_x = cv.SIDE_MARGIN + (x + figure['x']) * cv.BOX_SIZE + 1
                box_y = cv.TOP_MARGIN + (y + figure['y']) * cv.BOX_SIZE + 1
                # For draw only game board, coord y must be 0 and more
                if y + figure['y'] >= 0:
                    # Draw boxes
                    pygame.draw.rect(cv.SURFACE, cv.COLOR_OUT[int(figure['color'])],
                                     (box_x + 1, box_y + 1, cv.BOX_SIZE - 1, cv.BOX_SIZE - 1))
                    # Stylization boxes
                    pygame.draw.rect(cv.SURFACE, cv.COLOR_IN[int(figure['color'])],
                                     (box_x + 4, box_y + 4, cv.BOX_SIZE - 7, cv.BOX_SIZE - 7))


# 4. GAME STATUS


def game_score(score, font):
    score_box = font.render("Score:  {}".format(score), 1, cv.WHITE)
    cv.SURFACE.blit(score_box, (cv.WIN_W - cv.SIDE_MARGIN, cv.TOP_MARGIN))


def game_level(rank_level, font):
    score_box = font.render("Level:   {}".format(rank_level), 1, cv.WHITE)
    cv.SURFACE.blit(score_box, (cv.WIN_W - cv.SIDE_MARGIN, 2 * cv.TOP_MARGIN))


def next_figure(next_shape, font):
    called_box = font.render("Next:", 1, cv.WHITE)
    cv.SURFACE.blit(called_box, (cv.WIN_W - cv.SIDE_MARGIN, 3 * cv.TOP_MARGIN))
    for y in cv.SHAPE_IND:
        for x in cv.SHAPE_IND:
            box_y = cv.WIN_W - cv.SIDE_MARGIN + (y * cv.BOX_SIZE + 1)
            box_x = (4 * cv.TOP_MARGIN) + (x * cv.BOX_SIZE + 1)
            if cv.SHAPES[next_shape['type']][next_shape['var']][x][y] != '.':
                # Draw boxes
                pygame.draw.rect(cv.SURFACE, cv.COLOR_OUT[int(next_shape['color'])],
                                 (box_y + 1, box_x + 1, cv.BOX_SIZE - 1, cv.BOX_SIZE - 1))
                # Stylization boxes
                pygame.draw.rect(cv.SURFACE, cv.COLOR_IN[int(next_shape['color'])],
                                 (box_y + 4, box_x + 4, cv.BOX_SIZE - 7, cv.BOX_SIZE - 7))
            else:
                # Draw background default boxes while color boxes forward figures can be
                pygame.draw.rect(cv.SURFACE, cv.BLACK,
                                 (box_y + 1, box_x + 1, cv.BOX_SIZE - 1, cv.BOX_SIZE - 1))


# 5. OPTIONS


def for_play(play, font):
    press = font.render("Press", 1, cv.ORANGE_IN)
    cv.SURFACE.blit(press, (int(cv.WIN_W * 0.75), int(5.5 * cv.TOP_MARGIN)))
    space = font.render("SPACE", 1, cv.ORANGE_IN)
    cv.SURFACE.blit(space, (int(cv.WIN_W * 0.75), 6 * cv.TOP_MARGIN))
    if play:
        mode_select = font.render("to pause", 1, cv.ORANGE_IN)
        cv.SURFACE.blit(mode_select, (int(cv.WIN_W * 0.75), int(6.5 * cv.TOP_MARGIN)))
    else:
        mode_select = font.render("to continue", 1, cv.ORANGE_IN)
        cv.SURFACE.blit(mode_select, (int(cv.WIN_W * 0.75), int(6.5 * cv.TOP_MARGIN)))


def key_help(font):
    help_press = font.render("Press", 1, cv.WHITE)
    cv.SURFACE.blit(help_press, (int(cv.WIN_W * 0.1), int(5.5 * cv.TOP_MARGIN)))
    help_button = font.render("SHIFT", 1, cv.WHITE)
    cv.SURFACE.blit(help_button, (int(cv.WIN_W * 0.1), 6 * cv.TOP_MARGIN))
    help_voice = font.render("to get help", 1, cv.WHITE)
    cv.SURFACE.blit(help_voice, (int(cv.WIN_W * 0.1), int(6.5 * cv.TOP_MARGIN)))


def key_list(font):
    list_press = font.render("Press", 1, cv.WHITE)
    cv.SURFACE.blit(list_press, (int(cv.WIN_W * 0.1), int(3.5 * cv.TOP_MARGIN)))
    list_button = font.render("ALT", 1, cv.WHITE)
    cv.SURFACE.blit(list_button, (int(cv.WIN_W * 0.1), 4 * cv.TOP_MARGIN))
    list_voice = font.render("List of best", 1, cv.WHITE)
    cv.SURFACE.blit(list_voice, (int(cv.WIN_W * 0.1), int(4.5 * cv.TOP_MARGIN)))


# 6. BEST LIST


def list_display():
    pygame.draw.rect(cv.SURFACE, cv.RED,
                     (cv.SIDE_MARGIN - 6, cv.TOP_MARGIN - 6, 2 * cv.BOARD_WIDTH + 15, cv.BOARD_HEIGHT + 15))
    pygame.draw.rect(cv.SURFACE, cv.WHITE,
                     (cv.SIDE_MARGIN - 1, cv.TOP_MARGIN - 1, 2 * cv.BOARD_WIDTH + 5, cv.BOARD_HEIGHT + 5))


def warning_window():
    pygame.draw.rect(cv.SURFACE, cv.BLUE,
                     (cv.SIDE_MARGIN - 6, cv.TOP_MARGIN - 6, 2 * cv.BOARD_WIDTH + 15, cv.BOARD_HEIGHT + 15))
    pygame.draw.rect(cv.SURFACE, cv.SKY_IN,
                     (cv.SIDE_MARGIN - 1, cv.TOP_MARGIN - 1, 2 * cv.BOARD_WIDTH + 5, cv.BOARD_HEIGHT + 5))


def key_play(font):
    help_press = font.render("Press", 1, cv.ORANGE_IN)
    cv.SURFACE.blit(help_press, (int(cv.WIN_W * 0.1), int(1 * cv.TOP_MARGIN)))
    help_button = font.render("SPACE", 1, cv.ORANGE_IN)
    cv.SURFACE.blit(help_button, (int(cv.WIN_W * 0.1), 1.5 * cv.TOP_MARGIN))
    help_voice = font.render("to continue", 1, cv.ORANGE_IN)
    cv.SURFACE.blit(help_voice, (int(cv.WIN_W * 0.1), int(2 * cv.TOP_MARGIN)))


def key_clean(font):
    list_press = font.render("Press", 1, cv.WHITE)
    cv.SURFACE.blit(list_press, (int(cv.WIN_W * 0.1), int(3.5 * cv.TOP_MARGIN)))
    list_button = font.render("DEL", 1, cv.WHITE)
    cv.SURFACE.blit(list_button, (int(cv.WIN_W * 0.1), 4 * cv.TOP_MARGIN))
    list_voice = font.render("Clear list", 1, cv.WHITE)
    cv.SURFACE.blit(list_voice, (int(cv.WIN_W * 0.1), int(4.5 * cv.TOP_MARGIN)))

# 7. VOLUME


def volume_level(volume, font):
    v_level = font.render("Volume: {}".format(volume), 1, cv.WHITE)
    cv.SURFACE.blit(v_level, (int(cv.WIN_W * 0.075), cv.TOP_MARGIN))
