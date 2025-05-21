import pygame
from consts import *
from ground import Ground 
from player import Player
from enemies_manager import EnemiesManager

pygame.init()
pygame.font.init()


def game():
    clock = pygame.time.Clock() 
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Rock Paper Scissor Infinite Runner")
    ground = Ground()
    ground.draw(screen)
    ground.update()
    
    ground_speed = ground.get_speed()
    
    try:
        font = pygame.font.Font("freesansbold.ttf", 32) # Using a common free font
    except FileNotFoundError:
    # Fallback to default font if 'freesansbold.ttf' is not found
        font = pygame.font.SysFont(None, 32)
    
    player = Player(font)
    player.update()
    player.draw(screen)
    
    enemies_manager = EnemiesManager(ground_speed)
    enemies_manager.spawn_enemy(font)
    enemies_manager.update()
    enemies_manager.draw(screen)
    
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
        enemies_manager.update()
        enemies_manager.draw(screen)
        pygame.display.update()
        # clock.tick(1) 
        clock.tick(60)
        
            
                    
        