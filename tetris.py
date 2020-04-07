# 1. MODULES

import sys
import time
import pygame
from pygame.locals import *

import basis
import field
import messages
import total
import cv

# 2. GAME LOOP


def game():

    # 1. INITIALIZATION BLOCK

    pygame.init()
    surface = cv.SURFACE
    pygame.display.set_caption("Tetris")
    board = basis.game_board()

    fall_time = time.time()

    play = False
    volume = 0

    start_mode = True
    play_mode = False
    help_mode = False
    game_over = False
    quit_mode = False
    best_list = False
    record_save = False
    delete_list = False

    name = ''

    font = pygame.font.SysFont("arial", 32)
    f_mn = pygame.font.SysFont("arial", 24)
    f_bg = pygame.font.SysFont("arial", 64)
    f_sp = pygame.font.SysFont("arial", 200, bold=1)

    figure = field.generate_shape()
    next_figure = field.generate_shape()

    score = 0

    pygame.mixer.music.load('tetris.mp3')
    pygame.mixer.music.play(-1, 0.0)

    # 2. GAME BLOCK

    while True:

        level = basis.level(score)
        frequency = basis.level_freq(score)

        # 1. QUIT MODE

        if not quit_mode:

            # ICON QUIT   ---   exit var 1
            if pygame.event.get(QUIT):
                quit_mode = True

            # KEY --ESC--   ---   exit var 2
            for event in pygame.event.get(KEYUP):
                if event.key == K_ESCAPE:
                    quit_mode = True

            if quit_mode:
                pygame.quit()
                sys.exit()

        # 2. START MODE

        if start_mode:
            surface.fill(cv.BLACK)
            messages.game_greeting(f_bg, f_sp)
            pygame.mixer.music.pause()

            for event in pygame.event.get(KEYDOWN):
                if event.key == K_SPACE:
                    pygame.mixer.music.unpause()
                    start_mode = False
                    play_mode = True
                    play = False

        # 3. GAME END MODE: GAME OVER MODE and RECORD SAVE MODE

        # 3.1 Game over mode

        if play_mode:
            if field.check_game(board, game_over):
                game_over = True
                play_mode = False

        if game_over:
            surface.fill(cv.PURPLE_IN)
            messages.game_end(f_bg)
            messages.result(score, level, font)

            if score > 0 and total.best_record(score):
                for event in pygame.event.get(KEYDOWN):
                    if event.key == K_SPACE:
                        game_over = False
                        record_save = True
            else:
                for event in pygame.event.get(KEYDOWN):
                    if event.key == K_SPACE:
                        board = basis.game_board()
                        score = 0
                        level = basis.level(score)
                        frequency = basis.level_freq(score)
                        game_over = False
                        start_mode = True

            # 3.2 Record save mode

        if record_save:
            surface.fill(cv.GREEN_IN)
            messages.new_best(f_bg)
            messages.input_your_name(font)
            if name != '':
                messages.continue_step(font)
            for event in pygame.event.get(KEYDOWN):
                if name == '':
                    if event.key == K_q:
                        name = name + 'Q'
                    elif event.key == K_w:
                        name = name + 'W'
                    elif event.key == K_e:
                        name = name + 'E'
                    elif event.key == K_r:
                        name = name + 'R'
                    elif event.key == K_t:
                        name = name + 'T'
                    elif event.key == K_y:
                        name = name + 'Y'
                    elif event.key == K_u:
                        name = name + 'U'
                    elif event.key == K_i:
                        name = name + 'I'
                    elif event.key == K_o:
                        name = name + 'O'
                    elif event.key == K_p:
                        name = name + 'P'
                    elif event.key == K_a:
                        name = name + 'A'
                    elif event.key == K_s:
                        name = name + 'S'
                    elif event.key == K_d:
                        name = name + 'D'
                    elif event.key == K_f:
                        name = name + 'F'
                    elif event.key == K_g:
                        name = name + 'G'
                    elif event.key == K_h:
                        name = name + 'H'
                    elif event.key == K_j:
                        name = name + 'J'
                    elif event.key == K_k:
                        name = name + 'K'
                    elif event.key == K_l:
                        name = name + 'L'
                    elif event.key == K_z:
                        name = name + 'Z'
                    elif event.key == K_x:
                        name = name + 'X'
                    elif event.key == K_c:
                        name = name + 'C'
                    elif event.key == K_v:
                        name = name + 'V'
                    elif event.key == K_b:
                        name = name + 'B'
                    elif event.key == K_n:
                        name = name + 'N'
                    elif event.key == K_m:
                        name = name + 'M'
                else:
                    if event.key == K_q:
                        name = name + 'q'
                    elif event.key == K_w:
                        name = name + 'w'
                    elif event.key == K_e:
                        name = name + 'e'
                    elif event.key == K_r:
                        name = name + 'r'
                    elif event.key == K_t:
                        name = name + 't'
                    elif event.key == K_y:
                        name = name + 'y'
                    elif event.key == K_u:
                        name = name + 'u'
                    elif event.key == K_i:
                        name = name + 'i'
                    elif event.key == K_o:
                        name = name + 'o'
                    elif event.key == K_p:
                        name = name + 'p'
                    elif event.key == K_a:
                        name = name + 'a'
                    elif event.key == K_s:
                        name = name + 's'
                    elif event.key == K_d:
                        name = name + 'd'
                    elif event.key == K_f:
                        name = name + 'f'
                    elif event.key == K_g:
                        name = name + 'g'
                    elif event.key == K_h:
                        name = name + 'h'
                    elif event.key == K_j:
                        name = name + 'j'
                    elif event.key == K_k:
                        name = name + 'k'
                    elif event.key == K_l:
                        name = name + 'l'
                    elif event.key == K_z:
                        name = name + 'z'
                    elif event.key == K_x:
                        name = name + 'x'
                    elif event.key == K_c:
                        name = name + 'c'
                    elif event.key == K_v:
                        name = name + 'v'
                    elif event.key == K_b:
                        name = name + 'b'
                    elif event.key == K_n:
                        name = name + 'n'
                    elif event.key == K_m:
                        name = name + 'm'
                    elif event.key == K_BACKSPACE or event.key == K_DELETE:
                        name = name[:-1]
                    elif event.key == K_SPACE:
                        total.add_record(name, score)
                        board = basis.game_board()
                        score = 0
                        level = basis.level(score)
                        frequency = basis.level_freq(score)
                        name = ''
                        record_save = False
                        start_mode = True
            messages.record_name(name, font)

        # GENERAL MODE: PLAY MODE, HELP MODE AND BEST LIST MODE
        # 4. PLAY MODE (It has two mods: play and pause (or play True and play False)

        if play_mode:

            # 4.1 Generation of figures

            if figure is None:
                figure = next_figure
                next_figure = field.generate_shape()

            if volume == 0:
                pygame.mixer.music.set_volume(0)
            elif volume == 1:
                pygame.mixer.music.set_volume(0.2)
            elif volume == 2:
                pygame.mixer.music.set_volume(0.4)
            elif volume == 3:
                pygame.mixer.music.set_volume(0.6)
            elif volume == 4:
                pygame.mixer.music.set_volume(0.8)
            elif volume == 5:
                pygame.mixer.music.set_volume(1)

            # 4.2 Play operators

            for event in pygame.event.get(KEYDOWN):

                # 4.2.1 General operators

                # KEY --SPACE--   ---   mode: play / pause (default mode is pause)
                if event.key == K_SPACE:
                    if help_mode:
                        help_mode = False
                    elif best_list:
                        best_list = False
                    elif delete_list:
                        delete_list = False
                    elif not play:
                        play = True
                    else:
                        play = False

                # KEY --SHIFT (left and right)--   ---   call HELP_MODE
                elif event.key == K_LSHIFT or event.key == K_RSHIFT:
                    if play:
                        play = False
                    if best_list:
                        best_list = False
                    if delete_list:
                        delete_list = False
                    if not help_mode:
                        help_mode = True

                # KEY --ALT (left and right)--   ---   call BEST_LIST_MODE
                elif event.key == K_LALT or event.key == K_RALT:
                    if play:
                        play = False
                    if help_mode:
                        help_mode = False
                    if delete_list:
                        delete_list = False
                    if not best_list:
                        best_list = True

                # KEY --DEL--   ---   clean best results
                elif event.key == K_DELETE:
                    if best_list:
                        delete_list = True
                        best_list = False

                # KEY --N--   ---   not clean best results
                elif event.key == K_n:
                    if delete_list:
                        delete_list = False
                        best_list = True

                # KEY --Y--   ---   if sure clean best results
                elif event.key == K_y:
                    if delete_list:
                        delete_list = False
                        total.delete_list()

                # KEY --PLUS--   ---   grow volume level
                elif volume < 5 and (event.key == K_PLUS or event.key == K_KP_PLUS):
                    volume += 1

                # KEY --MINUS--   ---   less volume level
                elif volume > 0 and (event.key == K_MINUS or event.key == K_KP_MINUS):
                    volume -= 1

                # 4.2.2 Operators of play mode

                # 4.2.2.1 Moving operators
                # KEY --LEFT--   ---   move left
                elif play and event.key == K_LEFT and field.free_place(board, figure, move_x=-1):
                    figure['x'] -= 1

                # KEY --RIGHT--   ---   move right
                elif play and event.key == K_RIGHT and field.free_place(board, figure, move_x=1):
                    figure['x'] += 1

                # KEY --DOWN--   ---   quick move down
                # check game board how many boxes figure can move down
                elif play and event.key == K_DOWN and field.free_place(board, figure, move_y=1):
                    fall_down = cv.BOX_H // 2
                    k = 0
                    for i in range(2, fall_down + 1):
                        if not field.free_place(board, figure, move_y=i):
                            figure['y'] += i - 1
                            k = 1
                            break
                    if k == 0:
                        figure['y'] += fall_down

                # 4.2.2.2 Rotating operators
                # KEY --UP--   ---   ROTATING
                elif play and event.key == K_UP and field.free_place(board, figure, move_y=1):
                    # create rotate figure
                    rotate = {'type': figure['type'],
                              'var': (figure['var'] + 1) % len(cv.SHAPES[figure['type']]),
                              'color': figure['color'],
                              'x': figure['x'],
                              'y': figure['y']}
                    # replaced figure on rotate figure if it can be
                    if rotate['y'] >= 0 and field.free_place(board, rotate, move_y=1):
                        figure = rotate
                    # if rotate figures has less width than current figure
                    # for figure types 'A', 'B', 'C' and 'E'
                    elif rotate['y'] >= 0 and field.free_place(board, rotate, move_x=-1, move_y=1):
                        figure = rotate
                        figure['x'] = figure['x'] - 1
                    # for figure types 'A', 'F' and 'G'
                    elif rotate['y'] >= 0 and field.free_place(board, rotate, move_x=1, move_y=1):
                        figure = rotate
                        figure['x'] = figure['x'] + 1
                    # only for figure type 'A' if it also don't replace
                    elif rotate['y'] >= 0 and field.free_place(board, rotate, move_x=-2, move_y=1):
                        figure = rotate
                        figure['x'] = figure['x'] - 2

            # 4.3 Moving

            if play:
                if time.time() - fall_time > frequency:
                    if not field.free_place(board, figure, move_y=1):
                        field.add_shape(board, figure)
                        complete = field.line_complete(board)
                        if complete > 0:
                            score += complete
                            field.line_clean(board)
                        figure = None
                    else:
                        figure['y'] += 1
                        fall_time = time.time()

            # 4.4 Drawing
            surface.fill(cv.BLACK)
            basis.game_display()  # draw display basis in center on window
            basis.game_boxes(board)  # draw game board on display
            basis.game_score(score, font)  # draw score on right up of display
            basis.game_level(level, font)  # draw level under score
            basis.next_figure(next_figure, font)  # draw word "Next" and draw next figure under level
            basis.for_play(play, f_mn)  # draw start/pause under next figure
            basis.key_help(f_mn)  # draw key for help info in left under of display
            basis.key_list(f_mn)  # draw key for to get list of best results
            basis.volume_level(volume, font)
            if figure:
                basis.game_fall(figure)  # draw current falling figure in falling position

        # 5. HELP MODE

        if help_mode:
            surface.fill(cv.BLACK)
            basis.game_display()
            messages.game_help(f_mn, font)
            basis.game_score(score, font)
            basis.game_level(level, font)
            basis.next_figure(next_figure, font)
            basis.for_play(play, f_mn)
            basis.key_list(f_mn)

        # 6. BEST LIST MODE

        if best_list:
            surface.fill(cv.BLACK)
            basis.list_display()
            messages.best_results(font)
            total.results(f_mn)
            basis.key_help(f_mn)
            basis.key_play(f_mn)
            basis.key_clean(f_mn)

        # 7. DELETE LIST MODE

        if delete_list:
            surface.fill(cv.BLACK)
            basis.warning_window()
            messages.warning_do(f_bg, font)
            basis.key_help(f_mn)
            basis.key_play(f_mn)
            basis.key_list(f_mn)

        # 7. UPDATING

        pygame.display.update()
        pygame.time.Clock().tick(cv.FPS)


# 3. SCRIPT


if __name__ == "__main__":
    game()
