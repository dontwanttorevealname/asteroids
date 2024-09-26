import pygame
import circleshape
import constants
import main

# Base class for game objects
class Shot(circleshape.CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, constants.SHOT_RADIUS)  # Call parent class __init__
        print("initialize bullet")
        self.x=x
        self.y=y
        self.rotation = 1
        self.position = pygame.math.Vector2(x, y)
        self.velocity = pygame.math.Vector2(0, -1)
    
    def draw(self, screen):
        print("draw bullet")
        pygame.draw.circle(screen, "yellow", (int(self.position.x), int(self.position.y)), self.radius, 1)

    def update(self, dt):
        velocity = pygame.Vector2(0, 1).rotate(self.rotation) * constants.PLAYER_SHOOT_SPEED * dt
        
        self.position += velocity 
        #self.position += self.velocity * dt
        # Update the CircleShape's x and y
        self.x = self.velocity.x * dt
        self.y = self.velocity.y * dt
