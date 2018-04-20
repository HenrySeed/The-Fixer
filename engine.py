import sys
import math
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

def getPoint(pos, angle, distance):
    '''Gets a point $distance away from pos along the'''

    # NW
    if angle < -90 or angle == 180:
        if angle == 180:
            angle = 0
        else:
            angle = angle * -1
            angle = 90 - (angle - 90)
        dir = "NW"

    # NE
    elif angle < 0:
        angle = angle * -1
        angle = 90 - angle
        dir = "NE"

    # SW
    elif angle >= 90:
        angle = angle - 90
        dir = "SW"
    
    # SE
    elif angle >= 0 and angle < 90:
        dir = "SE"


    if angle == 0:
        x_length = distance
        y_length = 0
    elif dir == "NE" or dir == "SW":
        x_length = math.sin(math.radians(angle)) * distance
        y_length = math.cos(math.radians(angle)) * distance
    else:
        x_length = math.cos(math.radians(angle)) * distance
        y_length = math.sin(math.radians(angle)) * distance

    # print("DIR: {}  ANGLE: {:2f}  POS: {}".format(dir, angle, pos))

    if dir == "NE": 
        return [pos[0] + x_length, pos[1] - y_length]
    elif dir == "SE": 
        return [pos[0] + x_length, pos[1] + y_length]
    elif dir == "SW": 
        return [pos[0] - x_length, pos[1] + y_length]
    elif dir == "NW": 
        return [pos[0] - x_length, pos[1] - y_length]



class Engine():
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('The Fixer')

        pygame.mouse.set_cursor((8,8),(0,0),(0,0,0,0,0,0,0,0),(0,0,0,0,0,0,0,0))

        pygame.font.init() 
        self.myfont = pygame.font.SysFont('Minotaur Phatte', 30)   

        self.fps = 60.0
        self.fpsClock = pygame.time.Clock()
        self.level = ""

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

        keys = pygame.key.get_pressed()

        # checks for reload
        if (keys[K_LCTRL] or keys[K_LMETA]) and keys[K_r]:
            self.level.objects = []

        # checks for quit
        if (keys[K_LCTRL] or keys[K_LMETA]) and keys[K_q]:
            pygame.quit()

        for event in events:
            if event.type == QUIT:
                pygame.quit()

        self.level.update()

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

        if self.level != "":
            self.level.render(screen)

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
