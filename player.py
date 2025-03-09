import pygame
from constants import *

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.width = PLATFORM_WIDTH
        self.height = PLATFORM_HEIGHT

    def draw(self, screen):
        pygame.draw.rect(screen, "white", (self.position.x-self.width/2.0, self.position.y-self.height/2.0, self.width, self.height))

    def update(self, dt, ball):
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_w]:
            if self.position.y > self.height/2.0:
                self.move(-dt)
        if keys[pygame.K_s]:
            if self.position.y < SCREEN_HEIGHT - self.height/2.0:
                self.move(dt)

    def move(self, dt):
        forward = pygame.Vector2(0, 1)
        self.position += forward * PLATFORM_SPEED * dt
