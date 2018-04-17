import sys

import time

# Import non-standard modules.
import pygame
from pygame.locals import *


def engine_draw(screen, pos, rgb=[0,0,0]):
    x, y = pos
    screen.set_at((x, y), rgb)

def rgb(hexColor):
    hexColor = hexColor.replace('#', '')
    return tuple(int(hexColor[i:i+2], 16) for i in (0, 2, 4))

def rot_center(image, angle):
    """rotate a Surface, maintaining position."""

    loc = image.get_rect().center  #rot_image is not defined 
    print(loc)
    rot_sprite = pygame.transform.rotate(image, angle)
    rot_sprite.get_rect().center = loc
    return rot_sprite


class Engine():
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('The Fixer')

        pygame.mouse.set_cursor((8,8),(0,0),(0,0,0,0,0,0,0,0),(0,0,0,0,0,0,0,0))

        pygame.font.init() 
        self.myfont = pygame.font.SysFont('Minotaur Phatte', 30)   

        self.fps = 60.0
        self.fpsClock = pygame.time.Clock()

        self.screen_width = 1200
        self.screen_height = 900

        self.camera_pos = (0, 0)

        self.cursor_x = 0
        self.cursor_y = 0

        # List of objects to be drawn in frame
        self.objects = []
        self.background_color = (0,0,0)

        # Set up the window.
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))        

    def update(self, dt):
        # Go through events that are passed to the script by the window.
        events = pygame.event.get()

        for event in events:
            if event.type == QUIT:
                pygame.quit()

            for obj in self.objects:
                try:
                    obj.checkKeys(event)    
                except:
                    pass  

        for obj in self.objects:
            try:
                obj.update(events)    
            except:
                pass              

    def draw(self, screen):
        """
        Draw things to the window. Called once per frame.
        """
        screen.fill(self.background_color) # Fill the screen with black.

        for obj in self.objects:
            obj.render(screen)

        pygame.display.flip()

    def loop(self):
        dt = 1/self.fps # dt is the time since last frame.
        while True:
            self.update(dt)
            self.draw(self.screen)
            dt = self.fpsClock.tick(self.fps)

    def addObject(self, obj):
        self.objects.append(obj)


class rect_128():
    def __init__(self, x, y, width, height, background=[0, 0, 0]):
        # List of pixel coords to be drawn in window
        self.coords = []
        self.visible = True
        self.background = background

        for i in range(x, x+width):
            self.coords.append([i, y])
            self.coords.append([i, y+height])

        for i in range(y, y+height):
            self.coords.append([x, i])
            self.coords.append([x+width, i])

    def render(self, screen):
        for (x, y) in self.coords:
            engine_draw(screen, [x, y], self.background)


class sprite_128():
    def __init__(self, path, pos=[0,0]):
        self.img = None
        self.pos = pos
        self.load(path)
        self.visible = True

    def load(self, path):
        self.img = pygame.image.load(path)

    def render(self, screen):
        screen.blit(pygame.transform.scale(self.img, (512, 512)), self.pos)
        pygame.display.flip()















    #
