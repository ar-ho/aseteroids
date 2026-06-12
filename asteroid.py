#!/usr/bin/env python3

from circleshape import *
from constants import *
import pygame
import random
from logger import log_event

class Asteroid(CircleShape):

    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)
        #calls the constructor of the parent class CircleShape to initialize the position and radius of the asteroid

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)
        #draws the asteroid on the screen as a white circle 
        # with the specified position and radius

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt
        #updates the position of the asteroid based on its velocity 
        #and the time delta (dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            new_angle = random.uniform(20,50)
            first_asteroid_vector = self.velocity.rotate(new_angle)
            second_asteroid_vector = self.velocity.rotate(-new_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid1.velocity = first_asteroid_vector * 1.2
            asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid2.velocity = second_asteroid_vector * 1.2