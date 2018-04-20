import math
import pygame
import engine



class Projectile():
    def __init__(self, start, cursor, angle):
        self.start = [start[0], start[1]]
        self.cursorPos = cursor

        self.angle = angle
        self.progress = 1                       # progress of the bullet towards its trajectory
        self.speed = 40                         # speed of the projectile

        self.color = (255, 255, 255)
        self.bullet_length = 6

        self.end = engine.getPoint(start, angle, 1000)


    def update(self):
        self.progress += self.speed


    def render(self, screen):    

        bullet_start = engine.getPoint(self.start, self.angle, self.progress)
        bullet_end = engine.getPoint(self.start, self.angle, self.progress + self.bullet_length)

        pygame.draw.line(screen, self.color, bullet_start, bullet_end, 3)
