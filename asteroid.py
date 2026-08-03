import pygame
import random
from logger import log_event
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface,) -> None:
        pygame.draw.circle(screen, "white", self.position , self.radius, LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.position += (self.velocity * dt)

    def split(self):
        pygame.sprite.Sprite.kill(self)

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        angle = random.uniform(20, 50)
        asteroid1_vector = self.velocity.rotate(angle)
        asteroid2_vector = self.velocity.rotate(-angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        asteroid1 = Asteroid(self.position[0], self.position[1], new_radius)
        asteroid2 = Asteroid(self.position[0], self.position[1], new_radius)

        asteroid1.velocity = asteroid1_vector * 1.2
        asteroid2.velocity = asteroid2_vector * 1.2