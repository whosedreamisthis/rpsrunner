import pygame
from consts import *
from ground import Ground 
from player import Player

pygame.init()

def game():
    clock = pygame.time.Clock() 
    screen = pygame.display.set_mode((700,250))
    pygame.display.set_caption("Rock Paper Scissor Infinite Runner")
    ground = Ground()
    ground.draw(screen)
    ground.update()
    
    player = Player()
    player.update()
    player.draw(screen)
    
    
    
    quit = False
        
    while not quit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit = True
        screen.fill((240,240,240))
        ground.update()
        ground.draw(screen)
        player.update()
        player.draw(screen)
        pygame.display.update()
        # clock.tick(1) 
        clock.tick(60)
        
            
                    
        