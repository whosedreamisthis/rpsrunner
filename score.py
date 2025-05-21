import pygame
from consts import *

class Score:
    def __init__(self):
        self.value = 0
        self.high_score = 0
      
        x = 150
        y = 20
        try:
            self.font = pygame.font.Font("assets/font/CourierPrime-Regular.ttf", 20) # Using a common free font
        except FileNotFoundError:
            self.font = pygame.font.SysFont(None, 20)
        
        self.text_surface = self.font.render(f"score: {self.value:04d}  high: {self.high_score:04d}", True, green) 
        self.text_rect = self.text_surface.get_rect()
        self.text_rect.center = (x,y)

    def draw(self,screen):
        screen.blit(self.text_surface, self.text_rect)
        
    def add_score(self, score):
        self.value += score
        
        if self.value > self.high_score:
            self.high_score = self.value

        self.text_surface = self.font.render(f"score: {self.value:04d}  high: {self.high_score:04d}", True, green) 

        
    