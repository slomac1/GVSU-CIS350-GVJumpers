import pygame, os, sys
from os.path import join
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
    return resource_path(os.path.join("Blackjack", "images", filename))

# Constants
CARD_WIDTH = 100
CARD_HEIGHT = 150
FPS = 60
WIDTH, HEIGHT = 800, 600
GREEN = (34, 139, 34)

# Load font
pygame.font.init()
FONT = pygame.font.SysFont('Arial', 24)

class Button:
    def __init__(self, text, x, y, w, h, callback):
        self.rect = pygame.Rect(x, y, w, h)
        self.color_idle = pygame.Color('gray15')
        self.color_hover = pygame.Color('lightskyblue')
        self.text = text
        self.font = pygame.font.SysFont('Arial', 20)
        self.callback = callback
        self.hovered = False

    def draw(self, screen):
        color = self.color_hover if self.hovered else self.color_idle
        pygame.draw.rect(screen, color, self.rect)
        pygame.draw.rect(screen, pygame.Color('white'), self.rect, 2)
        text_surface = self.font.render(self.text, True, pygame.Color('white'))
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def handle_event(self, event):
        mouse_pos = pygame.mouse.get_pos()
        self.hovered = self.rect.collidepoint(mouse_pos)
        if event.type == pygame.MOUSEBUTTONDOWN and self.hovered:
            self.callback()

class InputBox:
    def __init__(self, x, y, w, h, text=''):
        self.rect = pygame.Rect(x, y, w, h)
        self.color_inactive = pygame.Color('lightskyblue3')
        self.color_active = pygame.Color('dodgerblue2')
        self.color = self.color_inactive
        self.text = text
        self.font = pygame.font.Font(None, 32)
        self.txt_surface = self.font.render(text, True, (0, 0, 0))
        self.active = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.active = self.rect.collidepoint(event.pos)
            self.color = self.color_active if self.active else self.color_inactive
        if event.type == pygame.KEYDOWN and self.active:
            if event.key == pygame.K_RETURN:
                return int(self.text) if self.text.isdigit() else None
            elif event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
            elif event.unicode.isdigit():
                self.text += event.unicode
            self.txt_surface = self.font.render(self.text, True, (0, 0, 0))
        return None

    def draw(self, screen):
        screen.blit(self.txt_surface, (self.rect.x + 5, self.rect.y + 5))
        pygame.draw.rect(screen, self.color, self.rect, 2)

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.image = self.load_image()
        self.back = self.load_image(back=True)

    def load_image(self, back=False):
        filename = "Yellow_back.jpg" if back else f"{self.rank}{self.suit}.jpg"
        path = os.path.join(image_path(filename))
        try:
            img = pygame.image.load(path).convert()
            return pygame.transform.scale(img, (CARD_WIDTH, CARD_HEIGHT))
        except Exception as e:
            return pygame.Surface((CARD_WIDTH, CARD_HEIGHT))

class BlackjackGUI:
    def __init__(self, screen):
        self.screen = screen
        self.input_box = InputBox(30, 250, 140, 32) # x, y, w, h
        self.bet_entered = None
        self.buttons = {
            "Deal": Button("Deal", 360, 140, 300, 200, self.on_deal),
            "hit": Button("hit", 200, 540, 80, 40, self.on_hit),
            "stand": Button("stand", 300, 540, 80, 40, self.on_stand),
            "double": Button("double", 400, 540, 80, 40, self.on_double),
            "split": Button("split", 500, 540, 80, 40, self.on_split),
            "Continue": Button("Continue", 550, 340, 120, 40, self.on_continue),
            "Quit": Button("Quit", 600, 540, 120, 40, self.on_quit),

        }
        self.last_button_pressed = None
        self.active_buttons = set()
        self.persistent_cards = []

    def show_buttons(self, *button_names):
        self.active_buttons = set(button_names)

    def hide_all_buttons(self):
        self.active_buttons = set()

    def on_deal(self): 
        if self.input_box.text.isdigit():
            self.bet_entered = int(self.input_box.text)
            print(f"Bet entered from textbox: ${self.bet_entered}")
        else:
            print("Invalid bet. Please enter a number.")

    def on_hit(self): 
        print("Hit pressed")
        self.last_button_pressed = "hit"
    def on_stand(self):
        print("Stand pressed")
        self.last_button_pressed = "stand"
        print(self.last_button_pressed)
    def on_double(self):
        print("Double pressed")
        self.last_button_pressed = "double"

    def on_split(self):
        print("Split pressed")
        self.last_button_pressed = "split"
    
    def on_continue(self):
        print("Continue pressed")
        self.last_button_pressed = "continue"

    def on_quit(self):
        print("quit pressed")
        self.last_button_pressed = "Quit"


    def draw(self, eng):
        self.screen.fill(GREEN)
        self.draw_table(eng)
        self.input_box.draw(self.screen)
        for name in self.active_buttons:
            if name not in self.buttons:
                print(f"Warning: '{name}' not found in buttons dictionary.")
            else:
                self.buttons[name].draw(self.screen)
        pygame.display.flip()

    def draw_table(self, eng):
        balance_text = FONT.render(f"Balance: {eng.balance}", True, (255, 255, 255))
        self.screen.blit(balance_text, (50, HEIGHT - 80))
        bt_text = FONT.render(f"Bet Here: ", True, (255, 255, 255))
        self.screen.blit(bt_text, (50, 220))
        if self.bet_entered is not None:
            bet_text = FONT.render(f"Bet: ${self.bet_entered}", True, (255, 255, 255))
            self.screen.blit(bet_text, (50, HEIGHT - 50))
        for img, x, y in self.persistent_cards:
            self.screen.blit(img, (x, y))

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                return False
            self.input_box.handle_event(event)
            # result = self.input_box.handle_event(event)
            # if result is not None:
            #     self.bet_entered = result
            #     print(f"Confirmed bet: ${self.bet_entered}")

            for name in self.active_buttons:
                if name in self.buttons:
                    self.buttons[name].handle_event(event)
                else:
                    print(f"Warning: '{name}' is not a valid button name!")
            # Optional: Track which button was clicked
            for name in self.active_buttons:
                btn = self.buttons[name]
                if btn.hovered and event.type == pygame.MOUSEBUTTONDOWN:
                    self.last_button_pressed = btn.text

        return True

    def animate_card_flip(self, card, x, y, eng, face_up=True):
        clock = pygame.time.Clock()
        for scale in range(10, 0, -1):
            self.screen.fill(GREEN)
            self.draw_table(eng)
            scaled = pygame.transform.scale(card.back, (scale * 10, CARD_HEIGHT))
            rect = scaled.get_rect(center=(x + CARD_WIDTH // 2, y + CARD_HEIGHT // 2))
            self.screen.blit(scaled, rect.topleft)
            pygame.display.flip()
            clock.tick(FPS)
        img = card.image if face_up else card.back
        for scale in range(1, 11):
            self.screen.fill(GREEN)
            self.draw_table(eng)
            scaled = pygame.transform.scale(img, (scale * 10, CARD_HEIGHT))
            rect = scaled.get_rect(center=(x + CARD_WIDTH // 2, y + CARD_HEIGHT // 2))
            self.screen.blit(scaled, rect.topleft)
            pygame.display.flip()
            clock.tick(FPS)
        self.persistent_cards.append((img, x, y))
    
    def draw_popup(self, message):
        # Create a popup box in the center
        popup_width, popup_height = 400, 150
        popup_x = (WIDTH - popup_width) // 2
        popup_y = (HEIGHT - popup_height) // 2
        popup_rect = pygame.Rect(popup_x, popup_y, popup_width, popup_height)

        # Draw the box
        pygame.draw.rect(self.screen, pygame.Color('black'), popup_rect)
        pygame.draw.rect(self.screen, pygame.Color('white'), popup_rect, 3)

        # Render the message
        font = pygame.font.SysFont("Arial", 28, bold=True)
        text_surface = font.render(message, True, pygame.Color('white'))
        text_rect = text_surface.get_rect(center=popup_rect.center)

        self.screen.blit(text_surface, text_rect)

