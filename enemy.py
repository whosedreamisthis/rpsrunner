import pygame
from consts import *

import random
class Enemy:
    def __init__(self,font,enemy_type,rock_surface, paper_surface, scissors_surface):
        Enemy.rock_surface = rock_surface
        Enemy.paper_surface = paper_surface
        Enemy.scissors_surface = scissors_surface
        
        self.x = WINDOW_WIDTH
        self.y = GROUND_HEIGHT
        
        self.type = enemy_type
        if self.type == "R":
            self.image = Enemy.rock_surface
        elif self.type == "S":
            self.image = Enemy.scissors_surface
        else:
            self.image = Enemy.paper_surface
            
        original_width, original_height = self.image.get_size()
        aspect_ratio = original_width / original_height

        desired_new_width = 40
        desired_new_height = int(desired_new_width / aspect_ratio) # Calculate height to maintain ratio

        self.image = pygame.transform.scale(self.image, (desired_new_width, desired_new_height))

        self.image_rect = self.image.get_rect()
        self.y  -= 10    
        self.image_rect.center = (self.x,self.y - 100)
        
    def draw(self,screen):
        screen.blit(self.image, self.image_rect)
    
    def get_x_pos(self):
        return self.x
    
    def update(self,speed):
        self.x -= speed
        self.image_rect.center = (self.x,self.y)

        
        