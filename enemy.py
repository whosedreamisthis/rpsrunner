import pygame
from consts import *
import random
class Enemy:
    def __init__(self,font,enemy_type):
        self.x = WINDOW_WIDTH
        self.y = GROUND_HEIGHT
        
        self.type = enemy_type
        if self.type == "R":
            self.color = rock_color
        elif self.type == "S":
            self.color = scissors_color
        else:
            self.color = paper_color
            
        self.text_surface = font.render(self.type, True, self.color) # Red text


        self.text_rect = self.text_surface.get_rect()

        self.text_rect.center = (self.x,self.y)
        
    def draw(self,screen):
        screen.blit(self.text_surface, self.text_rect)
    
    def get_x_pos(self):
        return self.x
    
    def update(self,speed):
        self.x -= speed
        self.text_rect.center = (self.x,self.y)

        
        