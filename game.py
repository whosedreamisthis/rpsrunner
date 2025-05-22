import pygame
import pygame_gui
import random
from consts import *
from ground import Ground 
from player import Player
from enemies_manager import EnemiesManager
from score import Score
pygame.init()
pygame.font.init()
pygame.mixer.init()

ui_manager = pygame_gui.UIManager((WINDOW_WIDTH, WINDOW_HEIGHT))
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

try:
    # Make sure this path is correct for your sound file
    player_win_sound = pygame.mixer.Sound("assets/sounds/coin.wav")
    enemy_win_sound = pygame.mixer.Sound("assets/sounds/injury.wav")
    tie_sound = pygame.mixer.Sound("assets/sounds/jump.wav")
    
except pygame.error as e:
    print(f"Could not load sound file: {e}")
    player_win_sound = None
    enemy_win_sound = None
    tie_sound = None
    
def collide(player,enemiesManager):
    enemy = enemiesManager.get_first_enemy()
    if enemy is not None and enemy.get_x_pos() <= 50:
        return enemy 
    
    return None   

def duel(player, enemy):
    if player.type == enemy.type:
        tie_sound.play()
        return "Tie"
    
    if (player.type == "R" and enemy.type == "P") or \
        (player.type == "S" and enemy.type == "R") or  \
        (player.type == "P" and enemy.type == "S"):
            enemy_win_sound.play()
            return "Enemy"
    
    player_win_sound.play()
    return "Player"
  
score = Score()
try:
    font = pygame.font.Font("freesansbold.ttf", 32) # Using a common free font
except FileNotFoundError:
# Fallback to default font if 'freesansbold.ttf' is not found
    font = pygame.font.SysFont(None, 32)
    
ground = Ground()
ground_speed = ground.get_speed()

enemies_manager = EnemiesManager(ground_speed,font)


def init_game_state():
    score.reset()    
    enemies_manager.reset()
    ground.reset()
    set_rps_buttons_visibility(True)
    
def set_rps_buttons_visibility(visible):
    if visible:
        rock_button.show()
        paper_button.show()
        scissors_button.show()
    else:
        rock_button.hide()
        paper_button.hide()
        scissors_button.hide()
            
button_width = (WINDOW_WIDTH - 40) // 3 # 20px padding on each side, 20px between
button_height = 50
button_y = WINDOW_HEIGHT - button_height - 10 # 10px from bottom

rock_button = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((10, button_y), (button_width, button_height)),
    text='ROCK',
    manager=ui_manager,
    object_id='#rock_button' # Unique ID for styling if needed
)
paper_button = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((20 + button_width, button_y), (button_width, button_height)),
    text='PAPER',
    manager=ui_manager,
    object_id='#paper_button'
)
scissors_button = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((30 + 2 * button_width, button_y), (button_width, button_height)),
    text='SCISSORS',
    manager=ui_manager,
    object_id='#scissors_button'
)

def game():
    
    clock = pygame.time.Clock() 
    pygame.display.set_caption("Rock Paper Scissor Infinite Runner")
    ground.draw(screen)
    ground.update()
    
    

    
    player = Player(font)
    player.update()
    player.draw(screen)
    
    restart_button = pygame_gui.elements.UIButton(
                   relative_rect=pygame.Rect((WINDOW_WIDTH//2-100, WINDOW_HEIGHT//2-25), (200, 50)),
                text="Restart",
                manager=ui_manager)  
    restart_button.hide()  

   
    

    
    quit = False
    game_over = False
    current_frame = 0
    time_delta = clock.tick(60) / 1000.0
    while not quit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    player.change("R")
                elif event.key == pygame.K_s  or event.key == pygame.K_UP:
                    player.change("P")
                elif event.key == pygame.K_d  or event.key == pygame.K_RIGHT:
                    player.change("S")
            
            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == restart_button:
                    if game_over:
                        init_game_state()
                        print("Game Restarted!")
                elif not game_over: # Only allow RPS button presses if game is not over
                    if event.ui_element == rock_button:
                        player.change("R")
                    elif event.ui_element == paper_button:
                        player.change("P")
                    elif event.ui_element == scissors_button:
                        player.change("S")
            
            ui_manager.process_events(event)
            
            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == restart_button:
                    if game_over: # Ensure restart only happens if game is actually over
                        init_game_state()
                        current_frame = 0
                        print("Game Restarted!")
                        game_over = False
                        restart_button.hide()
                    
                    
                
        
        screen.fill((240,240,240))
        
        if (not game_over):
            ground.update()
            player.update()
            enemies_manager.update(time_delta)
            current_frame += 1 
            if current_frame > SPEED_UPGRADE_FRAME:
                ground.speed += 1
                enemies_manager.adjust_spawn_rate(ground.speed)
    
                current_frame = 0
                
            enemy = collide(player,enemies_manager)
            if (enemy is not None):
                print("player collided with enemy")
                
                
                winner = "Player" if god_mode else duel(player,enemy)
                if winner == "Enemy":
                    game_over = True
                    set_rps_buttons_visibility(False)
                    enemy.draw(screen)
                else:
                    if winner == "Player":
                        score.add_score(1)
                    enemies_manager.pop_first_enemy()
                    del enemy
        
        else:
            font_large = pygame.font.Font(None, 50)
            game_over_text = font_large.render("GAME OVER!", True, (155, 155, 155))
            text_rect = game_over_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 - 50))
            screen.blit(game_over_text, text_rect)
            restart_button.show()

        ui_manager.update(time_delta)           
                
        player.draw(screen)
        enemies_manager.draw(screen)    
        ground.draw(screen)
        score.draw(screen)
        

        ui_manager.draw_ui(screen)         

        pygame.display.flip()
        # clock.tick(1) 
        clock.tick(60)
        
            
                    
        