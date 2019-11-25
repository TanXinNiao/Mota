import pygame
import sys
from hero import *
from enemy import *
from floor import *
from icon import *
from pygame.locals import *

"""floor1 = Floor1()
hero = Hero()
              
hero.point_x -= 1
floor1.searchEvent(hero, hero.point_x, hero.point_y)
print(hero.life)"""

pygame.init()

tick = pygame.time.Clock()

screen = pygame.display.set_mode((672, 416), 0, 32)
pygame.display.set_caption("魔塔 -- 贪心鸟")

background = pygame.image.load('images/background.png')
screen.blit(background, (0, 0))


rect = background.get_rect()


#ball = GreenBall()

delay = 100

running = True

#地图中怪物“动态”图片索引
index = 0
#英雄移动索引
move_index = 0
#初始化楼层
floor1 = Floor1()
floor2 = Floor2()
floor3 = Floor3()
floor4 = Floor4()
floor5 = Floor5()
floor6 = Floor6()
floor7 = Floor7()
floor8 = Floor8()
floor9 = Floor9()
floor10 = Floor10()

hero = Hero()
floor = floor1
life_icon = LifeIcon(0, 64)
sword_icon = SwordIcon(0, 96)
shield_icon = ShieldIcon(0, 128)
money_icon = MoneyIcon(0, 160)
yellowkey_icon = YellowKeyIcon(0, 224)
bluekey_icon = BlueKeyIcon(0, 256)
redkey_icon = RedKeyIcon(0, 288)

def draw_icon(screen):
    life_icon.draw(screen)
    sword_icon.draw(screen)
    shield_icon.draw(screen)
    money_icon.draw(screen)
    yellowkey_icon.draw(screen)
    bluekey_icon.draw(screen)
    redkey_icon.draw(screen)

while running:
    if hero.floor_num == 1:
        floor = floor1
    elif hero.floor_num == 2:
        floor = floor2
    elif hero.floor_num == 3:
        floor = floor3
    elif hero.floor_num == 4:
        floor = floor4
    elif hero.floor_num == 5:
        floor = floor5
    elif hero.floor_num == 6:
        floor = floor6
    elif hero.floor_num == 7:
        floor = floor7
    elif hero.floor_num == 8:
        floor = floor8
    elif hero.floor_num == 9:
        floor = floor9
    elif hero.floor_num == 10:
        floor = floor10
    hero.prep_data()
    screen.blit(background, (0, 0))
    #更新上下楼勇士的位置
    floor.set_hero_pos(hero)
    floor.draw(screen, index, hero)
    draw_icon(screen)
    hero.draw(screen, move_index)
    hero.show_data(screen)
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
    
    if not(delay%10):
        floor.draw(screen, index, hero)
        index = (index+1)%4
  
    if hero.move == 1:
        if floor.searchEvent(screen, index, hero, int(hero.rect.left/32)-4, \
                             int((hero.rect.bottom+1)/32)):
            hero.status = 1
            hero.rect.top += 8
            move_index = (move_index+1)%4
            if move_index == 0:
                hero.move = 0
        else:
            hero.status = 1
            hero.move = 0

    if hero.move == 2:
        if floor.searchEvent(screen, index, hero, int((hero.rect.left-1)/32)-4, \
                             int(hero.rect.top/32)):
            hero.status = 2
            hero.rect.left -= 8
            move_index = (move_index+1)%4
            if move_index == 0:
                hero.move = 0
        else:
            hero.status = 2
            hero.move = 0


    if hero.move == 3:
        if floor.searchEvent(screen, index, hero, int((hero.rect.right+1)/32)-4, \
                             int(hero.rect.top/32)):
            hero.status = 3
            screen.blit(hero.images[index+(hero.status-1)*4], hero.rect)
            hero.rect.left += 8
            move_index = (move_index+1)%4
            if move_index == 0:
                hero.move = 0
        else:
            hero.status =3
            hero.move = 0

    if hero.move == 4:
        if floor.searchEvent(screen, index, hero, 
                                 int(hero.rect.left/32-4),
                                 int((hero.rect.top-1)/32)):
            hero.status = 4
            hero.rect.top -= 8
            move_index = (move_index+1)%4
            if move_index == 0:
                hero.move = 0
        else:
            hero.status = 4
            hero.move = 0

    

    #检测键盘操作
    key_pressed=pygame.key.get_pressed()
    if key_pressed[K_w] or key_pressed[K_UP]:
        hero.moveUp()
    if key_pressed[K_s] or key_pressed[K_DOWN]:
        hero.moveDown(screen, index, floor)            
    if key_pressed[K_a] or key_pressed[K_LEFT]:
        hero.moveLeft(screen, index, floor)
    if key_pressed[K_d] or key_pressed[K_RIGHT]:
        hero.moveRight(screen, index, floor)
        
    delay-=1
    if not delay:
        delay=100

    pygame.display.flip()
    tick.tick(60)
