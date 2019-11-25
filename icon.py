import pygame

class SwordIcon(pygame.sprite.Sprite):
    def __init__(self, x, y):
        self.image=pygame.image.load('images/sword1.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = x, y

    def draw(self, screen):
        screen.blit(self.image, self.rect)

class ShieldIcon(pygame.sprite.Sprite):
    def __init__(self, x, y):
        self.image=pygame.image.load('images/shield1.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = x, y

    def draw(self, screen):
        screen.blit(self.image, self.rect)

class LifeIcon(pygame.sprite.Sprite):
    def __init__(self, x, y):
        self.image=pygame.image.load('images/life.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = x, y

    def draw(self, screen):
        screen.blit(self.image, self.rect)

class MoneyIcon(pygame.sprite.Sprite):
    def __init__(self, x, y):
        self.image=pygame.image.load('images/money.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = x, y

    def draw(self, screen):
        screen.blit(self.image, self.rect)

class YellowKeyIcon(pygame.sprite.Sprite):
    def __init__(self, x, y):
        self.image=pygame.image.load('images/yellowkey.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = x, y

    def draw(self, screen):
        screen.blit(self.image, self.rect)

class BlueKeyIcon(pygame.sprite.Sprite):
    def __init__(self, x, y):
        self.image=pygame.image.load('images/bluekey.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = x, y

    def draw(self, screen):
        screen.blit(self.image, self.rect)

class RedKeyIcon(pygame.sprite.Sprite):
    def __init__(self, x, y):
        self.image=pygame.image.load('images/redkey.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = x, y

    def draw(self, screen):
        screen.blit(self.image, self.rect)
