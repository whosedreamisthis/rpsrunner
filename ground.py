import pygame

class Ground():
    def __init__(self):
        self.ground_length = 1202
        self.ground1 = pygame.image.load("assets/ground.png")
        self.ground1_x = 0
        self.ground1_y = 200
        
        self.ground2 = pygame.image.load("assets/ground.png")
        self.ground2_x = self.ground1_x + self.ground_length
        self.ground2_y = self.ground1_y
        
        self.speed = 4
        
    def draw(self, screen):
        screen.blit(self.ground1, (self.ground1_x,self.ground1_y))
        screen.blit(self.ground2, (self.ground2_x,self.ground2_y))

    def update(self):
        self.ground1_x -= self.speed
        self.ground2_x -= self.speed
        
        if self.ground1_x + self.ground_length < 0:
            self.ground1_x = self.ground2_x + self.ground_length
        elif self.ground2_x + self.ground_length < 0:
            self.ground2_x = self.ground1_x + self.ground_length
