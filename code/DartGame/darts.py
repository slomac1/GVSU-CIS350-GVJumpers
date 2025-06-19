import pygame, math, os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import tickets_manager

''' 
Used chatGPT for this the get_save_path. Was able to have it work with a straight path for load and save tickets.
But needed something more advanded in order to create the executable.
Also used chatGPT to create most of the art and images in the Platformer/images folder
'''

def resource_path(relative_path):
    """Use in PyInstaller to find files correctly."""
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

def image_path(filename):
    return resource_path(os.path.join("DartGame", "images", filename))

CENTER = [450, 400]
CENTER_BOARD = [454, 415]
WHITE = (225, 225, 225)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

class Darts:
    def __init__(self):
        pygame.init()
        self.tickets = tickets_manager.load_tickets()

    def play_darts(self):
        screen = pygame.display.set_mode((900, 900))
        no_darts = 15
        total = 301
        self.display_darts(no_darts, screen)
        self.display_total(screen, total)

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    pass
                elif event.type == pygame.MOUSEBUTTONUP:
                    no_darts -= 1
                    pos = pygame.mouse.get_pos()
                    self.display_darts(no_darts, screen)  # TODO, pos)
                    total = self.get_score(screen, pos, total)
                    if total == 0:
                        tickets_manager.save_tickets(self.tickets + 10)
                        running = False
                    if no_darts == 0:
                        running = False
        pygame.quit()


    def display_darts(self, no, screen):
        screen.fill((200, 200, 200))
        image = pygame.image.load(image_path('picture_dartboard.png'))
        image = pygame.transform.scale(image, (840, 640))
        screen.blit(image, (40, 90))

        image_dart = pygame.image.load(image_path('picture_dart.png'))
        image_dart = pygame.transform.scale(image_dart, (50, 100))

        for i in range(no):
            screen.blit(image_dart, (40*i, 795))

        pygame.display.update()


    def display_score(self, screen, string):
        font = pygame.font.SysFont('cambria', 32)
        text = font.render(string, True, BLACK)
        text_rect = text.get_rect()
        text_rect.center = (CENTER[0], 50)
        screen.blit(text, text_rect)
        pygame.display.update()


    def display_total(self, screen, score):
        font = pygame.font.SysFont('cambria', 20)
        text = font.render("Score: " + str(score), True, BLACK)
        text_rect = text.get_rect()
        text_rect.center = (52, 20)
        screen.blit(text, text_rect)
        pygame.display.update()


    def get_score(self, screen, pos, total):
        place_holder = total
        values = [6, 13, 4, 18, 1, 20, 5, 12, 9, 14, 11, 8, 16, 7, 19, 3, 17, 2, 15, 10]

        center_to_x = pos[0] - CENTER_BOARD[0]
        center_to_y = CENTER_BOARD[1] - pos[1]

        r = math.sqrt(center_to_x ** 2 + center_to_y ** 2)
        angle = math.degrees(math.atan2(center_to_y, center_to_x))

        trapezoid = math.floor((angle + 9) / 18)
        score = values[trapezoid]

        if r > 243:
            self.display_score(screen, "Miss")
        elif r > 222:
            self.display_score(screen, "Triple " + str(score))
            total -= score * 3
        elif r > 154:
            self.display_score(screen, str(score))
            total -= score
        elif r > 136:
            self.display_score(screen, "Double " + str(score))
            total -= score * 2
        elif r > 29:
            self.display_score(screen, str(score))
            total -= score
        elif r > 14:
            self.display_score(screen, "Bull 25")
            total -= 25
        else:
            self.display_score(screen, "Bullseye 50")
            total -= 50

        if total < 0:
            total = place_holder
            self.display_score(screen, "BUST                                      BUST")
            self.display_total(screen, total)
        else:
            self.display_total(screen, total)
        return total