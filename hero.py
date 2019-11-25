import pygame
from enemy import *
from floor import *
from items import *
from terrain import *

class Hero(pygame.sprite.Sprite):
    def __init__(self):
        self.attack = 10
        self.defend = 10
        self.life = 10000
        
        self.images = []
        #表示勇士的朝向
        self.status = 1
        #钥匙数量
        self.yellowkey = 0
        self.bluekey = 0
        self.redkey = 0

        #这个move表示移动方向，1下2左3右4上0不移动
        self.move = 0

        self.money = 0
        for i in range(1, 17):
            self.images.append(pygame.image.load('images/hero_'\
                                                 +str(i)+'.png').convert_alpha())
        self.rect = self.images[0].get_rect()
        self.rect.left, self.rect.top = 10*32, 11*32

        #记录数据
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 36)

        #勇士所在的楼层数
        self.floor_num = 1

        #勇士上下楼梯状态
        self.stair = 0


    def pk(self, enemy):
        damage1 = self.attack - enemy.defend
        damage2 = enemy.attack - self.defend
        self.money += enemy.money

        while(True):
            enemy.life -= damage1
            if enemy.life <= 0:
                break

            self.life -= damage2
            if self.life < 0:
                print("游戏结束")

    def moveUp(self):
        self.move = 4

    def moveDown(self, screen, index, floor):
        self.move = 1

    def moveLeft(self, screen, index, floor):
        self.move = 2

    def moveRight(self, screen, index, floor):
        self.move = 3

    def draw(self, screen, index):
        if index == 0:
            screen.blit(self.images[(self.status-1)*4], self.rect)
        else:
            screen.blit(self.images[index+(self.status-1)*4], self.rect)
        

    def prep_data(self):
        life_str = str(self.life)
        attack_str = str(self.attack)
        defend_str = str(self.defend)
        money_str = str(self.money)
        yellowkey_str = str(self.yellowkey)
        bluekey_str = str(self.bluekey)
        redkey_str = str(self.redkey)
        floor_num_str = "Floor  "+str(self.floor_num)

        self.attack_image = self.font.render(attack_str, True, self.text_color,
                                           (200, 200, 200))
        self.defend_image = self.font.render(defend_str, True, self.text_color,
                                           (200, 200, 200))
        self.money_image = self.font.render(money_str, True, self.text_color,
                                           (200, 200, 200))
        self.yellowkey_image = self.font.render(yellowkey_str, True, self.text_color,
                                           (200, 200, 200))
        self.life_image = self.font.render(life_str, True, self.text_color,
                                           (200, 200, 200))
        self.bluekey_image = self.font.render(bluekey_str, True, self.text_color,
                                           (200, 200, 200))
        self.redkey_image = self.font.render(redkey_str, True, self.text_color,
                                           (200, 200, 200))
        self.floor_num_image = self.font.render(floor_num_str, True, self.text_color,
                                           (200, 200, 200))

        self.floor_num_rect = self.life_image.get_rect()
        self.floor_num_rect.left = 20
        self.floor_num_rect.top = 20

        self.life_rect = self.life_image.get_rect()
        self.life_rect.left = 36
        self.life_rect.top = 68

        self.attack_rect = self.life_image.get_rect()
        self.attack_rect.left = 36
        self.attack_rect.top = 100

        self.defend_rect = self.life_image.get_rect()
        self.defend_rect.left = 36
        self.defend_rect.top = 132

        self.money_rect = self.life_image.get_rect()
        self.money_rect.left = 36
        self.money_rect.top = 164

        self.yellowkey_rect = self.life_image.get_rect()
        self.yellowkey_rect.left = 36
        self.yellowkey_rect.top = 228

        self.bluekey_rect = self.life_image.get_rect()
        self.bluekey_rect.left = 36
        self.bluekey_rect.top = 260

        self.redkey_rect = self.life_image.get_rect()
        self.redkey_rect.left = 36
        self.redkey_rect.top = 292

    def show_data(self, screen):
        screen.blit(self.life_image, self.life_rect)
        screen.blit(self.attack_image, self.attack_rect)
        screen.blit(self.defend_image, self.defend_rect)
        screen.blit(self.money_image, self.money_rect)
        screen.blit(self.yellowkey_image, self.yellowkey_rect)
        screen.blit(self.bluekey_image, self.bluekey_rect)
        screen.blit(self.redkey_image, self.redkey_rect)
        screen.blit(self.floor_num_image, self.floor_num_rect)
        
        
