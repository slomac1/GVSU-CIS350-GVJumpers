import pygame
import math
# import random
# from pygame.locals import *

CENTER = [450, 400]
CENTER_BOARD = [454, 415]
WHITE = (225, 225, 225)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)


def play_darts():
    screen = pygame.display.set_mode((900, 900))
    no_darts = 15
    total = 301
    display_darts(no_darts, screen)
    display_total(screen, total)

    running = True
    while running:
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pass
            elif event.type == pygame.MOUSEBUTTONUP:
                no_darts -= 1
                pos = pygame.mouse.get_pos()
                display_darts(no_darts, screen)  # TODO, pos)
                total = get_score(screen, pos, total)
                if total == 0:
                    return 1
                if no_darts == 0:
                    return 0


def display_darts(no, screen):
    screen.fill((200, 200, 200))
    image = pygame.image.load('picture_dartboard.png')
    image = pygame.transform.scale(image, (840, 640))
    screen.blit(image, (40, 90))

    image_dart = pygame.image.load('picture_dart.png')
    image_dart = pygame.transform.scale(image_dart, (50, 100))

    for i in range(no):
        screen.blit(image_dart, (40*i, 795))

    pygame.display.update()


def display_score(screen, string):
    font = pygame.font.SysFont('cambria', 32)
    text = font.render(string, True, BLACK)
    text_rect = text.get_rect()
    text_rect.center = (CENTER[0], 50)
    screen.blit(text, text_rect)
    pygame.display.update()


def display_total(screen, score):
    font = pygame.font.SysFont('cambria', 20)
    text = font.render("Score: " + str(score), True, BLACK)
    text_rect = text.get_rect()
    text_rect.center = (52, 20)
    screen.blit(text, text_rect)
    pygame.display.update()


def get_score(screen, pos, total):
    place_holder = total
    values = [6, 13, 4, 18, 1, 20, 5, 12, 9, 14, 11, 8, 16, 7, 19, 3, 17, 2, 15, 10]

    center_to_x = pos[0] - CENTER_BOARD[0]
    center_to_y = CENTER_BOARD[1] - pos[1]

    r = math.sqrt(center_to_x ** 2 + center_to_y ** 2)
    angle = math.degrees(math.atan2(center_to_y, center_to_x))

    trapezoid = math.floor((angle + 9) / 18)
    score = values[trapezoid]

    if r > 243:
        display_score(screen, "Miss")
    elif r > 222:
        display_score(screen, "Triple " + str(score))
        total -= score * 3
    elif r > 154:
        display_score(screen, str(score))
        total -= score
    elif r > 136:
        display_score(screen, "Double " + str(score))
        total -= score * 2
    elif r > 29:
        display_score(screen, str(score))
        total -= score
    elif r > 14:
        display_score(screen, "Bull 25")
        total -= 25
    else:
        display_score(screen, "Bullseye 50")
        total -= 50

    if total < 0:
        total = place_holder
        display_score(screen, "BUST                                      BUST")
        display_total(screen, total)
    else:
        display_total(screen, total)
    return total


if __name__ == "__main__":
    pygame.init()
    play_darts()
    pygame.quit()
