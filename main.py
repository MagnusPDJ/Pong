import pygame
from constants import *
from opponent import Opponent
from player import Player
from ball import Ball
from score import Score

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
    Score.containers = (updatables, drawables)

    player = Player(PLATFORM_WIDTH, SCREEN_HEIGHT/2.0)
    opponent = Opponent(SCREEN_WIDTH - PLATFORM_WIDTH, SCREEN_HEIGHT/2.0)
    ball = Ball(SCREEN_WIDTH/2.0, SCREEN_HEIGHT/2.0)
    score = Score()

    while True:
        paused = True
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        updatables.update(dt, ball)

        if ball.check_hit(player):
            dist = (player.position.y - ball.position.y)/(player.height/2.0)
            ball.rotate_player(dist)
        if ball.check_hit(opponent):
            dist1 = (opponent.position.y - ball.position.y)/(opponent.height/2.0)
            ball.rotate_opponent(dist1)
        
        if ball.position.x - ball.radius <= 0:
            score.add_points("opponent")
            score.endscreen(screen, "opponent")
            pygame.display.update() 
            while paused:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        exit()
                    if event.type == pygame.KEYDOWN:
                        if pygame.key.name(event.key) == "n":
                            print("Goodbye")
                            exit()
                        if pygame.key.name(event.key) == "y":
                            ball.rotation = 270
                            ball.position = pygame.Vector2(SCREEN_WIDTH/2.0, SCREEN_HEIGHT/2.0)
                            player.position = pygame.Vector2(PLATFORM_WIDTH, SCREEN_HEIGHT/2.0)
                            opponent.position = pygame.Vector2(SCREEN_WIDTH - PLATFORM_WIDTH, SCREEN_HEIGHT/2.0)
                            ball.spawncd = 0
                            paused = False
        if ball.position.x + ball.radius >= SCREEN_WIDTH:
            score.add_points("player")
            score.endscreen(screen, "player")
            pygame.display.update() 
            while paused:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        exit()
                    if event.type == pygame.KEYDOWN:
                        if pygame.key.name(event.key) == "n":
                            print("Goodbye")
                            exit()
                        if pygame.key.name(event.key) == "y":
                            ball.rotation = 90
                            ball.position = pygame.Vector2(SCREEN_WIDTH/2.0, SCREEN_HEIGHT/2.0)
                            player.position = pygame.Vector2(PLATFORM_WIDTH, SCREEN_HEIGHT/2.0)
                            opponent.position = pygame.Vector2(SCREEN_WIDTH - PLATFORM_WIDTH, SCREEN_HEIGHT/2.0)
                            ball.spawncd = 0
                            paused = False                   

        screen.fill("black")
        
        for obj in drawables:
            obj.draw(screen)



        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()