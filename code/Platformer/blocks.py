from .setting import *

class Block(pygame.sprite.Sprite):
    def __init__(self, groups, surf, size, pos):
        super().__init__(groups)
        if surf == None:
            self.image = pygame.Surface(size)
            self.image.fill('black')
        else:
            self.image = surf
        self.rect = self.image.get_rect(center = pos)

    def update(self):
        pass
        