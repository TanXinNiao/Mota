import pygame
from floor import *

class Door(pygame.sprite.Sprite):
    def __init__(self, floor):
        #门类型
        self.type = "door"
        self.floor = floor

class YellowDoor(Door):
    def __init__(self, floor, x , y):
        super().__init__(floor)
        self.images = []
        for i in range(1, 5):
            self.images.append(pygame.image.load('images/yellowdoor_0'\
                                                 +str(i)+'.png').convert_alpha())
        self.doortype = "yellow"
        self.open = False
        self.status = 0
        self.rect = self.images[0].get_rect()
        self.rect.left, self.rect.top = x, y

    #由于key只有一张图片，这里的index没用，但是还是要加上
    def draw(self, screen, index):
        if self.open == False:
            screen.blit(self.images[0], self.rect)
        else:
            screen.blit(self.images[self.status], self.rect)
            self.status += 1
        if self.status == 4:
            self.floor.point[int(self.rect.left/32-4)][int(self.rect.top/32)]=0

class BlueDoor(Door):
    def __init__(self, floor, x , y):
        super().__init__(floor)
        self.images = []
        for i in range(1, 5):
            self.images.append(pygame.image.load('images/bluedoor_0'\
                                                 +str(i)+'.png').convert_alpha())
        self.doortype = "blue"
        self.open = False
        self.status = 0
        self.rect = self.images[0].get_rect()
        self.rect.left, self.rect.top = x, y

    #由于key只有一张图片，这里的index没用，但是还是要加上
    def draw(self, screen, index):
        if self.open == False:
            screen.blit(self.images[0], self.rect)
        else:
            screen.blit(self.images[self.status], self.rect)
            self.status += 1
        if self.status == 4:
            self.floor.point[int(self.rect.left/32-4)][int(self.rect.top/32)]=0

class RedDoor(Door):
    def __init__(self, floor, x , y):
        super().__init__(floor)
        self.images = []
        for i in range(1, 5):
            self.images.append(pygame.image.load('images/reddoor_0'\
                                                 +str(i)+'.png').convert_alpha())
        self.doortype = "red"
        self.open = False
        self.status = 0
        self.rect = self.images[0].get_rect()
        self.rect.left, self.rect.top = x, y

    #由于key只有一张图片，这里的index没用，但是还是要加上
    def draw(self, screen, index):
        if self.open == False:
            screen.blit(self.images[0], self.rect)
        else:
            screen.blit(self.images[self.status], self.rect)
            self.status += 1
        if self.status == 4:
            self.floor.point[int(self.rect.left/32-4)][int(self.rect.top/32)]=0
        
class SpecialDoor(Door):
    def __init__(self, floor, x , y):
        super().__init__(floor)
        self.images = []
        for i in range(1, 5):
            self.images.append(pygame.image.load('images/specialdoor_0'\
                                                 +str(i)+'.png').convert_alpha())
        self.doortype = "special"
        self.open = False
        self.status = 0
        self.rect = self.images[0].get_rect()
        self.rect.left, self.rect.top = x, y

    #由于key只有一张图片，这里的index没用，但是还是要加上
    def draw(self, screen, index):
        if self.open == False:
            screen.blit(self.images[0], self.rect)
        else:
            screen.blit(self.images[self.status], self.rect)
            self.status += 1
        if self.status == 4:
            self.floor.point[int(self.rect.left/32-4)][int(self.rect.top/32)]=0
                            
                               
            
