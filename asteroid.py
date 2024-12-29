import pygame
import random

from constants import *
from circleshape import CircleShape


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        angel = random.uniform(20, 50)
        rad = self.radius - ASTEROID_MIN_RADIUS
        v1 = self.velocity.rotate(angel)
        v2 = self.velocity.rotate(-angel)

        ast1 = Asteroid(self.position.x, self.position.y, rad)
        ast2 = Asteroid(self.position.x, self.position.y, rad)

        ast1.velocity = v1 * 1.2
        ast2.velocity = v2 * 1.2

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
