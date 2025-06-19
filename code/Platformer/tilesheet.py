from .setting import *
import sys, os

def resource_path(relative_path):
    """Use in PyInstaller to find files correctly."""
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

def image_path(filename):
    return resource_path(os.path.join("Platformer", "images", filename))

class Tilesheet:

    def __init__(self, filename, width, height, rows, cols):
        image = pygame.image.load(image_path(f'{filename}.png')).convert_alpha()
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