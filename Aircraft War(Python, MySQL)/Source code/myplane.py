import pygame

#pygame.sprite.Sprite used to draw plane
class MyPlane(pygame.sprite.Sprite):
    
    #Generate the plane in screen
    def __init__(self, bg_size):
        pygame.sprite.Sprite.__init__(self)

        #Make the plane looks flying
        self.image1 = pygame.image.load("images/me1.png").convert_alpha()
        self.image2 = pygame.image.load("images/me2.png").convert_alpha()

        #Make destroy in progress
        self.destroy_images = []
        self.destroy_images.extend([\
            pygame.image.load("images/me_destroy_1.png").convert_alpha(), \
            pygame.image.load("images/me_destroy_2.png").convert_alpha(), \
            pygame.image.load("images/me_destroy_3.png").convert_alpha(), \
            pygame.image.load("images/me_destroy_4.png").convert_alpha() \
            ])

        #Put player's plane in screen
        self.rect = self.image1.get_rect()
        self.width, self.height = bg_size[0], bg_size[1]
        
        #Set position in the middle bottom
        self.rect.left, self.rect.top = \
                        (self.width - self.rect.width) // 2, \
                        self.height - self.rect.height - 60
        #Set plane's speed
        self.speed = 10
        self.active = True
        #Invincible signal
        self.invincible = False
        #Used to detect collision
        self.mask = pygame.mask.from_surface(self.image1)

    #Set the position when plane go up. Rect used to detect collision
    def moveUp(self):
        #Top
        if self.rect.top > 0:
            self.rect.top -= self.speed
        else:
            self.rect.top = 0

    def moveDown(self):
        #Bottom
        if self.rect.bottom < self.height - 60:
            self.rect.top += self.speed
        else:
            self.rect.bottom = self.height - 60

    def moveLeft(self):
        #Left
        if self.rect.left > 0:
            self.rect.left -= self.speed
        else:
            self.rect.left = 0

    def moveRight(self):
        #Right
        if self.rect.right < self.width:
            self.rect.left += self.speed
        else:
            self.rect.right = self.width

    #Reset player's plane if player's plane down for multiple chance
    def reset(self):
        self.rect.left, self.rect.top = \
                        (self.width - self.rect.width) // 2, \
                        self.height - self.rect.height - 60
        self.active = True
        self.invincible = True
