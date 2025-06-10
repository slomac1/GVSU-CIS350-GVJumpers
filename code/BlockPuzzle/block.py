import pygame, sys, random, time, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import tickets_manager

def run_puzzle():
    pygame.init()

    # Basic setup
    WIDTH, HEIGHT = 600, 400
    TILE = 100
    RED = (255, 0, 0)
    WOOD = (139, 69, 19)
    BG = (245, 222, 179)
    GREEN = (0, 255, 0)
    BLACK = (0, 0, 0)
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

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

        def draw(self):
            screen.blit(self.surface, self.rect)
            pygame.draw.rect(screen, BLACK, self.rect, 2)

        def move(self, dx, dy, others):
            new_rect = self.rect.move(dx, dy)
            if new_rect.left < 0 or new_rect.top < 0 or new_rect.right > WIDTH or new_rect.bottom > HEIGHT:
                return
            for other in others:
                if other != self and other.rect.colliderect(new_rect):
                    return
            self.rect = new_rect

    # Exit box
    exit_area = pygame.Rect(WIDTH - TILE // 2, HEIGHT - TILE, TILE // 2, TILE)

    # Create blocks

    def make_blocks():
        blocks = [Block(0, 0, TILE * 2, TILE, RED, is_red=True)]
        occupied = {(0, 0), (TILE, 0)}
        positions = [(x, y) for x in range(0, WIDTH, TILE) for y in range(0, HEIGHT, TILE)]
        random.shuffle(positions)

        for _ in range(7):
            for x, y in positions:
                size = random.choice([(TILE, TILE * 2), (TILE * 2, TILE)])
                w, h = size
                if x + w > WIDTH or y + h > HEIGHT:
                    continue
                block_area = {(i, j) for i in range(x, x + w, TILE) for j in range(y, y + h, TILE)}
                if not block_area & occupied:
                    occupied |= block_area
                    blocks.append(Block(x, y, w, h, WOOD))
                    break
        return blocks

    # Main puzzle function

    def game():
        blocks = make_blocks()
        red = blocks[0]
        start_time = time.time()

        while True:
            screen.fill(BG)
            pygame.draw.rect(screen, GREEN, exit_area)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
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
                        new_x = round(b.rect.x / TILE) * TILE
                        new_y = round(b.rect.y / TILE) * TILE
                        b.move(new_x - b.rect.x, new_y - b.rect.y, blocks)
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

            for b in blocks:
                b.draw()

            # Show time left
            time_left = max(0, 20 - int(time.time() - start_time))
            font = pygame.font.SysFont(None, 24)
            screen.blit(font.render(f'Time: {time_left}s', True, BLACK), (10, HEIGHT - 30))

            if red.rect.colliderect(exit_area):
                return True
            if time.time() - start_time > 20:
                return False

            pygame.display.flip()
            clock.tick(30)

    # Run puzzle
    score = 0
    tickets = tickets_manager.load_tickets()
    for attempt in range(3):
        if game():
            score = [10, 7, 3][attempt]
            break

    # Show result
    screen.fill((255, 255, 255))
    font = pygame.font.SysFont(None, 36)
    if score:
        msg = "You have cleared the puzzle!!"
        msg2 = f"You have earned {score} points"
        tickets_manager.save_tickets(tickets + score)
    else:
        msg = "You lost. Score: 0"
        msg2 = ""
    screen.blit(font.render(msg, True, BLACK), (WIDTH // 3 - 30, HEIGHT // 2 - 20))
    screen.blit(font.render(msg2, True, BLACK), (WIDTH // 3 - 30, HEIGHT // 2 + 20))
    pygame.display.flip()
    pygame.time.wait(3000)
    pygame.quit()