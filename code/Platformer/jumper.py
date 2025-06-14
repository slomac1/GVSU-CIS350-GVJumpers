from .setting import *
from random import randint
from .player import Player
from .enemy import Enemy
from .blocks import Block
from .clouds import Cloud
from .tilesheet import Tilesheet
from .tilesheet_manager import create_tilesheets
from . import save_manager
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import tickets_manager
cur_directory = os.path.dirname(__file__)
image_directory = os.path.join(cur_directory, "images")


class Jumper:
    def __init__(self):
        pygame.init()

        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.SCALED | pygame.DOUBLEBUF, vsync=1)
        pygame.display.set_caption("GVJumping")

        # for adjusting screen darkness, potential option for monster area
        self.overlay = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.overlay.fill('black')
        self.overlay.set_alpha(0)

        self.tickets = tickets_manager.load_tickets()
        self.game_data = None

        self.carnival_running = True
        self.dungeon_running = False
        self.clock = pygame.time.Clock()

        self.minigame_to_play = None

        self.offset_x = 0
        self.offset_y = 0

        self.all_carnival_sprites = pygame.sprite.Group()
        self.carnival_level_sprites = pygame.sprite.Group()
        self.background_sprites = pygame.sprite.Group()
        self.minigame_sprites = pygame.sprite.Group()
        self.player_sprite = pygame.sprite.Group()

        self.all_tent_sprites = pygame.sprite.Group()
        self.tent_level_sprites = pygame.sprite.Group()
        self.enemy_sprites = pygame.sprite.Group()
        self.attack_sprites = pygame.sprite.Group()

        self.tiles = create_tilesheets()

        '''
        Sprites for level and background for the carnival area
        
        '''
        # Controls info for carnival area
        carnival_controls_surf = pygame.image.load(join(image_directory, 'player_controls.png')).convert_alpha()
        carnival_controls_surf = pygame.transform.scale(carnival_controls_surf, (250, 200))
        Block(self.all_carnival_sprites, carnival_controls_surf, None, (640, 100))

        # Controls info for tent area
        tent_controls_surf = pygame.image.load(join(image_directory, 'player_controls_tent.png')).convert_alpha()
        self.tent_controls_surf = pygame.transform.scale(tent_controls_surf, (250, 133))

        # Control prompt for entering booth and tent
        booth_prompt_surf = pygame.image.load(join(image_directory, 'enter_minigame_prompt.png')).convert_alpha()
        self.booth_prompt_surf = pygame.transform.scale(booth_prompt_surf, (250, 75))
        tent_prompt_surf = pygame.image.load(join(image_directory, 'enter_tent_prompt.png')).convert_alpha()
        self.tent_prompt_surf = pygame.transform.scale(tent_prompt_surf, (250, 75))

        # Starting and Ending Message
        starting_message = pygame.image.load(join(image_directory, 'starting_message.png')).convert_alpha()
        self.starting_message = pygame.transform.scale(starting_message, (450, 200))
        ending_message = pygame.image.load(join(image_directory, 'ending_message.png')).convert_alpha()
        self.ending_message = pygame.transform.scale(ending_message, (450, 200))

        # Win and Loss images
        win_message = pygame.image.load(join(image_directory, 'won.png')).convert_alpha()
        self.win_message = pygame.transform.scale(win_message, (900,600))
        lost_message = pygame.image.load(join(image_directory, 'lost.png')).convert_alpha()
        self.lost_message = pygame.transform.scale(lost_message, (900,600))

        Cloud(self.background_sprites, self.tiles['cloud1'], (randint(200,5000), randint(-300, 150)))
        Cloud(self.background_sprites, self.tiles['cloud2'], (randint(200,5000), randint(-300, 150)))
        Cloud(self.background_sprites, self.tiles['cloud3'], (randint(200,5000), randint(-300, 150)))
        Cloud(self.background_sprites, self.tiles['cloud4'], (randint(200,5000), randint(-300, 150)))
        Cloud(self.background_sprites, self.tiles['cloud5'], (randint(200,5000), randint(-300, 150)))
        Cloud(self.background_sprites, self.tiles['cloud6'], (randint(200,5000), randint(-300, 150)))
        Cloud(self.background_sprites, self.tiles['cloud7'], (randint(200,5000), randint(-300, 150)))
        Cloud(self.background_sprites, self.tiles['cloud8'], (randint(200,5000), randint(-300, 150)))
        Cloud(self.background_sprites, self.tiles['cloud1'], (randint(200,5000), randint(-300, 150)))
        Cloud(self.background_sprites, self.tiles['cloud2'], (randint(200,5000), randint(-300, 150)))
        Cloud(self.background_sprites, self.tiles['cloud3'], (randint(200,5000), randint(-300, 150)))
        Cloud(self.background_sprites, self.tiles['cloud4'], (randint(200,5000), randint(-300, 150)))
        Cloud(self.background_sprites, self.tiles['cloud5'], (randint(200,5000), randint(-300, 150)))
        Cloud(self.background_sprites, self.tiles['cloud6'], (randint(200,5000), randint(-300, 150)))
        Cloud(self.background_sprites, self.tiles['cloud7'], (randint(200,5000), randint(-300, 150)))
        Cloud(self.background_sprites, self.tiles['cloud8'], (randint(200,5000), randint(-300, 150)))

        # Creating base world with tiles
        Block((self.carnival_level_sprites, self.all_carnival_sprites), self.tiles['grass_left'], None, (1664, 452))
        Block((self.carnival_level_sprites, self.all_carnival_sprites), self.tiles['grass_right'], None, (1920, 452))
        for i in range(-1,11):
            Block((self.carnival_level_sprites, self.all_carnival_sprites), self.tiles['grass1'], None, (256 + (512 * i), 552))
            Block((self.carnival_level_sprites, self.all_carnival_sprites), self.tiles['grass2'], None, (512 * i, 552))
            Block((self.carnival_level_sprites, self.all_carnival_sprites), self.tiles['dirt1_light'], None, (256 + (512 * i), 808))
            Block((self.carnival_level_sprites, self.all_carnival_sprites), self.tiles['dirt2_light'], None, (512 * i, 808))

        # Ferris wheel sprite pull and create
        Block(self.all_carnival_sprites, self.tiles['ferris_wheel'], None, (2600, -88))

        # Booth sprite pull and creating
        self.dart_game = Block((self.minigame_sprites, self.all_carnival_sprites), self.tiles['dart_booth'], None, (1200, 296))
        self.puzzle_game = Block((self.minigame_sprites, self.all_carnival_sprites), self.tiles['puzzle_booth'], None, (1800, 196))
        self.card_game = Block((self.minigame_sprites, self.all_carnival_sprites), self.tiles['card_booth'], None, (3400, 296))

        # Tent sprite pull and creating
        self.tent = Block(self.all_carnival_sprites, self.tiles['tent'], None, (4000, 168))

        Block(self.all_carnival_sprites, self.tiles['archway_open'] , None, (428, 284))
        self.archway = Block((self.all_carnival_sprites, self.carnival_level_sprites), self.tiles['archway_close'] , None, (428, 330))

        '''
        Sprites for level and background in tent area
        
        '''
        self.tent_background = pygame.image.load(join(image_directory, 'tent_background.png')).convert_alpha()
        self.tent_background = pygame.transform.scale(self.tent_background, (3000, 1200))
        self.tent_background_rect = self.tent_background.get_rect(center = (1175, (WINDOW_HEIGHT / 2)))

        # Enemy sprites
        zombie_tilesheet = Tilesheet('zombie_spritesheet', 146, 249, 2, 4)
        self.zombie_surf = []
        for i in range(4):
            self.zombie_surf.append(pygame.transform.scale(zombie_tilesheet.get_tile(i, 1), (64,128)))
        for i in range(4):
            self.zombie_surf.append(pygame.transform.scale(zombie_tilesheet.get_tile(i, 0), (64,128)))

        # Park Manager
        self.manager = Block(self.all_carnival_sprites, self.tiles['sad_manager'], None, (600, 330))

        # player animations
        player_run_walk_attack = Tilesheet('sprites_02', 384, 512, 4, 4)
        player_surf = []

        player_surf.append(pygame.transform.scale(player_run_walk_attack.get_tile(0, 2), (72, 128)))
        player_surf.append(pygame.transform.scale(player_run_walk_attack.get_tile(0, 2), (72, 128)))
        player_surf.append(pygame.transform.scale(player_run_walk_attack.get_tile(0, 2), (72, 128)))
        player_surf.append(pygame.transform.scale(player_run_walk_attack.get_tile(0, 2), (72, 128)))
    
        player_surf.append(pygame.transform.scale(player_run_walk_attack.get_tile(0, 0), (70, 128)))
        player_surf.append(pygame.transform.scale(player_run_walk_attack.get_tile(1, 0), (68, 128)))
        player_surf.append(pygame.transform.scale(player_run_walk_attack.get_tile(2, 0), (70, 128)))
        player_surf.append(pygame.transform.scale(player_run_walk_attack.get_tile(3, 0), (68, 128)))
    
        player_surf.append(pygame.transform.scale(player_run_walk_attack.get_tile(1, 3), (66, 128)))
        player_surf.append(pygame.transform.scale(player_run_walk_attack.get_tile(1, 3), (66, 128)))
        player_surf.append(pygame.transform.scale(player_run_walk_attack.get_tile(1, 3), (66, 128)))
        player_surf.append(pygame.transform.scale(player_run_walk_attack.get_tile(1, 3), (66, 128)))
    
        player_surf.append(pygame.transform.scale(player_run_walk_attack.get_tile(0, 1), (74, 128)))
        player_surf.append(pygame.transform.scale(player_run_walk_attack.get_tile(1, 1), (80, 128)))
        player_surf.append(pygame.transform.scale(player_run_walk_attack.get_tile(3, 1), (84, 128)))
        player_surf.append(pygame.transform.scale(player_run_walk_attack.get_tile(2, 1), (80, 128)))
        player_surf.append(pygame.transform.scale(player_run_walk_attack.get_tile(3, 1), (80, 128)))
        
        self.player = Player(self.player_sprite, player_surf)
        
        # Use to get new tilesheet sizes
        test_surf = pygame.image.load(join(image_directory, 'sprites_02.png')).convert_alpha()
        test_rect = test_surf.get_rect(topleft = (0, 0))
        print(test_rect.bottomright)
        
        # Fence sprite pull and creating
        Block(self.carnival_level_sprites, None, (280, 300), (428, 0))
        Block((self.all_carnival_sprites, self.carnival_level_sprites), self.tiles['fence_left'], None, (200, 360))
        Block((self.all_carnival_sprites, self.carnival_level_sprites), self.tiles['fence_left'], None, (-6, 360))
        Block((self.all_carnival_sprites, self.carnival_level_sprites), self.tiles['fence_left'], None, (-212, 360))
        Block((self.all_carnival_sprites, self.carnival_level_sprites), self.tiles['fence_post_left'], None, (4600, 348))
        Block((self.all_carnival_sprites, self.carnival_level_sprites), self.tiles['fence_right'], None, (4831, 360))
        Block((self.all_carnival_sprites, self.carnival_level_sprites), self.tiles['fence_right'], None, (5037, 360))
    
    def create_tent_area(self):
        for sprite in self.all_tent_sprites:
            sprite.kill()

        # ground blocks 
        for i in range(-2, 11):
            Block((self.tent_level_sprites, self.all_tent_sprites), self.tiles['dirt_top1_dark'], None, (256 + (512 * i), 552))
            Block((self.tent_level_sprites, self.all_tent_sprites), self.tiles['dirt_top2_dark'], None, (512 * i, 552))
            Block((self.tent_level_sprites, self.all_tent_sprites), self.tiles['dirt1_dark'], None, (256 + (512 * i), 808))
            Block((self.tent_level_sprites, self.all_tent_sprites), self.tiles['dirt2_dark'], None, (512 * i, 808))

        # scaffolding array
        for i in range(9):
            for j in range(3):
                Block(self.all_tent_sprites, self.tiles['side_double'], None, (558 + (448 * i), 296 - (256 * j)))

        # walking planks
        for i in range(20):
            piece = randint(0,1)
            if piece == 0:
                x = randint(0,7)
                y = randint(0,2)
                new_block = Block((), self.tiles['medium'], None, (782 + (448 * x), 156 - (256 * y)))
            else:
                x = randint(0,6)
                y = randint(0,2)
                new_block = Block((), self.tiles['long'], None, (1006 + (448 * x), 156 - (256 * y)))
            if not pygame.sprite.spritecollide(new_block, self.tent_level_sprites, False):
                self.all_tent_sprites.add(new_block)
                self.tent_level_sprites.add(new_block)

        # Enemies
        for i in range(10):
            x = randint(0,7)
            y = randint(0,2)
            new_enemy = Enemy((), self.zombie_surf, (782 + (448 * x), 160 - (256 * y)))
            if pygame.sprite.spritecollide(new_enemy, self.tent_level_sprites, False):
                self.enemy_sprites.add(new_enemy)
                self.all_tent_sprites.add(new_enemy)

        # stands and ring wall
        stands_right = pygame.image.load(join(image_directory, 'stands.png')).convert_alpha()
        stands_left = pygame.transform.flip(stands_right, True, False)
        Block(self.all_tent_sprites, stands_left, None, (-200, 200))
        Block(self.all_tent_sprites, stands_right, None, (4900, 200))
        for i in range(3):
            Block(self.all_tent_sprites, self.tiles['ring_wall'], None, (4600 + (i * 220), 360))
            Block(self.all_tent_sprites, self.tiles['ring_wall'], None, (160 - (i * 220), 360))

        Block(self.all_tent_sprites, self.tent_controls_surf, None, (2600, 250))

        return
        
    def handle_movement(self):
        self.player.original_location = self.player.rect.center
        keys_pressed = pygame.key.get_pressed()
        if self.player.index == 15:
            self.player.attack(self.attack_sprites)
        if keys_pressed[pygame.K_e] and self.minigame_booth_prompt(True):
            self.carnival_running = False
            self.save_assets(True)
            if self.minigame_to_play == 'dungeon':
                self.dungeon_running = True
                self.run_dungeon()
            else:
                self.carnival_running = False
            return
        elif keys_pressed[pygame.K_ESCAPE]:
            if self.dungeon_running:
                self.dungeon_running = False
                self.carnival_running = True
                self.run_carnival()
                return
            elif self.carnival_running and self.tickets >= 100 and self.player.rect.x < 400:
                self.carnival_running = False
                self.dungeon_running = False
                self.won()
                return
        elif keys_pressed[pygame.K_k] and self.dungeon_running and (pygame.time.get_ticks() - self.player.last_attack_time > self.player.attack_cooldown):
            self.player.last_attack_time = pygame.time.get_ticks()
            self.player.index = 12
            self.player.attacking = True
        elif keys_pressed[pygame.K_d] and keys_pressed[pygame.K_a]:
            self.player.direction = 0
        elif keys_pressed[pygame.K_d] and self.player.rect.x < 4400:
            self.player.direction = 1
        elif keys_pressed[pygame.K_a] and self.player.rect.x > 300:
            self.player.direction = -1
        else:
            self.player.direction = 0

        self.player.rect.x += self.player.direction * PLAYER_SPEED
        horizontal_collide = self.check_horizontal_collision()
        if not horizontal_collide and self.player.direction != 0:
            self.player.moving = True
        else:
            self.player.moving = False

        self.player.rect.y += self.player.velocity_y
        vertical_collide = self.check_vertical_collision()
        if not vertical_collide:
            if not self.player.in_air and not self.player.attacking:
                self.player.index = 8
            self.player.in_air = True
        else:
            if self.player.in_air and not self.player.attacking:
                self.player.index = 0
            self.player.in_air = False
        if keys_pressed[pygame.K_j] and self.player.in_air == False:
            self.player.velocity_y = -25
        self.player.velocity_y = min(GRAVITY, (self.player.velocity_y + 1))

        self.player.current_locaiton = self.player.rect.center

        self.offset_x += self.player.original_location[0] - self.player.current_locaiton[0]
        self.offset_y += self.player.original_location[1] - self.player.current_locaiton[1]

    def check_horizontal_collision(self):
        if self.carnival_running == True:
            current_sprites = self.carnival_level_sprites
        else:
            current_sprites = self.tent_level_sprites
        for block in current_sprites:
            if pygame.sprite.collide_rect(self.player, block):
                if self.player.direction == 1:
                    self.player.rect.right = block.rect.left
                else:
                    self.player.rect.left = block.rect.right
                return True
        return False
    
    def check_vertical_collision(self):
        if self.carnival_running == True:
            current_sprites = self.carnival_level_sprites
        else:
            current_sprites = self.tent_level_sprites
        for block in current_sprites:
            if pygame.sprite.collide_rect(self.player, block):
                if self.player.velocity_y < 0:
                    self.player.rect.top = block.rect.bottom
                    self.player.velocity_y = 0
                    return False
                else:
                    self.player.rect.bottom = block.rect.top
                    return True
        return False
    
    def check_enemy_collision(self):
        current_time = pygame.time.get_ticks()
        damage_cooldown = (current_time - self.player.damage_taken_time)
        if damage_cooldown >= 250:
            for enemy in self.enemy_sprites:
                if pygame.sprite.collide_mask(self.player, enemy):
                    self.player.damage_taken_time = current_time
                    self.player.health -= 10
                    return True
        return False
    
    def display_character_info(self):
        font = pygame.font.Font(None, 30)
        text_surf1 = font.render(f'HP: {self.player.health}', True, ('red'))
        text_surf2 = font.render(f'Tickets: {self.tickets}', True, ('red'))
        text_rect1 = text_surf1.get_rect(topleft = (50, 50))
        text_rect2 = text_surf2.get_rect(topleft = (50, 85))
        self.display_surface.blit(text_surf1, text_rect1)
        self.display_surface.blit(text_surf2, text_rect2)

    def minigame_booth_prompt(self, check):
        for booth in self.minigame_sprites:
            if pygame.sprite.collide_rect(self.player, booth):
                self.display_surface.blit(self.booth_prompt_surf, (booth.rect.x + self.offset_x, booth.rect.y - 75 + self.offset_y))
                if booth == self.dart_game and check:
                    self.minigame_to_play = 'darts'
                elif booth == self.card_game and check:
                    self.minigame_to_play = 'cards'
                elif booth == self.puzzle_game and check:
                    self.minigame_to_play = 'puzzle'
                return True
        if pygame.sprite.collide_rect(self.player, self.tent):
            self.display_surface.blit(self.tent_prompt_surf, (self.tent.rect.x + self.offset_x + 125, self.tent.rect.y + 125 + self.offset_y))
            self.minigame_to_play = 'dungeon'
            return True
        return False
    
    def load_assets(self):
        self.game_data = save_manager.load()
        
        self.offset_x = self.game_data["offset_x"]
        self.offset_y = self.game_data["offset_y"]
        self.player.index = self.game_data["p_index"]
        self.player.rect.centerx = self.game_data["p_rectx"]
        self.player.rect.centery = self.game_data["p_recty"]
        self.player.health = min(self.player.health, self.game_data["p_health"])
    
    def save_assets(self, condition):
        if condition:
            save_manager.save({"offset_x": self.offset_x,
                            "offset_y": self.offset_y,
                            "p_index": self.player.index,
                            "p_rectx": self.player.rect.centerx,
                            "p_recty": self.player.rect.centery,
                            "p_health": self.player.health})
        else:
            save_manager.save(None)
            self.game_data = None
        return

    def run_carnival(self):
        self.load_assets()
        
        if self.tickets >= 100:
            self.archway.kill()
            self.manager = Block(self.all_carnival_sprites, self.tiles['happy_manager'], None, (600, 330))

        while self.carnival_running:
            self.clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.carnival_running = False
                    return

            self.handle_movement()
            if self.dungeon_running == True:
                return
            self.player.update()
            
            self.display_surface.fill('#a7e0fa')
            for cloud in self.background_sprites:
                self.display_surface.blit(cloud.image, (cloud.rect.x + self.offset_x, cloud.rect.y + self.offset_y))
                self.background_sprites.update()

            for sprite in self.all_carnival_sprites:
                self.display_surface.blit(sprite.image, (sprite.rect.x + self.offset_x, sprite.rect.y + self.offset_y))

            if self.tickets < 100 and self.player.rect.x < 600:
                self.display_surface.blit(self.starting_message, (630 + self.offset_x, 150 + self.offset_y))
            elif self.player.rect.x < 600:
                self.display_surface.blit(self.ending_message, (630 + self.offset_x, 150 + self.offset_y))

            self.display_surface.blit(self.player.image, (WINDOW_WIDTH / 2 - 32, WINDOW_HEIGHT / 2 - 64))

            self.display_character_info()
            self.minigame_booth_prompt(False)

            pygame.display.flip()
        tickets_manager.save_tickets(self.tickets)
        self.save_assets(True)

    def run_dungeon(self):
        self.create_tent_area()
        self.offset_x += (self.player.rect.x - 2350)
        self.player.rect.x = 2350
        while self.dungeon_running == True:
            self.clock.tick(FPS)
            if self.player.health <= 0:
                self.lost()
                return
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.dungeon_running = False
                    return

            self.handle_movement()
            self.player.update()

            for enemy in self.enemy_sprites:
                if enemy.update(self.attack_sprites, self.tent_level_sprites, self.player.rect):
                    self.tickets += 5

            for attack in self.attack_sprites:
                attack.update()

            self.check_enemy_collision()

            self.display_surface.blit(self.tent_background, (self.tent_background_rect.x + (self.offset_x * .25),self.tent_background_rect.y + (self.offset_y * .25)))
            for sprite in self.all_tent_sprites:
                self.display_surface.blit(sprite.image, (sprite.rect.x + self.offset_x, sprite.rect.y + self.offset_y))
            self.display_surface.blit(self.player.image, (WINDOW_WIDTH / 2 - 32, WINDOW_HEIGHT / 2 - 64))
            self.display_surface.blit(self.overlay, (0,0))
            self.display_character_info()

            pygame.display.flip()
        self.run_carnival()

    def won(self):
        self.display_surface.blit(self.win_message, (190,60))
        pygame.display.flip()
        self.save_assets(False)
        tickets_manager.save_tickets(0)
        pygame.time.wait(5000)
        pygame.quit(), sys.exit()

    def lost(self):
        self.display_surface.blit(self.lost_message, (190,60))
        pygame.display.flip()
        self.save_assets(False)
        tickets_manager.save_tickets(0)
        pygame.time.wait(5000)
        pygame.quit(), sys.exit()