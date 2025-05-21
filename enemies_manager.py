from enemy import Enemy
import random
from consts import *
original_min_wait_frames = 80
original_max_wait_frames = 150
class EnemiesManager:
    def __init__(self,speed,font):
        self.enemies = []
        self.ground_speed = speed
        self.current_spawn_time = 1
        self.font = font
        self.min_wait_frames = original_min_wait_frames
        self.max_wait_frames = original_max_wait_frames
   
    def reset(self):
        self.enemies.clear() 
        self.current_spawn_time = 1
        self.min_wait_frames = original_min_wait_frames
        self.max_wait_frames = original_max_wait_frames
            
    def spawn_enemy(self):
        enemy_type =random.choice(ENEMY_TYPES)

        new_enemy = Enemy(self.font,enemy_type)
        self.enemies.append(new_enemy)
        
    def update(self):
        
        self.current_spawn_time -= 1
        
        if self.current_spawn_time <= 0:
            self.current_spawn_time = random.randint(self.min_wait_frames,self.max_wait_frames)

            self.spawn_enemy()
        
        for enemy in self.enemies:
            enemy.update(self.ground_speed)
            
    def pop_first_enemy(self):
        enemy = self.enemies.pop(0)
        return enemy
    
    def get_first_enemy(self):
        if len(self.enemies) == 0:
            return None
        return self.enemies[0]
    
    def draw(self,screen):
        for enemy in self.enemies:
            enemy.draw(screen)
            
    def delete_enemy(self,enemy):
        self.enemies.remove(enemy)
        