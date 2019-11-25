import pygame

class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y):
        #地形类型
        self.type = "terrain"
        self.image=pygame.image.load('images/wall.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = x, y

    #由于Wall只有一张图片，这里的index没用，但是还是要加上
    def draw(self, screen, index):
        screen.blit(self.image, self.rect)
