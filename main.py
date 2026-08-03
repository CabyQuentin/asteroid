import pygame
import sys
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, drawable, updatable)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0.0

    asteroid_field = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        for thing in updatable:
            thing.update(dt)
        for asteroid in asteroids:
            if asteroid.collide_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collide_with(shot):
                    log_event("asteroid_shot")
                    asteroid.split()
                    pygame.sprite.Sprite.kill(shot)
        for thing in drawable:
            thing.draw(screen)
        pygame.display.flip()

        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
