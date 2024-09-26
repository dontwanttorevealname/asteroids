import pygame
import circleshape
import constants
import main
import random

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

    def split(self):
        self.kill
        if self.radius <= constants.ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20,50)
            v1 = self.velocity = self.velocity.rotate(random_angle)
            v2 = self.velocity = self.velocity.rotate(-random_angle)
            new_radius = self.radius - constants.ASTEROID_MIN_RADIUS
            asteroid1 = Asteroid(self.x + new_radius, self.y + new_radius, new_radius)
            asteroid1.velocity = v1 * 1.3
            asteroid2 = Asteroid(self.x - new_radius, self.y - new_radius, new_radius)
            asteroid2.velocity = v2 * 1.3