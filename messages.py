# 1. MODULES

import cv

# 2. START MODE


def game_greeting(font, font_s):

    t1 = font_s.render("T", 1, cv.RED)
    cv.SURFACE.blit(t1, (int(cv.WIN_W * 0.05), int(cv.TOP_MARGIN * 1)))
    e2 = font_s.render("E", 1, cv.SKY)
    cv.SURFACE.blit(e2, (int(cv.WIN_W * 0.2), int(cv.TOP_MARGIN * 1)))
    t3 = font_s.render("T", 1, cv.PINK)
    cv.SURFACE.blit(t3, (int(cv.WIN_W * 0.37), int(cv.TOP_MARGIN * 1)))
    r4 = font_s.render("R", 1, cv.GRASS)
    cv.SURFACE.blit(r4, (int(cv.WIN_W * 0.53), int(cv.TOP_MARGIN * 1)))
    i5 = font_s.render("I", 1, cv.PURPLE)
    cv.SURFACE.blit(i5, (int(cv.WIN_W * 0.72), int(cv.TOP_MARGIN * 1)))
    s6 = font_s.render("S", 1, cv.GREEN)
    cv.SURFACE.blit(s6, (int(cv.WIN_W * 0.8), int(cv.TOP_MARGIN * 1)))

    prs = font.render("PRESS SPACE", 1, cv.ORANGE_IN)
    cv.SURFACE.blit(prs, (int(cv.SIDE_MARGIN // 1.2), int(cv.TOP_MARGIN * 5)))
    stt = font.render("TO START", 1, cv.ORANGE_IN)
    cv.SURFACE.blit(stt, (int(cv.SIDE_MARGIN * 1.05), int(cv.TOP_MARGIN * 6)))


# 2. GAME OVER MODE


def game_end(font):
    status = font.render("GAME OVER", 1, cv.ORANGE)
    cv.SURFACE.blit(status, (int(cv.WIN_W * 0.25), cv.TOP_MARGIN * 2))


def result(score, level_q, font):
    scr = font.render("YOUR SCORE IS {}".format(score), 1, cv.WHITE)
    cv.SURFACE.blit(scr, (cv.SIDE_MARGIN - 20, cv.TOP_MARGIN * 4))
    lvl = font.render("YOUR LAST LEVEL IS {}".format(level_q), 1, cv.WHITE)
    cv.SURFACE.blit(lvl, (cv.SIDE_MARGIN - 20, cv.TOP_MARGIN * 5))
    stt = font.render("PRESS SPACE TO CONTINUE", 1, cv.ORANGE_IN)
    cv.SURFACE.blit(stt, (cv.SIDE_MARGIN // 1.2, cv.TOP_MARGIN * 7))


# 3. HELP MODE


def game_help(font, font_s):

    help_to = font_s.render("HELP", 1, cv.BLACK)
    cv.SURFACE.blit(help_to, (int(cv.SIDE_MARGIN * 1.35), int(cv.TOP_MARGIN * 1.2)))

    esc = font.render("ESC", 1, cv.BLACK)
    cv.SURFACE.blit(esc, (int(cv.SIDE_MARGIN * 1.05), int(cv.TOP_MARGIN * 2)))
    esc_p = font.render("Exit", 1, cv.BLACK)
    cv.SURFACE.blit(esc_p, (int(cv.SIDE_MARGIN * 1.45), int(cv.TOP_MARGIN * 2)))
    spc = font.render("SPACE", 1, cv.BLACK)
    cv.SURFACE.blit(spc, (int(cv.SIDE_MARGIN * 1.05), int(cv.TOP_MARGIN * 2.4)))
    spc_p = font.render("Play/Pause", 1, cv.BLACK)
    cv.SURFACE.blit(spc_p, (int(cv.SIDE_MARGIN * 1.45), int(cv.TOP_MARGIN * 2.4)))
    shf = font.render("SHIFT", 1, cv.BLACK)
    cv.SURFACE.blit(shf, (int(cv.SIDE_MARGIN * 1.05), int(cv.TOP_MARGIN * 2.8)))
    shf_p = font.render("Show help", 1, cv.BLACK)
    cv.SURFACE.blit(shf_p, (int(cv.SIDE_MARGIN * 1.45), int(cv.TOP_MARGIN * 2.8)))
    alt = font.render("ALT", 1, cv.BLACK)
    cv.SURFACE.blit(alt, (int(cv.SIDE_MARGIN * 1.05), int(cv.TOP_MARGIN * 3.2)))
    alt_p = font.render("Best results", 1, cv.BLACK)
    cv.SURFACE.blit(alt_p, (int(cv.SIDE_MARGIN * 1.45), int(cv.TOP_MARGIN * 3.2)))

    lef = font.render("LEFT", 1, cv.BLACK)
    cv.SURFACE.blit(lef, (int(cv.SIDE_MARGIN * 1.05), int(cv.TOP_MARGIN * 4)))
    lef_p = font.render("Move left", 1, cv.BLACK)
    cv.SURFACE.blit(lef_p, (int(cv.SIDE_MARGIN * 1.45), int(cv.TOP_MARGIN * 4)))
    rgt = font.render("RIGHT", 1, cv.BLACK)
    cv.SURFACE.blit(rgt, (int(cv.SIDE_MARGIN * 1.05), int(cv.TOP_MARGIN * 4.4)))
    rgt_p = font.render("Move right", 1, cv.BLACK)
    cv.SURFACE.blit(rgt_p, (int(cv.SIDE_MARGIN * 1.45), int(cv.TOP_MARGIN * 4.4)))
    dwn = font.render("DOWN", 1, cv.BLACK)
    cv.SURFACE.blit(dwn, (int(cv.SIDE_MARGIN * 1.05), int(cv.TOP_MARGIN * 4.8)))
    dwn_p = font.render("Move down", 1, cv.BLACK)
    cv.SURFACE.blit(dwn_p, (int(cv.SIDE_MARGIN * 1.45), int(cv.TOP_MARGIN * 4.8)))
    upp = font.render("UP", 1, cv.BLACK)
    cv.SURFACE.blit(upp, (int(cv.SIDE_MARGIN * 1.05), int(cv.TOP_MARGIN * 5.2)))
    upp_p = font.render("Rotate", 1, cv.BLACK)
    cv.SURFACE.blit(upp_p, (int(cv.SIDE_MARGIN * 1.45), int(cv.TOP_MARGIN * 5.2)))

    upp = font.render("+", 1, cv.BLACK)
    cv.SURFACE.blit(upp, (int(cv.SIDE_MARGIN * 1.05), int(cv.TOP_MARGIN * 6)))
    upp_p = font.render("Up volume", 1, cv.BLACK)
    cv.SURFACE.blit(upp_p, (int(cv.SIDE_MARGIN * 1.45), int(cv.TOP_MARGIN * 6)))
    upp = font.render("-", 1, cv.BLACK)
    cv.SURFACE.blit(upp, (int(cv.SIDE_MARGIN * 1.05), int(cv.TOP_MARGIN * 6.4)))
    upp_p = font.render("Down volume", 1, cv.BLACK)
    cv.SURFACE.blit(upp_p, (int(cv.SIDE_MARGIN * 1.45), int(cv.TOP_MARGIN * 6.4)))


# 4. BEST LIST


def best_results(font_s):
    best = font_s.render("BEST RESULTS", 1, cv.BLACK)
    cv.SURFACE.blit(best, (int(cv.SIDE_MARGIN * 1.6), int(cv.TOP_MARGIN * 1.2)))


def new_best(font):
    best_result = font.render("YOU HAVE BEST RESULT", 1, cv.BLACK)
    cv.SURFACE.blit(best_result, (int(cv.WIN_W * 0.02), int(cv.TOP_MARGIN * 1.4)))


def input_your_name(font):
    best_result = font.render("INPUT YOUR NAME", 1, cv.BLACK)
    cv.SURFACE.blit(best_result, (int(cv.WIN_W * 0.3), int(cv.TOP_MARGIN * 4)))


def record_name(name, font):
    winner = font.render(name, 1, cv.PURPLE)
    cv.SURFACE.blit(winner, (int(cv.WIN_W * 0.4), int(cv.TOP_MARGIN * 5)))


def continue_step(font):
    winner_save = font.render("PRESS SPACE", 1, cv.BLACK)
    cv.SURFACE.blit(winner_save, (int(cv.WIN_W * 0.35), int(cv.TOP_MARGIN * 6)))


def warning_do(font_s, font):
    warning = font_s.render("DO YOU SURE", 1, cv.BLACK)
    cv.SURFACE.blit(warning, (int(cv.WIN_W * 0.3), int(cv.TOP_MARGIN * 2)))
    warning = font_s.render("DELETE?", 1, cv.BLACK)
    cv.SURFACE.blit(warning, (int(cv.WIN_W * 0.4), int(cv.TOP_MARGIN * 3.5)))
    yes = font.render("Y - YES", 1, cv.BLACK)
    cv.SURFACE.blit(yes, (int(cv.WIN_W * 0.4), int(cv.TOP_MARGIN * 6)))
    no = font.render("N - NOT", 1, cv.BLACK)
    cv.SURFACE.blit(no, (int(cv.WIN_W * 0.6), int(cv.TOP_MARGIN * 6)))
