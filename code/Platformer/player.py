from setting import *

class Player(pygame.sprite.Sprite):
    def __init__(self, groups, surf):
        super().__init__(groups)
        self.surf = surf
        self.index = 0
        self.image = self.surf[self.index]
        self.rect = self.image.get_rect(center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))
        self.velocity_y = GRAVITY
        self.direction = 0

        self.health = 100

        self.last_movement_time = pygame.time.get_ticks()
        self.moving = False
        self.original_direction = 1

        self.in_air = False

        self.original_location = [0,0]
        self.current_locaiton = [0,0]

        self.damage_taken_time = pygame.time.get_ticks()

    def update(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_movement_time > 200 and not self.moving and not self.in_air:
            self.last_movement_time = current_time
            if self.index == 3:
                self.index = 1
            else:
                self.index = 3
        elif current_time - self.last_movement_time > 200 and self.in_air:
            self.last_movement_time = current_time
            if self.index < 8 or self.index == 11:
                self.index = 8
            else:
                self.index += 1
        elif current_time - self.last_movement_time > 200 and self.moving and not self.in_air:
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

        
        
        