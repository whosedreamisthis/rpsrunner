import pygame
from consts import *

class Ground():
    def __init__(self):
        self.ground_length = 1202
        self.ground1 = pygame.image.load("assets/images/ground.png")
        self.ground1_x = 0
        self.ground1_y = GROUND_HEIGHT + 5
        
        self.ground2 = pygame.image.load("assets/images/ground.png")
        self.ground2_x = self.ground1_x + self.ground_length
        self.ground2_y = self.ground1_y
        
        self.speed = 2
        
    def reset(self):
        self.speed = 2
    def get_ground_pos(self):
        return (self.ground1_x,self.ground1_y)
        
    def draw(self, screen):
        screen.blit(self.ground1, (self.ground1_x,self.ground1_y))
        screen.blit(self.ground2, (self.ground2_x,self.ground2_y))

    def get_speed(self):
        return self.speed
    
    def update(self):
        self.ground1_x -= self.speed
        self.ground2_x -= self.speed
        
        if self.ground1_x + self.ground_length < 0:
            self.ground1_x = self.ground2_x + self.ground_length
        elif self.ground2_x + self.ground_length < 0:
            self.ground2_x = self.ground1_x + self.ground_length
