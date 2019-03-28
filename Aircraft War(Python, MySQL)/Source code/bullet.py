import pygame

#Normal bullet
class Bullet1(pygame.sprite.Sprite):
    def __init__(self, position):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images/bullet1.png").convert_alpha()
        #Get rect
        self.rect = self.image.get_rect()
        #Initiate bullet position 
        self.rect.left, self.rect.top = position
        #Set speed
        self.speed = 12
        self.active = False
        #Check collision
        self.mask = pygame.mask.from_surface(self.image)

    def move(self):
        #Move to top
        self.rect.top -= self.speed

        if self.rect.top < 0:
            self.active = False

    #When player move plane, reset the bullet position
    def reset(self, position):
        self.rect.left, self.rect.top = position
        self.active = True

#Double bullet
class Bullet2(pygame.sprite.Sprite):
    def __init__(self, position):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images/bullet2.png").convert_alpha()
        #Get rect
        self.rect = self.image.get_rect()
        #Initiate bullet position 
        self.rect.left, self.rect.top = position
        #Set speed
        self.speed = 14
        self.active = False
        #Check collision
        self.mask = pygame.mask.from_surface(self.image)

    def move(self):
        #Move to top
        self.rect.top -= self.speed

        if self.rect.top < 0:
            self.active = False
            
    #When player move plane, reset the bullet position
    def reset(self, position):
        self.rect.left, self.rect.top = position
        self.active = True
    
