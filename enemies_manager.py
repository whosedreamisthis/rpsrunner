from enemy import Enemy

class EnemiesManager:
    def __init__(self,speed):
        self.enemies = []
        self.ground_speed = speed
        
    def spawn_enemy(self,font):
        new_enemy = Enemy(font)
        self.enemies.append(new_enemy)
        
    def update(self):
        for enemy in self.enemies:
            enemy.update(self.ground_speed)
            
    def draw(self,screen):
        for enemy in self.enemies:
            enemy.draw(screen)
            
    def delete_enemy(self,enemy):
        self.enemies.remove(enemy)
        