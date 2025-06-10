from .setting import *

class Attack(pygame.sprite.Sprite):
    def __init__(self, groups, pos):
        super().__init__(groups)
        self.image = pygame.Surface((32, 32))
        self.image.fill('white')
        self.rect = self.image.get_rect(center = pos)
        self.create_time = pygame.time.get_ticks()

    def update(self):
        if pygame.time.get_ticks() - self.create_time > 500:
            self.kill()
        return