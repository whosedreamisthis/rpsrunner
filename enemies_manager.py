from enemy import Enemy
import random
from consts import *

# Define original spawn times in SECONDS
# These are the times at the game's initial ground speed.
# Let's adjust these to be more meaningful for initial speed.
original_min_spawn_duration = 5.0  # seconds
original_max_spawn_duration = 10.0  # seconds

class EnemiesManager:
    def __init__(self, initial_speed, font):
        self.enemies = []
        self.font = font

        # Store the initial ground speed to calculate ratios for scaling
        self.original_ground_speed = initial_speed

        # Base spawn durations (in seconds)
        self.base_min_spawn_duration = original_min_spawn_duration
        self.base_max_spawn_duration = original_max_spawn_duration

        # Current effective spawn durations (these will change with speed)
        self.min_wait_time = self.base_min_spawn_duration
        self.max_wait_time = self.base_max_spawn_duration

        # Timer for spawning
        self.time_until_next_spawn = random.uniform(self.min_wait_time, self.max_wait_time)
        self.current_time_since_last_spawn = 0.0

        self.ground_speed = initial_speed # Current ground speed, updated by game.py

    def reset(self):
        self.enemies.clear()
        self.min_wait_time = self.base_min_spawn_duration
        self.max_wait_time = self.base_max_spawn_duration
        self.time_until_next_spawn = random.uniform(self.min_wait_time, self.max_wait_time)
        self.current_time_since_last_spawn = 0.0
        self.ground_speed = self.original_ground_speed # Reset speed for manager


    def spawn_enemy(self):
        enemy_type = random.choice(ENEMY_TYPES)
        new_enemy = Enemy(self.font, enemy_type)
        self.enemies.append(new_enemy)
        self.num_enemies_spawned = getattr(self, 'num_enemies_spawned', 0) + 1 # Initialize if not present


    def update(self, time_delta):
        # Update spawn timer using time_delta
        self.current_time_since_last_spawn += time_delta

        if self.current_time_since_last_spawn >= self.time_until_next_spawn:
            self.current_time_since_last_spawn = 0.0
            self.time_until_next_spawn = random.uniform(self.min_wait_time, self.max_wait_time)
            self.spawn_enemy()

        for enemy in self.enemies:
            enemy.update(self.ground_speed) # Enemies move at current ground speed

    def adjust_spawn_rate(self, new_ground_speed):
        self.ground_speed = new_ground_speed # Update the manager's current ground speed

        # Calculate a scaling factor for spawn times.
        # If speed doubles, spawn time should ideally halve to maintain density.
        # This means the factor is (original_speed / new_speed).
        if self.original_ground_speed == 0: # Avoid division by zero
            spawn_factor = 1.0 # If original speed is 0, no scaling
        else:
            spawn_factor = self.original_ground_speed / new_ground_speed

        # Apply the factor to the base spawn durations
        # Ensure spawn durations don't go below a sensible minimum (e.g., 0.5 seconds).
        min_allowed_spawn_time = 0.5 # Minimum time between spawns
        
        self.min_wait_time = max(self.base_min_spawn_duration * spawn_factor, min_allowed_spawn_time)
        # Ensure max_wait_time is always greater than min_wait_time,
        # maintaining a similar range as the original times.
        # Original range: original_max_spawn_duration - original_min_spawn_duration
        duration_range = self.base_max_spawn_duration - self.base_min_spawn_duration
        self.max_wait_time = max(self.base_max_spawn_duration * spawn_factor, self.min_wait_time + duration_range * 0.5) # Example: at least half original range
        
        # If the next spawn was planned based on old rates, adjust it
        # to prevent extremely long or short waits after a speed change.
        if self.time_until_next_spawn > self.max_wait_time or self.time_until_next_spawn < self.min_wait_time:
             self.time_until_next_spawn = random.uniform(self.min_wait_time, self.max_wait_time)

    def pop_first_enemy(self):
        if self.enemies: # Check if list is not empty before popping
            return self.enemies.pop(0)
        return None # Return None if no enemies to pop

    def get_first_enemy(self):
        if not self.enemies:
            return None
        return self.enemies[0]

    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)

    # delete_enemy is not used in game.py, so it can be removed
    # def delete_enemy(self, enemy):
    #     self.enemies.remove(enemy)