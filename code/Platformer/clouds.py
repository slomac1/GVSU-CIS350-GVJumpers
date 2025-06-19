from .setting import *

class Cloud(pygame.sprite.Sprite):
    def __init__(self, groups, surf, pos):
        super().__init__(groups)
        self.group = groups
        self.image = surf
        self.rect = self.image.get_rect(center = pos)
        self.last_movement = pygame.time.get_ticks()

    def update(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_movement > 10:
            self.last_movement = current_time
            self.rect.x -= 1
            if self.rect.x < 0:
                Cloud(self.group, self.image, (5000, self.rect.y))
                self.kill()
            return