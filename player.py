import pygame
import random
from consts import *

class Player:
    def __init__(self,font):
        self.type = random.choice(ENEMY_TYPES)
        self.font = font
        self.text_surface = font.render(self.type, True, dark_gray) # Red text
        

# You can also render text with a background color:
# text_surface_bg = font.render("Text with Background", True, black, white) # Black text, white background

# Get the rectangle of the text surface
        self.text_rect = self.text_surface.get_rect()

# Center the text on the screen
        x = 30
        y = GROUND_HEIGHT
        self.text_rect.center = (x,y)

    def change(self,new_type):
        self.type = new_type
        self.text_surface = self.font.render(self.type, True, dark_gray)
    
    def get_pos_x():
        return 30
    
    def draw(self, screen):
        screen.blit(self.text_surface, self.text_rect)
            
    def update(self):
        pass
        