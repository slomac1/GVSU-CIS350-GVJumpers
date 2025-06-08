from .setting import *
import sys
import os
cur_directory = os.path.dirname(__file__)
image_directory = os.path.join(cur_directory, "images")

class Tilesheet:

    def __init__(self, filename, width, height, rows, cols):
        image = pygame.image.load(join(image_directory, f'{filename}.png')).convert_alpha()
        self.sprites = []

        for tile_x in range(0, cols):
            line = []
            self.sprites.append(line)
            for tile_y in range(0, rows):
                rect = (tile_x * width, tile_y * height, width, height)
                temp_image = image.subsurface(rect)
                mask = pygame.mask.from_surface(temp_image)
                bounding_rects = mask.get_bounding_rects()
                bounding_rect = bounding_rects[0]
                surf = pygame.Surface((bounding_rect.width, bounding_rect.height), pygame.SRCALPHA)
                surf.blit(temp_image, (0,0), area=bounding_rect)
                line.append(surf)

    def get_tile(self, x, y):
        return self.sprites[x][y]