import pygame
from constants import *
from opponent import Opponent
from player import Player
from ball import Ball

def main():
    pygame.init()

    clock = pygame.time.Clock()
    dt = 0

    pygame.display.quit()
    pygame.display.set_caption("Pong")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()

    Opponent.containers = (updatables, drawables)
    Ball.containers = (updatables, drawables)
    Player.containers = (updatables, drawables)

    player = Player(PLATFORM_WIDTH, SCREEN_HEIGHT/2.0)
    opponent = Opponent(SCREEN_WIDTH - PLATFORM_WIDTH, SCREEN_HEIGHT/2.0)
    ball = Ball(SCREEN_WIDTH/2.0, SCREEN_HEIGHT/2.0)


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        updatables.update(dt, ball)

        if ball.check_hit(player):
            ball.rotate_player()
        if ball.check_hit(opponent):
            ball.rotate_opponent()
        
        screen.fill("black")
        
        for obj in drawables:
            obj.draw(screen)



        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()