import pygame
import circleshape
import constants
import main
import shot

# Base class for game objects
class Player(circleshape.CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, constants.PLAYER_RADIUS)
        self.rotation = 0
        self.cooldown = constants.PLAYER_SHOOT_COOLDOWN
        self.speed = 0
    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen,):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)
    
    def rotate(self, dt):
        self.rotation += constants.PLAYER_TURN_SPEED * dt

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * self.speed * dt



    def update(self, dt):

        self.move(dt)
        self.cooldown = self.cooldown - dt
        keys = pygame.key.get_pressed()
        nokeys = 1
        if keys[pygame.K_a]:
            inverse = dt * -1
            self.rotate(inverse)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_s]:
            nokeys = 0
            if self.speed > (constants.PLAYER_MAX_SPEED * -1):
                self.speed = self.speed -  constants.PLAYER_ACCELERATION_RATE
        if keys[pygame.K_w]:
            nokeys = 0
            if self.speed < constants.PLAYER_MAX_SPEED:
                self.speed = self.speed +  constants.PLAYER_ACCELERATION_RATE
        if nokeys == 1:
            if self.speed > 0:
                self.speed = self.speed - constants.PLAYER_ACCELERATION_RATE
            elif self.speed < 0:
                self.speed = self.speed + constants.PLAYER_ACCELERATION_RATE
        if keys[pygame.K_SPACE]:
            self.shoot()
        if self.position.x < 0:
            self.position.x = constants.SCREEN_WIDTH
        elif self.position.x > constants.SCREEN_WIDTH:
            self.position.x = 0
        
        if self.position.y < 0:
            self.position.y = constants.SCREEN_HEIGHT
        elif self.position.y > constants.SCREEN_HEIGHT:
            self.position.y = 0




    def shoot(self):
        
        if self.cooldown <= 0:
            bullet = shot.Shot(self.position, self.position)
            bullet.velocity = pygame.Vector2(0, 1)
            bullet.rotation = self.rotation
            bullet.velocity = bullet.velocity * constants.PLAYER_SHOOT_SPEED
            self.cooldown = constants.PLAYER_SHOOT_COOLDOWN


