from .setting import *

class FerrisWheel(pygame.sprite.Sprite):
    def __init__(self, groups, surf, pos):
        super().__init__(groups)
        self.original_surface = surf
        self.image = surf
        self.rect = self.image.get_rect(center = pos)
        self.rotation = 1
        self.last_movement = pygame.time.get_ticks()

    def update(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_movement > 100:
            self.last_movement = current_time
            self.image = pygame.transform.rotate(self.original_surface, self.rotation)
            self.rect = self.image.get_rect(center = self.rect.center)
            self.rotation += 1
        return