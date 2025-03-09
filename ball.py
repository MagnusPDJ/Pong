import pygame
from constants import *

class Ball(pygame.sprite.Sprite):
    def __init__(self, x, y):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.radius = BALL_RADIUS
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.rotation = 85

    def draw(self, screen):
        pygame.draw.circle(screen, "white", (self.position.x, self.position.y), self.radius)

    def update(self, dt, ball):
        self.move(dt)

        if self.position.y > SCREEN_HEIGHT - BALL_RADIUS:
            self.rotate_wall()
        if self.position.y < BALL_RADIUS:
            self.rotate_wall()

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * BALL_SPEED * dt
    
    def rotate_wall(self):
        angle = 180 - self.rotation
        self.rotation = angle
   
    def rotate_player(self):
        angle = 360 - self.rotation
        self.rotation = angle

    def rotate_opponent(self):
        angle = 360 - self.rotation
        self.rotation = angle
 
    def check_hit(self, rect):
        circle_distance_x = abs(self.position.x + - rect.position.x)
        circle_distance_y = abs(self.position.y - rect.position.y)
        if circle_distance_x > rect.width/2.0+self.radius or circle_distance_y > rect.height/2.0+self.radius:
            return False
        if circle_distance_x <= rect.width/2.0 or circle_distance_y <= rect.height/2.0:
            return True
        corner_x = circle_distance_x-rect.width/2.0
        corner_y = circle_distance_y-rect.height/2.0
        corner_distance_sq = corner_x**2.0 + corner_y**2.0
        return corner_distance_sq <= self.radius ** 2.0