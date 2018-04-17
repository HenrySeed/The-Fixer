import math
import pygame



class Projectile():
    def __init__(self, angle, start):
        self.start = [start[0], start[1]]
        self.angle = angle
        self.dist = 0

        self.color = (255, 255, 255)

    def render(self, screen):
        x_dist = math.sin(self.angle)*self.dist
        y_dist = math.sqrt(self.dist**2 + x_dist**2)

        # pygame.draw.line(screen, self.color, self.start, (self.start[0] + x_dist, self.start[1] + y_dist))
        pygame.draw.line(screen, self.color, (100, 100), (self.start[0] - 10, self.start[1] - 10), 1)
