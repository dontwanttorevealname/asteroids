# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *
clock = pygame.time.Clock()
dt = 0
def main():
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updatable, drawable)

    dt = 0
    pygame.init()

    print("Starting asteroids!")
    print("Screen width: " + str(SCREEN_WIDTH))
    print("Screen height: " + str(SCREEN_HEIGHT))
    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        for obj in updatable:
            obj.update(dt)
        pygame.Surface.fill(screen,"black")
        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()
        dt =  clock.tick(60) / 1000
if __name__ == "__main__":
    main()