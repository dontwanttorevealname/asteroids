import pygame
import circleshape
import constants
import main

# Base class for game objects
class Asteroid(circleshape.CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.x = x  # Explicitly set x
        self.y = y  # Explicitly set y
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", (int(self.x), int(self.y)), self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
        self.x, self.y = self.position.x, self.position.y 