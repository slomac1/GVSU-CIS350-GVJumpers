import pygame
import random
# from pygame.locals import *

CENTER = [450, 400]
WHITE = (225, 225, 225)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)


def play_darts():
    screen = pygame.display.set_mode((900, 900))
    no_darts = 15
    display_darts(no_darts, screen)
    # x, y = move_circle(454, 414, 50, no_darts, screen)

    running = True
    while running:
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                r = 50
                # while event.type != pygame.MOUSEBUTTONUP:
                #     if r > 5:
                #         r -= 1
                #     else:
                #         r += 1
                #     move_circle(x, y, r, no_darts, screen)

            elif event.type == pygame.MOUSEBUTTONUP:
                no_darts -= 1
                x = 454
                y = 414
                display_darts(no_darts, screen)
            #x, y = move_circle(x, y, 50, no_darts, screen)


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


# def move_circle(x, y, r, no, screen):
#     if r == 50:
#         x += random.randint(-10, 10)
#         y += random.randint(-10, 10)
#
#     circle = screen.convert_alpha()
#     display_darts(no, screen)
#     circle.fill([0, 0, 0, 0])
#
#     pygame.draw.circle(circle, (225, 225, 0, 220), [x, y], r, 0)
#     screen.blit(circle, (0, 0))
#     pygame.display.update()
#     return x, y


if __name__ == "__main__":
    pygame.init()
    play_darts()
    pygame.quit()
