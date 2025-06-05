from setting import *

class Enemy(pygame.sprite.Sprite):
    def __init__(self, groups, surf, pos):
        super().__init__(groups)
        self.surf = surf
        self.index = 0
        self.image = self.surf[self.index]
        self.rect = self.image.get_rect(center = pos)
        self.velocity_y = GRAVITY
        self.velocity_x = 2
        self.moving = False
        self.direction = 1
        self.original_direction = 1
        self.last_movement_time = pygame.time.get_ticks()

    def update(self, attack_sprites, level_sprites, player_pos):
        if self.hit_by_attack(attack_sprites):
            self.kill()
            return True
        self.moving = self.detect_player(player_pos)
        if self.moving:
            self.rect.x += (self.velocity_x * self.direction)
            self.check_horizontal_collision(level_sprites)
        self.rect.y += self.velocity_y
        self.check_vertical_collision(level_sprites)

        current_time = pygame.time.get_ticks()
        if current_time - self.last_movement_time > 200 and not self.moving:
            self.last_movement_time = current_time
            if self.index == 3:
                self.index = 1
            else:
                self.index = 3
        elif current_time - self.last_movement_time > 200 and self.moving:
            self.last_movement_time = current_time
            if self.index < 4 or self.index >= 7:
                self.index = 4
            else:
                self.index += 1
    
        if self.direction == 1:
            self.image = self.surf[self.index]
        elif self.direction == -1:
            self.image = pygame.transform.flip(self.surf[self.index], True, False)
        else:
            if self.original_direction == 1:
                self.image = self.surf[self.index]
            else:
                self.image = pygame.transform.flip(self.surf[self.index], True, False)
        if self.direction != 0:
            self.original_direction = self.direction

    def detect_player(self, player_pos):
        playerx_distance = player_pos.x - self.rect.x
        playery_distance = abs(player_pos.y - self.rect.y)
        if playery_distance < 600 and abs(playerx_distance) < 600:
            if playerx_distance >= 0:
                self.direction = 1
            else:
                self.direction = -1
            if abs(playerx_distance) <= 10:
                return False
            return True
        return False
    
    def check_horizontal_collision(self, level_sprites):
        for block in level_sprites:
            if pygame.sprite.collide_rect(self, block):
                if self.direction == 1:
                    self.rect.right = block.rect.left
                else:
                    self.rect.left = block.rect.right
                return True
        return False
    
    def check_vertical_collision(self, level_sprites):
        for block in level_sprites:
            if pygame.sprite.collide_rect(self, block):
                if self.velocity_y < 0:
                    self.rect.top = block.rect.bottom
                    self.velocity_y = 0
                    return False
                else:
                    self.rect.bottom = block.rect.top
                    return True
        return False
    
    def hit_by_attack(self, attack_sprites):
        for attack in attack_sprites:
            if pygame.sprite.collide_rect(self, attack):
                return True
        return False