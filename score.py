import pygame
from constants import *

class Score(pygame.sprite.Sprite):
    def __init__(self):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()   

        self.__playerscore = 0
        self.__opponentscore = 0
        self.font = pygame.font.Font("freesansbold.ttf", 25)
        self.text1 = self.font.render(f"{self.get_playerscore()} | {self.get_opponentscore()}", True, "white")
        self.__textrect1 = self.text1.get_rect()
        self.__textrect1.center = (SCREEN_WIDTH//2, 30)
        self.player_scores = self.font.render(f"You score! Continue? (y / n)", True, "white")
        self.__player_scoresrect = self.player_scores.get_rect()
        self.__player_scoresrect.center = (SCREEN_WIDTH//2, SCREEN_HEIGHT//2)
        self.opponent_scores = self.font.render(f"Opponent scores! Continue? (y / n)", True, "white")
        self.__opponent_scoresrect = self.opponent_scores.get_rect()
        self.__opponent_scoresrect.center = (SCREEN_WIDTH//2, SCREEN_HEIGHT//2)
        

    def get_opponentscore(self):
        return self.__opponentscore

    def get_playerscore(self):
        return self.__playerscore
    
    def add_points(self, who):
        if who == "player":
            self.__playerscore += 1
        if who == "opponent":
            self.__opponentscore += 1

    def draw(self, screen):
        screen.blit(self.text1, self.__textrect1)
    
    def update(self, dt, ball):
        self.text1 = self.font.render(f"{self.get_playerscore()} | {self.get_opponentscore()}", True, "white")

    def endscreen(self, screen, who):
        if who == "player":
            screen.blit(self.player_scores, self.__player_scoresrect)
        if who == "opponent":
            screen.blit(self.opponent_scores, self.__opponent_scoresrect)