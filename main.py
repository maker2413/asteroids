import pygame
import sys

from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import *
from player import Player
from player import Shot

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
    shots = pygame.sprite.Group

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Player.containers = (updatable, drawable)
    Shot.containers = (updatable, drawable)

    player = Player(x=SCREEN_WIDTH/2, y=SCREEN_HEIGHT/2)
    asteroidField = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill(color="black")

        for u in updatable:
            u.update(dt=dt)
        for d in drawable:
            d.draw(screen=screen)
        for a in asteroids:
            if a.check_collision(player):
                print("Game Over!")
                sys.exit(0)

        pygame.display.flip()

        dt = clock.tick(60) / 1000

# This line ensures the main() function is only called when this file is run
# directly; it won't run if it's imported as a module. It's considered the
# "pythonic" way to structure an executable program in Python. Technically, the
# program will work fine by just calling main(), but you might get an angry
# letter from Guido van Rossum if you don't.
if __name__ == "__main__":
    main()
