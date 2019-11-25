import pygame

class Enemy(pygame.sprite.Sprite):

    def __init__(self, floor, life, attack, defend):
        pygame.sprite.Sprite.__init__(self)
        self.life = life
        self.attack = attack
        self.defend = defend
        self.floor = floor
        self.type = "enemy"
        self.active = True
        self.money = 1
        self.dead_img = pygame.image.load('images/dead.png').convert_alpha()
        
class GreenBall(Enemy):

    def __init__(self, floor, x, y):
        super().__init__(floor, 35, 18, 1)
        self.type = "enemy"
        self.images = []
        
        for i in range(1, 5):
            self.images.append(pygame.image.load('images/greenball_0'\
                                                 +str(i)+'.png').convert_alpha())

        self.rect = self.images[0].get_rect()
        self.rect.left, self.rect.top = x, y

    def draw(self, screen, index):
        if self.active:
            screen.blit(self.images[index], self.rect)
        else:
            screen.blit(self.dead_img, self.rect)
        if not self.active:
            self.floor.point[int(self.rect.left/32-4)][int(self.rect.top/32)]=0
        

class RedBall(Enemy):

    def __init__(self, floor, x, y):
        super().__init__(floor, 45, 20, 2)
        self.type = "enemy"
        self.images = []
        
        for i in range(1, 5):
            self.images.append(pygame.image.load('images/redball_0'\
                                                 +str(i)+'.png').convert_alpha())

        self.rect = self.images[0].get_rect()
        self.rect.left, self.rect.top = x, y

    def draw(self, screen, index):
        if self.active:
            screen.blit(self.images[index], self.rect)
        else:
            screen.blit(self.dead_img, self.rect)
        if not self.active:
            self.floor.point[int(self.rect.left/32-4)][int(self.rect.top/32)]=0

class SmallBat(Enemy):

    def __init__(self, floor, x, y):
        super().__init__(floor, 35, 38, 3)
        self.type = "enemy"
        self.images = []
        
        for i in range(1, 5):
            self.images.append(pygame.image.load('images/smallbat_0'\
                                                 +str(i)+'.png').convert_alpha())

        self.rect = self.images[0].get_rect()
        self.rect.left, self.rect.top = x, y

    def draw(self, screen, index):
        if self.active:
            screen.blit(self.images[index], self.rect)
        else:
            screen.blit(self.dead_img, self.rect)
        if not self.active:
            self.floor.point[int(self.rect.left/32-4)][int(self.rect.top/32)]=0

class SmallSkeleton(Enemy):

    def __init__(self, floor, x, y):
        super().__init__(floor, 50, 42, 6)
        self.type = "enemy"
        self.images = []
        
        for i in range(1, 5):
            self.images.append(pygame.image.load('images/smallskeleton_0'\
                                                 +str(i)+'.png').convert_alpha())

        self.rect = self.images[0].get_rect()
        self.rect.left, self.rect.top = x, y

    def draw(self, screen, index):
        if self.active:
            screen.blit(self.images[index], self.rect)
        else:
            screen.blit(self.dead_img, self.rect)
        if not self.active:
            self.floor.point[int(self.rect.left/32-4)][int(self.rect.top/32)]=0

class MidSkeleton(Enemy):

    def __init__(self, floor, x, y):
        super().__init__(floor, 55, 52, 12)
        self.type = "enemy"
        self.images = []
        
        for i in range(1, 5):
            self.images.append(pygame.image.load('images/midskeleton_0'\
                                                 +str(i)+'.png').convert_alpha())

        self.rect = self.images[0].get_rect()
        self.rect.left, self.rect.top = x, y

    def draw(self, screen, index):
        if self.active:
            screen.blit(self.images[index], self.rect)
        else:
            screen.blit(self.dead_img, self.rect)
        if not self.active:
            self.floor.point[int(self.rect.left/32-4)][int(self.rect.top/32)]=0

class SmallMaster(Enemy):

    def __init__(self, floor, x, y):
        super().__init__(floor, 60, 32, 8)
        self.type = "enemy"
        self.images = []
        
        for i in range(1, 5):
            self.images.append(pygame.image.load('images/smallmaster_0'\
                                                 +str(i)+'.png').convert_alpha())

        self.rect = self.images[0].get_rect()
        self.rect.left, self.rect.top = x, y

    def draw(self, screen, index):
        if self.active:
            screen.blit(self.images[index], self.rect)
        else:
            screen.blit(self.dead_img, self.rect)
        if not self.active:
            self.floor.point[int(self.rect.left/32-4)][int(self.rect.top/32)]=0

class SmallGuard(Enemy):

    def __init__(self, floor, x, y):
        super().__init__(floor, 50, 48, 22)
        self.type = "speicl1"
        self.images = []
        
        for i in range(1, 5):
            self.images.append(pygame.image.load('images/smallguard_0'\
                                                 +str(i)+'.png').convert_alpha())

        self.rect = self.images[0].get_rect()
        self.rect.left, self.rect.top = x, y

    def draw(self, screen, index):
        if self.active:
            screen.blit(self.images[index], self.rect)
        else:
            screen.blit(self.dead_img, self.rect)
        if not self.active:
            self.floor.point[int(self.rect.left/32-4)][int(self.rect.top/32)]=0

class MidGuard(Enemy):

    def __init__(self, floor, x, y):
        super().__init__(floor, 50, 100, 20)
        self.type = "enemy"
        self.images = []
        
        for i in range(1, 5):
            self.images.append(pygame.image.load('images/midguard_0'\
                                                 +str(i)+'.png').convert_alpha())

        self.rect = self.images[0].get_rect()
        self.rect.left, self.rect.top = x, y

    def draw(self, screen, index):
        if self.active:
            screen.blit(self.images[index], self.rect)
        else:
            screen.blit(self.dead_img, self.rect)
        if not self.active:
            self.floor.point[int(self.rect.left/32-4)][int(self.rect.top/32)]=0


class BigSkeleton(Enemy):

    def __init__(self, floor, x, y):
        super().__init__(floor, 100, 65, 15)
        self.type = "enemy"
        self.images = []
        
        for i in range(1, 5):
            self.images.append(pygame.image.load('images/bigskeleton_0'\
                                                 +str(i)+'.png').convert_alpha())

        self.rect = self.images[0].get_rect()
        self.rect.left, self.rect.top = x, y

    def draw(self, screen, index):
        if self.active:
            screen.blit(self.images[index], self.rect)
        else:
            screen.blit(self.dead_img, self.rect)
        if not self.active:
            self.floor.point[int(self.rect.left/32-4)][int(self.rect.top/32)]=0

class Floor8Special(Enemy):

    def __init__(self, floor, x, y):
        super().__init__(floor, 100, 65, 15)
        self.type = "special2"
        self.images = []
        
        for i in range(1, 5):
            self.images.append(pygame.image.load('images/midskeleton_0'\
                                                 +str(i)+'.png').convert_alpha())

        self.rect = self.images[0].get_rect()
        self.rect.left, self.rect.top = x, y

    def draw(self, screen, index):
        if self.active:
            screen.blit(self.images[index], self.rect)
        else:
            screen.blit(self.dead_img, self.rect)
        if not self.active:
            self.floor.point[int(self.rect.left/32-4)][int(self.rect.top/32)]=0
