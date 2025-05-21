import pygame
from consts import *
import random
class Enemy:
    def __init__(self,font):
        self.x = WINDOW_WIDTH + random.randrange(10,200)
        self.y = GROUND_HEIGHT
        
        self.type = "R"
        self.text_surface = font.render(self.type, True, black) # Red text


        self.text_rect = self.text_surface.get_rect()

        self.text_rect.center = (self.x,self.y)
        
    def draw(self,screen):
        screen.blit(self.text_surface, self.text_rect)
    
    
    
    def update(self,speed):
        self.x -= speed
        self.text_rect.center = (self.x,self.y)

        
        