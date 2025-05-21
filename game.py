import pygame
from consts import *
from ground import Ground 
from player import Player
from enemies_manager import EnemiesManager

pygame.init()
pygame.font.init()


def collide(player,enemiesManager):
    enemy = enemiesManager.get_first_enemy()
    if enemy.get_x_pos() <= 50:
        return enemy 
    
    return None   

def duel(player, enemy):
    if player.type == enemy.type:
        return "Tie"
    
    if (player.type == "R" and enemy.type == "P") or \
        (player.type == "S" and enemy.type == "R") or  \
        (player.type == "P" and enemy.type == "S"):
            return "Enemy"
    
    if player.type == "N":
        return "Enemy"
    
    return "Player"
        
    
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
    
    enemies_manager = EnemiesManager(ground_speed,font)
    
    enemies_manager.update()
    enemies_manager.draw(screen)

    
    quit = False
    game_over = False
    while not quit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit = True
                
        
        screen.fill((240,240,240))
        
        if (not game_over):
            ground.update()
            player.update()
            enemies_manager.update()
            
            enemy = collide(player,enemies_manager)
            if (enemy is not None):
                print("player collided with enemy")
                
                
                winner = duel(player,enemy)
                if winner == "Enemy":
                    game_over = True
                    enemy.draw(screen)
                else:
                    enemies_manager.pop_first_enemy()
                    del enemy
                    
                    
                
        ground.draw(screen)
        player.draw(screen)
        enemies_manager.draw(screen)    
        pygame.display.update()
        # clock.tick(1) 
        clock.tick(60)
        
            
                    
        