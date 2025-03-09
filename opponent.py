import pygame
from constants import *

class Opponent(pygame.sprite.Sprite):
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
        d = self.direction(ball)
        if d == 0:
            return
        if self.position.y >= self.height/2.0 and d < 0:
            self.move(dt*d)
        if self.position.y <= SCREEN_HEIGHT - self.height/2.0 and d > 0:
            self.move(dt*d)

    def move(self, dt):
        forward = pygame.Vector2(0, 1)
        self.position += forward * PLATFORM_SPEED * dt
    
    def direction(self, ball):
        d = ball.position.y - self.position.y
        if d == 0:
            return 0
        if d < 0:
            return -1
        return 1
    

