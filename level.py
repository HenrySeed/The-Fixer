import pygame
import os


class Level():
    def __init__(self, player, engine, start_pos=(0,0)):

        self.start_pos = start_pos
        player.pos = [start_pos[0], start_pos[1]]

        self.player = player
        self.engine = engine

        self.objects = []

        self.image = pygame.image.load(os.path.join('level1.jpg'))
        self.image = pygame.transform.scale(self.image, (564*9, 430*9))


    def addObject(self, obj):
        self.objects.append(obj)


    def render(self, screen):

        player_x, player_y = self.player.pos

        screen.blit(self.image, (0, 0))

        for obj in self.objects:
            obj.render(screen)