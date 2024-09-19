# this allows us to use code from
# the open-source pygame library
# throughout this file
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shots import *
import pygame
import sys

def main():
    pygame.init()
    print("Starting asteroids!")
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Shot.containers = (shots, updatable, drawable)
    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = updatable

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        for obj in updatable:
            obj.update(dt)
        for asteroid in asteroids:
            if player.is_colliding(asteroid):
                print("Game Over, pal!")
                sys.exit()

        for asteroid in asteroids:
            for shot in shots:
                if shot.is_colliding(asteroid):
                    asteroid.split()
                    shot.kill()
        screen.fill("black")
        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()
        time = clock.tick(60)
        dt = time/1000


if __name__ == "__main__":
    main()
