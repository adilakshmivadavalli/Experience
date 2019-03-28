import pygame
from random import *

#Double bullet supply
class Bullet_Supply(pygame.sprite.Sprite):
    def __init__(self, bg_size):
        pygame.sprite.Sprite.__init__(self)

        #Set supply bag's picture
        self.image = pygame.image.load("images/bullet_supply.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.width, self.height = bg_size[0], bg_size[1]
        #Set the position, random position and -100 height.
        self.rect.left, self.rect.bottom = \
                        randint(0, self.width - self.rect.width), -100
        #Set speed
        self.speed = 5
        self.active = False
        self.mask = pygame.mask.from_surface(self.image)

    #Set movement
    def move(self):
        if self.rect.top < self.height:
            self.rect.top += self.speed
        else:
            self.active = False

    #When supply bag goes out of screen, reset it.
    def reset(self):
        self.active = True
        self.rect.left, self.rect.bottom = \
                        randint(0, self.width - self.rect.width), -100
        
#Super bullet supply                 
class Bomb_Supply(pygame.sprite.Sprite):
    def __init__(self, bg_size):
        pygame.sprite.Sprite.__init__(self)

        #Set supply bag's picture
        self.image = pygame.image.load("images/bomb_supply.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.width, self.height = bg_size[0], bg_size[1]
        #Set the position, random position and -100 height.
        self.rect.left, self.rect.bottom = \
                        randint(0, self.width - self.rect.width), -100
        #Set speed
        self.speed = 5
        self.active = False
        self.mask = pygame.mask.from_surface(self.image)

    #Set movement
    def move(self):
        if self.rect.top < self.height:
            self.rect.top += self.speed
        else:
            self.active = False

    #When supply bag goes out of screen, reset it.
    def reset(self):
        self.active = True
        self.rect.left, self.rect.bottom = \
                        randint(0, self.width - self.rect.width), -100                                          
