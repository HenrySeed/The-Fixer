from engine import *
from math import *
import os

from projectile import *


class Player():
    def __init__(self, eengine):
        self.pos = [0,0]

        self.engine = eengine

        self.movementSpeed = 5
        self.look_angle = 0

        self.image = pygame.image.load(os.path.join('player.gif'))
        self.image = pygame.transform.scale(self.image, (90, 90))


    def render(self, screen):

        x = int(self.engine.screen_width / 2)
        y = int(self.engine.screen_height / 2)
        
        textsurface = self.engine.myfont.render(str(self.look_angle), False, (255, 255, 255))
        screen.blit(textsurface,(10,10))

        x_y_string = "Cursor X: " + str(self.engine.cursor_x) + "  Cursor Y: " + str(self.engine.cursor_y)
        textsurface = self.engine.myfont.render(x_y_string, False, (255, 255, 255))
        screen.blit(textsurface,(10,40))

        x_y_string = "X: " + str(self.pos[0]) + "  Y: " + str(self.pos[1])
        textsurface = self.engine.myfont.render(x_y_string, False, (255, 255, 255))
        screen.blit(textsurface,(10,70))

        # Draw shadow
        pygame.draw.circle(screen, (0, 0, 0, 10), self.pos, 30)

        #draw surf to screen and catch the rect that blit returns
        blittedRect = Rect(self.pos[0]-45, self.pos[1]-45, 90, 90)

        #get center of surf for later
        oldCenter = blittedRect.center

        #rotate surf by DEGREE amount degrees
        rotatedSurf =  pygame.transform.rotate(self.image, (self.look_angle * -1) + 8)

        #get the rect of the rotated surf and set it's center to the oldCenter
        rotRect = rotatedSurf.get_rect()
        rotRect.center = oldCenter

        #draw rotatedSurf with the corrected rect so it gets put in the proper spot
        screen.blit(rotatedSurf, rotRect)

        for col in range(0, 10):
            for row in range(0, 10):
                engine_draw(screen, [int(self.engine.cursor_x+col/2), int(self.engine.cursor_y+row/2)], (255, 255, 255))




    def update(self, events):

        x = self.pos[0]
        y = self.pos[1]

        self.engine.cursor_x, self.engine.cursor_y = pygame.mouse.get_pos()
        self.look_angle = degrees(atan2(self.engine.cursor_y - y, self.engine.cursor_x - x))

        # self.image = pygame.transform.rotate(self.image, 30)

        keys = pygame.key.get_pressed()
        x_change = 0
        y_change = 0

        if keys[K_w]:
            y_change = -1 * self.movementSpeed

        if keys[K_s]:
            y_change = self.movementSpeed

        if keys[K_a]:
            x_change = -1 * self.movementSpeed

        if keys[K_d]:
            x_change = self.movementSpeed

        self.pos[0] += x_change
        self.pos[1] += y_change

        
