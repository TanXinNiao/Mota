import pygame

class Item(pygame.sprite.Sprite):
    def __init__(self, floor):
        #物品类型
        self.type = "item"
        self.active = True
        self.floor = floor

class YellowKey(Item):
    def __init__(self, floor, x , y):
        super().__init__(floor)
        self.itemtype = "yellowkey"
        self.image=pygame.image.load('images/yellowkey.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = x, y

    #由于key只有一张图片，这里的index没用，但是还是要加上
    def draw(self, screen, index):
        if self.active:
            screen.blit(self.image, self.rect)
        else:
            self.floor.point[int(self.rect.left/32-4)][int(self.rect.top/32)]=0
            

class BlueKey(Item):
    def __init__(self, floor, x , y):
        super().__init__(floor)
        self.itemtype = "bluekey"
        self.image=pygame.image.load('images/bluekey.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = x, y

    def draw(self, screen, index):
        if self.active:
            screen.blit(self.image, self.rect)
        else:
            self.floor.point[int(self.rect.left/32-4)][int(self.rect.top/32)]=0

class RedKey(Item):
    def __init__(self, floor,x , y):
        super().__init__(floor)
        self.itemtype = "redkey"
        self.image=pygame.image.load('images/redkey.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = x, y

    def draw(self, screen, index):
        if self.active:
            screen.blit(self.image, self.rect)
        else:
            self.floor.point[int(self.rect.left/32-4)][int(self.rect.top/32)]=0

class RedLife(Item):
    def __init__(self, floor, x , y):
        super().__init__(floor)
        self.itemtype = "redlife"
        self.image=pygame.image.load('images/redlife.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = x, y

    def draw(self, screen, index):
        if self.active:
            screen.blit(self.image, self.rect)
        else:
            self.floor.point[int(self.rect.left/32-4)][int(self.rect.top/32)]=0

class BlueLife(Item):
    def __init__(self, floor, x , y):
        super().__init__(floor)
        self.itemtype = "bluelife"
        self.image=pygame.image.load('images/bluelife.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = x, y

    def draw(self, screen, index):
        if self.active:
            screen.blit(self.image, self.rect)
        else:
            self.floor.point[int(self.rect.left/32-4)][int(self.rect.top/32)]=0

class RedCrystal(Item):
    def __init__(self, floor, x , y):
        super().__init__(floor)
        self.itemtype = "redcrystal"
        self.image=pygame.image.load('images/redcrystal.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = x, y

    def draw(self, screen, index):
        if self.active:
            screen.blit(self.image, self.rect)
        else:
            self.floor.point[int(self.rect.left/32-4)][int(self.rect.top/32)]=0

class BlueCrystal(Item):
    def __init__(self, floor, x , y):
        super().__init__(floor)
        self.itemtype = "bluecrystal"
        self.image=pygame.image.load('images/bluecrystal.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = x, y

    def draw(self, screen, index):
        if self.active:
            screen.blit(self.image, self.rect)
        else:
            self.floor.point[int(self.rect.left/32-4)][int(self.rect.top/32)]=0

class Sword1(Item):
    def __init__(self, floor, x , y):
        super().__init__(floor)
        self.itemtype = "sword1"
        self.image=pygame.image.load('images/sword1.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = x, y

    def draw(self, screen, index):
        if self.active:
            screen.blit(self.image, self.rect)
        else:
            self.floor.point[int(self.rect.left/32-4)][int(self.rect.top/32)]=0

class Shield1(Item):
    def __init__(self, floor, x , y):
        super().__init__(floor)
        self.itemtype = "shield1"
        self.image=pygame.image.load('images/shield1.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = x, y

    def draw(self, screen, index):
        if self.active:
            screen.blit(self.image, self.rect)
        else:
            self.floor.point[int(self.rect.left/32-4)][int(self.rect.top/32)]=0
