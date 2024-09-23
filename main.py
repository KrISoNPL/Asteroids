import pygame
import sys

from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import Shot

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

def main():
    pygame.init()
    clock = pygame.time.Clock()    
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group() 
    shots = pygame.sprite.Group()

    Player.containers = (updatable,drawable)
    Asteroid.containers = (updatable,drawable,asteroids)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable, shots)

    player = Player(SCREEN_WIDTH / 2,SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    while 0 == 0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
                      
        for obj in updatable:
            obj.update(dt)

        for obj in asteroids:
            if player.check_collisions(obj):
                print("Game over!")
                sys.exit()
            for shot in shots:
                if shot.check_collisions(obj):
                    shot.kill()
                    obj.split()

        pygame.Surface.fill(screen, "black")

        for obj in drawable:
            obj.draw(screen)          

        pygame.display.flip()

        # limit the framerate to 60 FPS        
        dt = clock.tick(60) / 1000


if(__name__ == "__main__"):
    main()
