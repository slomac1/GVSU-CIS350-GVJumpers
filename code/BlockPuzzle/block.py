import pygame, sys, random, time, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import tickets_manager

# Basic setup
WIDTH, HEIGHT = 1280, 720
TILE = 100
RED = '#df4a2a'
WOOD = (139, 69, 19)
BG = '#f3ad45'
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

# Simple block object
class Block:
    def __init__(self, x, y, w, h, color, is_red=False):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = color
        self.is_red = is_red
        self.dragging = False
        self.offset = (0, 0)
        self.surface = pygame.Surface((w, h))
        self.surface.fill(color)

    def draw(self, screen):
        screen.blit(self.surface, self.rect)
        pygame.draw.rect(screen, BLACK, self.rect, 2)

    def move(self, dx, dy, others):
        new_rect = self.rect.move(dx, dy)
        if new_rect.left < 340 or new_rect.top < 160 or new_rect.right > 940 or new_rect.bottom > 560:
            return
        for other in others:
            if other != self and other.rect.colliderect(new_rect):
                return
        self.rect = new_rect

class Puzzle:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True

        self.exit_area = pygame.Rect(940 - TILE // 2, 560 - TILE, TILE // 2, TILE)

        # Create blocks

    def make_blocks(self):
        blocks = [Block(340, 160, TILE * 2, TILE, RED, is_red=True)]
        occupied = {(0, 0), (TILE, 0)}
        positions = [(x, y) for x in range(0, 600, TILE) for y in range(0, 400, TILE)]
        random.shuffle(positions)

        for _ in range(7):
            for x, y in positions:
                size = random.choice([(TILE, TILE * 2), (TILE * 2, TILE)])
                w, h = size
                if x + w > 600 or y + h > 400:
                    continue
                block_area = {(i, j) for i in range(x, x + w, TILE) for j in range(y, y + h, TILE)}
                if not block_area & occupied:
                    occupied |= block_area
                    blocks.append(Block((x + 340), (y + 160), w, h, WOOD))
                    break
        return blocks
    
    def game(self):
        blocks = self.make_blocks()
        red = blocks[0]
        start_time = time.time()

        while True:
            self.screen.fill(BG)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                    return False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    for b in blocks:
                        if b.rect.collidepoint(event.pos):
                            b.dragging = True
                            b.offset = (b.rect.x - event.pos[0], b.rect.y - event.pos[1])
                elif event.type == pygame.MOUSEBUTTONUP:
                    for b in blocks:
                        b.dragging = False
                elif event.type == pygame.MOUSEMOTION:
                    for b in blocks:
                        if b.dragging:
                            mx, my = event.pos
                            dx = mx + b.offset[0] - b.rect.x
                            dy = my + b.offset[1] - b.rect.y
                            if abs(dx) > TILE // 2:
                                b.move(TILE if dx > 0 else -TILE, 0, blocks)
                            if abs(dy) > TILE // 2:
                                b.move(0, TILE if dy > 0 else -TILE, blocks)

            pygame.draw.rect(self.screen, '#f5d395', pygame.Rect(340, 160, 600, 400))
            for b in blocks:
                b.draw(self.screen)
            pygame.draw.rect(self.screen, GREEN, self.exit_area)
            pygame.draw.rect(self.screen, '#774326', pygame.Rect(340, 160, 600, 400), width = 10)

            # Show time left
            time_left = max(0, 20 - int(time.time() - start_time))
            font = pygame.font.SysFont(None, 24)
            self.screen.blit(font.render(f'Time: {time_left}s', True, BLACK), (10, HEIGHT - 30))

            if red.rect.colliderect(self.exit_area):
                return True
            if time.time() - start_time > 20:
                return False

            pygame.display.flip()
            self.clock.tick(30)

    # Run puzzle

    def run_puzzle(self):
        score = 0
        tickets = tickets_manager.load_tickets()
        for attempt in range(3):
            if self.running:
                if self.game():
                    score = [10, 7, 3][attempt]
                    break
            else:
                return

        # Show result
        self.screen.fill((255, 255, 255))
        font = pygame.font.SysFont(None, 36)
        if score:
            msg = "You have cleared the puzzle!!"
            msg2 = f"You have earned {score} tickets"
            tickets_manager.save_tickets(tickets + score)
        else:
            msg = "You lost. Score: 0"
            msg2 = ""
        self.screen.blit(font.render(msg, True, BLACK), (WIDTH // 3 - 30, HEIGHT // 2 - 20))
        self.screen.blit(font.render(msg2, True, BLACK), (WIDTH // 3 - 30, HEIGHT // 2 + 20))
        pygame.display.flip()
        pygame.time.wait(3000)
        pygame.quit()
