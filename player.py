import pygame
import random
from consts import *
class Player:
    def __init__(self,font):
        Player.rock_surface = pygame.image.load("assets/images/rock.png").convert_alpha()
        Player.scissors_surface = pygame.image.load("assets/images/scissors.png").convert_alpha()
        Player.paper_surface = pygame.image.load("assets/images/paper.png").convert_alpha()

        self.type = random.choice(ENEMY_TYPES)
        
        self.set_image()
        self.image_rect = self.image.get_rect()
        self.image_rect.center =  (35,GROUND_HEIGHT - 10)

        

    def set_image(self):
        if self.type == "R":
            self.image = Player.rock_surface
        elif self.type == "S":
            self.image =  Player.scissors_surface
        else:    
            self.image =  Player.paper_surface
            
        original_width, original_height = self.image.get_size()
        aspect_ratio = original_width / original_height

        desired_new_width = 40
        desired_new_height = int(desired_new_width / aspect_ratio) # Calculate height to maintain ratio

        self.image = pygame.transform.scale(self.image, (desired_new_width, desired_new_height))

# You can also render text with a background color:
# text_surface_bg = font.render("Text with Background", True, black, white) # Black text, white background

# Get the rectangle of the text surface
        # self.text_rect = self.text_surface.get_rect()

# Center the text on the screen
        # x = 30
        # y = GROUND_HEIGHT
        # self.text_rect.center = (x,y)

    def change(self,new_type):
        self.type = new_type
        self.set_image()

        
    
    def get_pos_x():
        return 30
    
    def draw(self, screen):
        # screen.blit(self.text_surface, self.text_rect)
        screen.blit(self.image, self.image_rect)
            
    def update(self):
        pass
        