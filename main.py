# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *


clock = pygame.time.Clock()
dt = 0
def main():
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    pygame.font.init()
    my_font = pygame.font.SysFont('Comic Sans MS', 30)

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    dt = 0
    score = 0
    time = 0
    clocker = 0
    lives = 3
    pygame.init()

    print("Starting asteroids!")
    print("Screen width: " + str(SCREEN_WIDTH))
    print("Screen height: " + str(SCREEN_HEIGHT))
    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)
    field = AsteroidField()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    text_surface = my_font.render(str(score), False, (255, 0, 0))
    timer_surface = my_font.render(str(time), False, (255, 0, 0))


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        for obj in updatable:
            obj.update(dt)
        for asteroid in asteroids:
            if asteroid.collision(player):
                if lives <= 1:
                    print("Score is " + str(score))
                    exit("Game over!")
                else:
                    lives -= 1
                    for asteroid in asteroids:
                        asteroid.kill()
                    player.position = (SCREEN_WIDTH / 2 , SCREEN_HEIGHT / 2)
            for shot in shots:
                if asteroid.collision(shot):
                    asteroid.split()
                    asteroid.kill()
                    shot.kill()
                    score += 1

        
        pygame.Surface.fill(screen,"black")
        timer_surface = my_font.render("Time alive: " + str(time), False, (255, 0, 0))
        text_surface = my_font.render("Score: " + str(score), False, (255, 0, 0))
        lives_surface = my_font.render("Lives remaining: " + str(lives), False, (255, 0, 0))


        clocker += 1
        if clocker >= constants.FPS:
            clocker = 0
            time += 1

        screen.blit(text_surface, (100, 25))
        screen.blit(timer_surface, (100, 60))
        screen.blit(lives_surface, (100, 100))

        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()
        dt =  clock.tick(constants.FPS) / 1000
if __name__ == "__main__":
    main()