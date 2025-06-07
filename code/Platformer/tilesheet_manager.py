from tilesheet import Tilesheet
from setting import *

def create_tilesheets():
        ground_tilesheet = Tilesheet('update_tile_blocks', 228, 214, 2, 4)
        wheel_tilesheet =  Tilesheet('ferris_wheel', 1024, 1024, 1, 1)
        dart_booth_tilesheet = Tilesheet('dart_game_booth', 1024, 1024, 1, 1)
        puzzle_booth_tilesheet = Tilesheet('puzzle_game_booth', 1024, 1024, 1, 1)
        cards_booth_tilesheet = Tilesheet('cards_game_booth', 1024, 1024, 1, 1)
        tent_tilesheet = Tilesheet('tent', 1024, 1024, 1, 1)
        tent_ground_tilsheet = Tilesheet('tent_ground_tiles', 209, 212, 2, 4)
        scaffolding_tilesheet1 = Tilesheet('scaffolding_sides', 170, 147, 2, 2)
        scaffolding_tilesheet2 = Tilesheet('scaffolding_short', 155, 77, 2, 2)
        scaffolding_tilesheet3 = Tilesheet('scaffolding_long', 512, 76, 1, 1)
        fence_tilesheet = Tilesheet('fence_tiles', 215, 131, 2, 2)
        archway_tilesheet = Tilesheet('archways', 241, 221, 1, 2)
        tiles = {
            'grass1' : pygame.transform.scale(ground_tilesheet.get_tile(0,0), (256, 256)),
            'grass2' : pygame.transform.scale(ground_tilesheet.get_tile(1,0), (256, 256)),
            'grass_right' : pygame.transform.scale(ground_tilesheet.get_tile(2,0), (256, 256)),
            'grass_left' : pygame.transform.scale(ground_tilesheet.get_tile(3,0), (256, 256)),
            'dirt1_light' : pygame.transform.scale(ground_tilesheet.get_tile(0,1), (256, 256)),
            'dirt2_light' : pygame.transform.scale(ground_tilesheet.get_tile(1,1), (256, 256)),
            'dirt_right_light' : pygame.transform.scale(ground_tilesheet.get_tile(2,1), (256, 256)),
            'dirt_left_light' : pygame.transform.scale(ground_tilesheet.get_tile(3,1), (256, 256)),
            'ferris_wheel' : pygame.transform.scale(wheel_tilesheet.get_tile(0,0), (1024, 1024)),
            'dart_booth': pygame.transform.scale(dart_booth_tilesheet.get_tile(0,0), (256, 256)),
            'puzzle_booth': pygame.transform.scale(puzzle_booth_tilesheet.get_tile(0,0), (256, 256)),
            'card_booth': pygame.transform.scale(cards_booth_tilesheet.get_tile(0,0), (256, 256)),
            'tent': pygame.transform.scale(tent_tilesheet.get_tile(0,0), (512, 512)),
            'dirt_top1_dark': pygame.transform.scale(tent_ground_tilsheet.get_tile(0,0), (256,256)),
            'dirt_top2_dark': pygame.transform.scale(tent_ground_tilsheet.get_tile(0,1), (256,256)),
            'dirt_left_dark': pygame.transform.scale(tent_ground_tilsheet.get_tile(2,0), (256,256)),
            'dirt_right_dark': pygame.transform.scale(tent_ground_tilsheet.get_tile(2,1), (256,256)),
            'dirt_topleft_dark': pygame.transform.scale(tent_ground_tilsheet.get_tile(1,0), (256,256)),
            'dirt_topright_dark': pygame.transform.scale(tent_ground_tilsheet.get_tile(1,1), (256,256)),
            'dirt1_dark': pygame.transform.scale(tent_ground_tilsheet.get_tile(3,0), (256,256)),
            'dirt2_dark': pygame.transform.scale(tent_ground_tilsheet.get_tile(3,1), (256,256)),
            'side_double': pygame.transform.scale(scaffolding_tilesheet1.get_tile(0,0), (128, 256)),
            'side_single': pygame.transform.scale(scaffolding_tilesheet1.get_tile(0,1), (128, 256)),
            'side_doubletop': pygame.transform.scale(scaffolding_tilesheet1.get_tile(1,1), (128, 256)),
            'side_singletop': pygame.transform.scale(scaffolding_tilesheet1.get_tile(1,0), (128, 256)),
            'short_full': pygame.transform.scale(scaffolding_tilesheet2.get_tile(0,0), (128, 64)),
            'short_left': pygame.transform.scale(scaffolding_tilesheet2.get_tile(0,1), (128, 64)),
            'short_middle': pygame.transform.scale(scaffolding_tilesheet2.get_tile(1,0), (128, 64)),
            'short_right': pygame.transform.scale(scaffolding_tilesheet2.get_tile(1,1), (128, 64)),
            'long': pygame.transform.scale(scaffolding_tilesheet3.get_tile(0,0), (512, 64)),
            'archway_open' : pygame.transform.scale(archway_tilesheet.get_tile(0,0), (280, 280)),
            'archway_close' : pygame.transform.scale(archway_tilesheet.get_tile(1,0), (280, 280)),
            'fence_post_left' : pygame.transform.scale(fence_tilesheet.get_tile(0,0), (256, 152)),
            'fence_post_right' : pygame.transform.scale(fence_tilesheet.get_tile(1,0), (256, 152)),
            'fence_left' : pygame.transform.scale(fence_tilesheet.get_tile(1,1), (206, 128)),
            'fence_right' : pygame.transform.scale(fence_tilesheet.get_tile(0,1), (206, 128)),
            }
        return tiles