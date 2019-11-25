import pygame
from enemy import *
from hero import *
from terrain import *
from items import *
from door import *
from stair import *
from PyQt5 import QtWidgets

class Floor():
    def __init__(self):
        #将地图分成13*13个方格，方格中如果储存的是0则为地板
        self.point = [[0 for i in range(13)] for i in range(13)]

        for i in range(13):
            self.point[i][0] = Wall((i+4)*32, 0)
        for i in range(11):
            self.point[0][i+1] = Wall(4*32, (i+1)*32)
        for i in range(11):
            self.point[12][i+1] = Wall(16*32, (i+1)*32)
        for i in range(13):
            self.point[i][12] = Wall((i+4)*32, 12*32)

        #特殊门开的标记事件
        self.special1 = 0
        self.special2 = 0
        self.special2start = False

    def searchEvent(self, screen, index, hero, x, y):
        
        if hero.floor_num==10 and x==6 and y ==6 and self.special2start==False:
            self.special2start=True
            hero.rect.left = 10 * 32
            hero.rect.top = 5 * 32
            self.point[1][3] = 0
            self.point[2][3] = 0
            self.point[3][3] = 0
            self.point[2][4] = 0
            self.point[9][3] = 0
            self.point[10][3] = 0
            self.point[11][3] = 0
            self.point[10][4] = 0
            self.point[6][4] = 0
            self.point[5][4] = Floor8Special(self, 9*32, 4*32)
            self.point[6][4] = Floor8Special(self, 10*32, 4*32)
            self.point[7][4] = Floor8Special(self, 11*32, 4*32)
            self.point[5][5] = Floor8Special(self, 9*32, 5*32)
            self.point[7][5] = Floor8Special(self, 11*32, 5*32)
            self.point[5][6] = Floor8Special(self, 9*32, 6*32)
            self.point[6][6] = Floor8Special(self, 10*32, 6*32)
            self.point[7][6] = Floor8Special(self, 11*32, 6*32)
            self.point[6][3] = SpecialDoor(self, 10*32, 3*32)
            self.point[6][7] = SpecialDoor(self, 10*32, 7*32)
            self.point[6][2] = BigSkeleton(self, 10*32, 2*32)
            return False

        if self.point[x][y] == 0:
            return True
        
        if self.point[x][y].type == "enemy":
            hero.pk(self.point[x][y])
            self.point[x][y].active = False
            return False

        if self.point[x][y].type == "speicl1":
            hero.pk(self.point[x][y])
            self.special1 += 1
            self.point[x][y].active = False
            return False
        
        if self.point[x][y].type == "special2":
            hero.pk(self.point[x][y])
            self.special2 += 1
            self.point[x][y].active = False
            return False  
        
        elif self.point[x][y].type == "item":
            self.point[x][y].active = False
            if self.point[x][y].itemtype == "yellowkey":
                hero.yellowkey += 1
            elif self.point[x][y].itemtype == "bluekey":
                hero.bluekey += 1
            elif self.point[x][y].itemtype == "redkey":
                hero.redkey += 1
            elif self.point[x][y].itemtype == "redlife":
                hero.life += 50
            elif self.point[x][y].itemtype == "bluelife":
                hero.life += 200
            elif self.point[x][y].itemtype == "redcrystal":
                hero.attack += 1
            elif self.point[x][y].itemtype == "bluecrystal":
                hero.defend += 1
            elif self.point[x][y].itemtype == "sword1":
                hero.attack += 10
            elif self.point[x][y].itemtype == "shield1":
                hero.defend += 10
                
            return False

        elif self.point[x][y].type == "door":
            if self.point[x][y].status == 0:
                if self.point[x][y].doortype == "yellow":
                    if hero.yellowkey > 0:
                        hero.yellowkey -= 1
                        self.point[x][y].open = True
                        
                elif self.point[x][y].doortype == "blue":
                    if hero.bluekey > 0:
                        hero.bluekey -= 1
                        self.point[x][y].open = True

                elif self.point[x][y].doortype == "red":
                    if hero.redkey > 0:
                        hero.redkey -= 1
                        self.point[x][y].open = True
                elif self.point[x][y].doortype == "special":
                    if self.special1 == 2 and hero.floor_num == 8:
                        self.point[x][y].open = True
                    if self.special2 == 8 and hero.floor_num == 10:
                        self.point[x][y].open = True
            return False

        elif self.point[x][y].type == "terrain":
            return False

        elif self.point[x][y].type == "upstair":
            if hero.floor_num == 10:
                print("通关成功！")
            hero.stair = 1
            hero.floor_num += 1
            return False
        
        elif self.point[x][y].type == "downstair":
            hero.stair = 2
            hero.floor_num -= 1
            return False
            
class Floor1(Floor):
    def __init__(self):
        super().__init__()

        #给第一层地图设置墙的坐标
        for i in range(10):
            self.point[i+1][2] = Wall((i+5)*32, 2*32)

        for i in range(8):
            self.point[4][i+4] = Wall(8*32, (i+4)*32)

        for i in range(3):
            self.point[6][i+3] = Wall(10*32, (i+3)*32)
            
        for i in range(2):
            self.point[i+7][5] = Wall((i+11)*32, 5*32)

        for i in range(5):
            self.point[10][i+3] = Wall(14*32, (i+3)*32)

        for i in range(4):
            self.point[i+6][7] = Wall((i+10)*32, 7*32)

        for i in range(3):
            self.point[i+7][9] = Wall((i+11)*32, 9*32)

        for i in range(2):
            self.point[8][i+10] = Wall(12*32, (i+10)*32)

        self.point[1][5] = Wall(5*32, 5*32)
        self.point[3][5] = Wall(7*32, 5*32)
        self.point[1][8] = Wall(5*32, 8*32)
        self.point[3][8] = Wall(7*32, 8*32)
        self.point[5][9] = Wall(9*32, 9*32)
        self.point[11][9] = Wall(15*32, 9*32)

        #给第一层地图设置绿球的坐标
        self.point[3][1] = GreenBall(self, 7*32, 1*32)
        self.point[5][1] = GreenBall(self, 9*32, 1*32)
        self.point[9][11] = GreenBall(self, 13*32, 11*32)
        self.point[11][11] = GreenBall(self, 15*32, 11*32)

        #红球坐标
        self.point[4][1] = RedBall(self, 8*32, 1*32)

        #小蝙蝠坐标
        self.point[7][6] = SmallBat(self, 11*32, 6*32)
        self.point[9][6] = SmallBat(self, 13*32, 6*32)
        self.point[10][10] = SmallBat(self, 14*32, 10*32)

        #小骷髅坐标
        self.point[2][4] = SmallSkeleton(self, 6*32, 4*32)

        #中骷髅坐标
        self.point[2][7] = MidSkeleton(self, 6*32, 7*32)

        #小法师坐标
        self.point[8][6] = SmallMaster(self, 12*32, 6*32)

        #钥匙坐标
        self.point[8][3] = YellowKey(self, 12*32, 3*32)
        self.point[1][6] = YellowKey(self, 5*32, 6*32)
        self.point[3][10] = YellowKey(self, 7*32, 10*32)
        self.point[3][11] = YellowKey(self, 7*32, 11*32)
        self.point[5][10] = YellowKey(self, 9*32, 10*32)

        #血瓶和水晶的坐标
        self.point[1][3] = RedLife(self, 5*32, 3*32)
        self.point[1][10] = RedLife(self, 5*32, 10*32)
        self.point[1][11] = RedLife(self, 5*32, 11*32)
        self.point[8][4] = RedLife(self, 12*32, 4*32)
        self.point[10][11] = BlueLife(self, 14*32, 11*32)

        self.point[2][11] = RedCrystal(self, 6*32, 11*32)
        self.point[7][3] = RedCrystal(self, 11*32, 3*32)
        self.point[7][4] = BlueCrystal(self, 11*32, 4*32)

        #门的坐标
        self.point[6][9] = YellowDoor(self, 10*32, 9*32)
        self.point[2][5] = YellowDoor(self, 6*32, 5*32)
        self.point[2][8] = YellowDoor(self, 6*32, 8*32)
        self.point[4][3] = YellowDoor(self, 8*32, 3*32)
        self.point[6][6] = YellowDoor(self, 10*32, 6*32)
        self.point[9][5] = YellowDoor(self, 13*32, 5*32)
        self.point[10][9] = YellowDoor(self, 14*32, 9*32)

        #楼梯坐标
        self.point[1][1] = Upstair(5*32, 1*32)

    #遍历地图，绘制地图的元素
    def draw(self, screen, index, hero):
        for i in range(13):
            for j in range(13):
                if self.point[i][j] != 0:
                    self.point[i][j].draw(screen, index)

    def set_hero_pos(self, hero):
        if hero.floor_num == 1:
            if hero.stair == 2:
                hero.stair = 0
                hero.rect.left, hero.rect.top = 6*32, 1*32
                
                
                    
class Floor2(Floor):
    def __init__(self):
        super().__init__()

        for i in range(9):
            self.point[2][i+3] = Wall(6*32, (i+3)*32)

        for i in range(2):
            self.point[i+3][2] = Wall((i+7)*32, 2*32)
        for i in range(4):
            self.point[i+3][3] = Wall((i+7)*32, 3*32)
        for i in range(2):
            self.point[i+10][2] = Wall((i+14)*32, 2*32)
        for i in range(4):
            self.point[i+8][3] = Wall((i+12)*32, 3*32)
        for i in range(3):
            self.point[i+3][6] = Wall((i+7)*32, 6*32)
        for i in range(3):
            self.point[i+9][6] = Wall((i+13)*32, 6*32)
        for i in range(3):
            self.point[i+3][9] = Wall((i+7)*32, 9*32)
        for i in range(3):
            self.point[i+9][9] = Wall((i+13)*32, 9*32)

        self.point[5][4] = Wall(9*32, 4*32)
        self.point[9][4] = Wall(13*32, 4*32)
        self.point[5][7] = Wall(9*32, 7*32)
        self.point[9][7] = Wall(13*32, 7*32)
        self.point[5][10] = Wall(9*32, 10*32)
        self.point[9][10] = Wall(13*32, 10*32)

        #怪物坐标
        self.point[6][2] = MidGuard(self, 10*32, 2*32)
        self.point[8][2] = MidGuard(self, 12*32, 2*32)
        self.point[11][4] = GreenBall(self, 15*32, 4*32)
        self.point[11][7] = RedBall(self, 15*32, 7*32)
        self.point[11][10] = BigSkeleton(self, 15*32, 10*32)

        #血瓶和水晶的坐标
        self.point[3][4] = YellowKey(self, 7*32, 4*32)
        self.point[3][5] = YellowKey(self, 7*32, 5*32)
        self.point[4][4] = YellowKey(self, 8*32, 4*32)
        self.point[3][10] = BlueLife(self, 7*32, 10*32)
        self.point[3][11] = BlueLife(self, 7*32, 11*32)
        self.point[4][10] = BlueLife(self, 8*32, 10*32)
        self.point[4][11] = BlueLife(self, 8*32, 11*32)

        self.point[3][8] = RedCrystal(self, 7*32, 8*32)
        self.point[4][8] = RedCrystal(self, 8*32, 8*32)
        self.point[3][7] = BlueCrystal(self, 7*32, 7*32)
        self.point[4][7] = BlueCrystal(self, 8*32, 7*32)

        #门坐标
        self.point[9][5] = YellowDoor(self, 13*32, 5*32)
        self.point[9][8] = YellowDoor(self, 13*32, 8*32)
        self.point[9][11] = YellowDoor(self, 13*32, 11*32)
        self.point[3][1] = BlueDoor(self, 7*32, 1*32)
        self.point[5][5] = BlueDoor(self, 9*32, 5*32)
        self.point[5][8] = BlueDoor(self, 9*32, 8*32)
        self.point[5][11] = BlueDoor(self, 9*32, 11*32)

        #楼梯坐标
        self.point[1][1] = Downstair(5*32, 1*32)
        self.point[1][11] = Upstair(5*32, 11*32)

    #遍历地图，绘制地图的元素
    def draw(self, screen, index, hero):
        for i in range(13):
            for j in range(13):
                if self.point[i][j] != 0:
                    self.point[i][j].draw(screen, index)

    def set_hero_pos(self, hero):
        if hero.floor_num == 2:
            if hero.stair == 1:
                hero.stair = 0
                hero.rect.left, hero.rect.top = 5*32, 2*32
            if hero.stair == 2:
                hero.stair = 0
                hero.rect.left, hero.rect.top = 5*32, 10*32

                    
class Floor3(Floor):
    def __init__(self):
        super().__init__()

        for i in range(3):
            self.point[3][i+1] = Wall(7*32, (i+1)*32)
        for i in range(4):
            self.point[7][i+1] = Wall(11*32, (i+1)*32)
        for i in range(4):
            self.point[3][i+6] = Wall(7*32, (i+6)*32)
        for i in range(6):
            self.point[7][i+6] = Wall(11*32, (i+6)*32)
        for i in range(3):
            self.point[i+2][4] = Wall((i+6)*32, 4*32)
        for i in range(3):
            self.point[i+9][3] = Wall((i+13)*32, 3*32)
        for i in range(3):
            self.point[i+9][6] = Wall((i+13)*32, 6*32)
        for i in range(4):
            self.point[i+1][10] = Wall((i+5)*32, 10*32)
        for i in range(3):
            self.point[i+9][9] = Wall((i+13)*32, 9*32)
            
        self.point[2][4] = Wall(6*32, 4*32)
        self.point[4][4] = Wall(8*32, 4*32)
        self.point[6][4] = Wall(10*32, 4*32)
        self.point[9][1] = Wall(13*32, 1*32)
        self.point[9][4] = Wall(13*32, 4*32)
        self.point[2][6] = Wall(6*32, 6*32)
        self.point[4][7] = Wall(8*32, 7*32)
        self.point[6][7] = Wall(10*32, 7*32)
        self.point[6][10] = Wall(10*32, 10*32)
        self.point[9][7] = Wall(13*32, 7*32)
        self.point[9][10] = Wall(13*32, 10*32)

        #怪物坐标
        self.point[7][5] = GreenBall(self, 11*32, 5*32)
        self.point[8][10] = RedBall(self, 12*32, 10*32)
        self.point[3][5] = SmallBat(self, 7*32, 5*32)
        self.point[10][2] = SmallBat(self, 14*32, 2*32)
        self.point[1][7] = SmallSkeleton(self, 5*32, 7*32)
        self.point[1][3] = SmallMaster(self, 5*32, 3*32)
        self.point[10][8] = SmallMaster(self, 14*32, 8*32)

        #物品坐标
        self.point[1][1] = YellowKey(self, 5*32, 1*32)
        self.point[2][8] = YellowKey(self, 6*32, 8*32)
        self.point[4][1] = YellowKey(self, 8*32, 1*32)
        self.point[4][3] = YellowKey(self, 8*32, 3*32)
        self.point[5][2] = YellowKey(self, 9*32, 2*32)
        self.point[6][1] = YellowKey(self, 10*32, 1*32)
        self.point[6][3] = YellowKey(self, 10*32, 3*32)
        self.point[11][8] = YellowKey(self, 15*32, 8*32)
        self.point[5][3] = BlueKey(self, 9*32, 3*32)
        self.point[2][2] = RedLife(self, 6*32, 2*32)
        self.point[1][9] = RedLife(self, 5*32, 9*32)
        self.point[11][1] = RedLife(self, 15*32, 1*32)
        self.point[11][7] = RedLife(self, 15*32, 7*32)
        self.point[5][1] = BlueLife(self, 9*32, 1*32)
        self.point[4][2] = BlueLife(self, 8*32, 2*32)
        self.point[6][2] = BlueLife(self, 10*32, 2*32)
        self.point[2][9] = RedCrystal(self, 6*32, 9*32)
        self.point[11][4] = RedCrystal(self, 15*32, 4*32)
        self.point[2][1] = BlueCrystal(self, 6*32, 1*32)

        #门的坐标
        self.point[1][4] = YellowDoor(self, 5*32, 4*32)
        self.point[1][6] = YellowDoor(self, 5*32, 6*32)
        self.point[9][2] = YellowDoor(self, 13*32, 2*32)
        self.point[9][8] = YellowDoor(self, 13*32, 8*32)
        self.point[9][11] = YellowDoor(self, 13*32, 11*32)

        #楼梯坐标
        self.point[11][11] = Upstair(15*32, 11*32)
        self.point[1][11] = Downstair(5*32, 11*32)

    #遍历地图，绘制地图的元素
    def draw(self, screen, index, hero):
        for i in range(13):
            for j in range(13):
                if self.point[i][j] != 0:
                    self.point[i][j].draw(screen, index)

    def set_hero_pos(self, hero):
        if hero.floor_num == 3:
            if hero.stair == 1:
                hero.stair = 0
                hero.rect.left, hero.rect.top = 6*32, 11*32
            if hero.stair == 2:
                hero.stair = 0
                hero.rect.left, hero.rect.top = 14*32, 11*32

class Floor4(Floor):
    def __init__(self):
        super().__init__()

        for i in range(3):
            self.point[4][i+1] = Wall(8*32, (i+1)*32)
        for i in range(3):
            self.point[8][i+1] = Wall(12*32, (i+1)*32)
        for i in range(4):
            self.point[2][i+8] = Wall(6*32, (i+8)*32)
        for i in range(3):
            self.point[6][i+9] = Wall(10*32, (i+9)*32)
        for i in range(4):
            self.point[10][i+8] = Wall(14*32, (i+8)*32)
        for i in range(3):
            self.point[i+3][4] = Wall((i+7)*32, 4*32)
        for i in range(3):
            self.point[i+7][4] = Wall((i+11)*32, 4*32)
        for i in range(8):
            self.point[i+4][6] = Wall((i+8)*32, 6*32)
        for i in range(3):
            self.point[i+5][8] = Wall((i+9)*32, 8*32)
            
        self.point[1][4] = Wall(5*32, 4*32)
        self.point[11][4] = Wall(15*32, 4*32)
        self.point[3][8] = Wall(7*32, 8*32)
        self.point[9][8] = Wall(13*32, 8*32)

        #怪物坐标
        self.point[3][7] = GreenBall(self, 7*32, 7*32)
        self.point[3][10] = GreenBall(self, 7*32, 10*32)
        self.point[4][11] = GreenBall(self, 8*32, 11*32)
        self.point[8][11] = GreenBall(self, 12*32, 11*32)
        self.point[1][7] = RedBall(self, 5*32, 7*32)
        self.point[6][5] = RedBall(self, 10*32, 5*32)
        self.point[4][9] = SmallBat(self, 8*32, 9*32)
        self.point[9][5] = SmallSkeleton(self, 13*32, 5*32)
        self.point[2][5] = SmallMaster(self, 6*32, 5*32)
        self.point[8][9] = SmallMaster(self, 12*32, 9*32)
        self.point[10][3] = MidSkeleton(self, 14*32, 3*32)

        #物品坐标
        self.point[3][2] = YellowKey(self, 7*32, 2*32)
        self.point[9][2] = YellowKey(self, 13*32, 2*32)
        self.point[3][11] = YellowKey(self, 7*32, 11*32)
        self.point[5][10] = YellowKey(self, 9*32, 10*32)
        self.point[5][11] = YellowKey(self, 9*32, 11*32)
        self.point[2][1] = BlueKey(self, 6*32, 1*32)
        self.point[1][2] = RedLife(self, 5*32, 2*32)
        self.point[9][10] = RedLife(self, 13*32, 10*32)
        self.point[11][1] = BlueLife(self, 15*32, 2*32)
        self.point[7][10] = RedCrystal(self, 11*32, 10*32)
        self.point[10][1] = RedCrystal(self, 14*32, 1*32)
        self.point[5][3] = RedCrystal(self, 9*32, 3*32)
        self.point[6][3] = RedCrystal(self, 10*32, 3*32)
        self.point[7][3] = RedCrystal(self, 11*32, 3*32)
        self.point[5][2] = BlueCrystal(self, 9*32, 2*32)
        self.point[6][2] = BlueCrystal(self, 10*32, 2*32)
        self.point[7][2] = BlueCrystal(self, 11*32, 2*32)

        #门的坐标
        self.point[1][8] = YellowDoor(self, 5*32, 8*32)
        self.point[2][4] = YellowDoor(self, 6*32, 4*32)
        self.point[4][5] = YellowDoor(self, 8*32, 5*32)
        self.point[4][8] = YellowDoor(self, 8*32, 8*32)
        self.point[8][8] = YellowDoor(self, 12*32, 8*32)
        self.point[10][4] = YellowDoor(self, 14*32, 4*32)
        self.point[11][8] = YellowDoor(self, 15*32, 8*32)
        self.point[6][4] = BlueDoor(self, 10*32, 4*32)

        #楼梯坐标
        self.point[11][11] = Downstair(15*32, 11*32)
        self.point[1][11] = Upstair(5*32, 11*32)

    #遍历地图，绘制地图的元素
    def draw(self, screen, index, hero):
        for i in range(13):
            for j in range(13):
                if self.point[i][j] != 0:
                    self.point[i][j].draw(screen, index)

    def set_hero_pos(self, hero):
        if hero.floor_num == 4:
            if hero.stair == 1:
                hero.stair = 0
                hero.rect.left, hero.rect.top = 15*32, 10*32
            if hero.stair == 2:
                hero.stair = 0
                hero.rect.left, hero.rect.top = 5*32, 10*32

class Floor5(Floor):
    def __init__(self):
        super().__init__()

        for i in range(2):
            self.point[2][i+1] = Wall(6*32, (i+1)*32)
        for i in range(9):
            self.point[5][i+2] = Wall(9*32, (i+2)*32)
        for i in range(5):
            self.point[7][i+1] = Wall(11*32, (i+1)*32)
        for i in range(5):
            self.point[7][i+7] = Wall(11*32, (i+7)*32)
        for i in range(4):
            self.point[10][i+2] = Wall(14*32, (i+2)*32)
        for i in range(2):
            self.point[i+1][4] = Wall((i+5)*32, 4*32)
        for i in range(2):
            self.point[i+3][7] = Wall((i+7)*32, 7*32)
        for i in range(2):
            self.point[i+8][5] = Wall((i+12)*32, 5*32)
        for i in range(4):
            self.point[i+1][10] = Wall((i+5)*32, 10*32)
        for i in range(3):
            self.point[i+8][7] = Wall((i+12)*32, 7*32)
        for i in range(3):
            self.point[i+9][9] = Wall((i+13)*32, 9*32)
            
        self.point[1][7] = Wall(5*32, 7*32)
        self.point[4][4] = Wall(8*32, 4*32)
        self.point[9][10] = Wall(13*32, 10*32)

        #怪物坐标
        self.point[6][8] = GreenBall(self, 10*32, 8*32)
        self.point[7][6] = GreenBall(self, 11*32, 6*32)
        self.point[8][2] = GreenBall(self, 12*32, 2*32)
        self.point[9][2] = GreenBall(self, 13*32, 2*32)
        self.point[4][1] = RedBall(self, 8*32, 1*32)
        self.point[11][2] = RedBall(self, 15*32, 2*32)
        self.point[11][7] = RedBall(self, 15*32, 7*32)
        self.point[4][6] = SmallBat(self, 8*32, 6*32)
        self.point[3][3] = SmallBat(self, 7*32, 3*32)
        self.point[6][4] = SmallBat(self, 10*32, 4*32)
        self.point[3][5] = SmallMaster(self, 7*32, 5*32)
        self.point[2][7] = MidSkeleton(self, 6*32, 7*32)

        #物品坐标
        self.point[1][5] = YellowKey(self, 5*32, 5*32)
        self.point[1][6] = YellowKey(self, 5*32, 6*32)
        self.point[6][2] = YellowKey(self, 10*32, 2*32)
        self.point[8][3] = YellowKey(self, 12*32, 3*32)
        self.point[8][4] = YellowKey(self, 12*32, 4*32)
        self.point[9][3] = YellowKey(self, 13*32, 3*32)
        self.point[9][4] = YellowKey(self, 13*32, 4*32)
        self.point[3][9] = RedLife(self, 7*32, 9*32)
        self.point[4][9] = RedCrystal(self, 8*32, 9*32)
        self.point[1][9] = BlueCrystal(self, 5*32, 9*32)
        self.point[11][11] = Sword1(self, 15*32, 11*32)

        #门的坐标
        self.point[2][3] = YellowDoor(self, 6*32, 3*32)
        self.point[3][4] = YellowDoor(self, 7*32, 4*32)
        self.point[5][1] = YellowDoor(self, 9*32, 1*32)
        self.point[8][9] = YellowDoor(self, 12*32, 9*32)
        self.point[10][1] = YellowDoor(self, 14*32, 1*32)
        self.point[9][11] = YellowDoor(self, 13*32, 11*32)

        #楼梯坐标
        self.point[1][1] = Upstair(5*32, 1*32)
        self.point[1][11] = Downstair(5*32, 11*32)

    #遍历地图，绘制地图的元素
    def draw(self, screen, index, hero):
        for i in range(13):
            for j in range(13):
                if self.point[i][j] != 0:
                    self.point[i][j].draw(screen, index)

    def set_hero_pos(self, hero):
        if hero.floor_num == 5:
            if hero.stair == 1:
                hero.stair = 0
                hero.rect.left, hero.rect.top = 6*32, 11*32
            if hero.stair == 2:
                hero.stair = 0
                hero.rect.left, hero.rect.top = 5*32, 3*32

class Floor6(Floor):
    def __init__(self):
        super().__init__()

        for i in range(3):
            self.point[2][i+1] = Wall(6*32, (i+1)*32)
        for i in range(3):
            self.point[5][i+1] = Wall(9*32, (i+1)*32)
        for i in range(4):
            self.point[5][i+7] = Wall(9*32, (i+7)*32)
        for i in range(4):
            self.point[7][i+2] = Wall(11*32, (i+2)*32)
        for i in range(3):
            self.point[7][i+9] = Wall(11*32, (i+9)*32)
        for i in range(3):
            self.point[10][i+9] = Wall(14*32, (i+9)*32)
        for i in range(3):
            self.point[i+8][2] = Wall((i+12)*32, 2*32)
        for i in range(4):
            self.point[i+8][5] = Wall((i+12)*32, 5*32)
        for i in range(4):
            self.point[i+2][5] = Wall((i+6)*32, 5*32)
        for i in range(4):
            self.point[i+1][7] = Wall((i+5)*32, 7*32)
        for i in range(4):
            self.point[i+7][7] = Wall((i+11)*32, 7*32)
        for i in range(3):
            self.point[i+2][10] = Wall((i+6)*32, 10*32)
            
        self.point[3][3] = Wall(7*32, 3*32)
        self.point[8][9] = Wall(12*32, 9*32)

        #怪物坐标
        self.point[10][1] = GreenBall(self, 14*32, 1*32)
        self.point[2][11] = GreenBall(self, 6*32, 11*32)
        self.point[4][3] = RedBall(self, 8*32, 3*32)
        self.point[3][6] = RedBall(self, 7*32, 6*32)
        self.point[9][9] = RedBall(self, 13*32, 9*32)
        self.point[11][9] = RedBall(self, 15*32, 9*32)
        self.point[2][9] = SmallBat(self, 6*32, 9*32)
        self.point[11][4] = SmallBat(self, 15*32, 4*32)
        self.point[1][8] = SmallMaster(self, 5*32, 8*32)
        self.point[4][6] = SmallMaster(self, 8*32, 6*32)
        self.point[7][1] = SmallMaster(self, 11*32, 1*32)
        self.point[5][11] = SmallSkeleton(self, 9*32, 11*32)
        self.point[8][6] = SmallSkeleton(self, 12*32, 6*32)
        self.point[9][6] = MidSkeleton(self, 13*32, 6*32)

        #物品坐标
        self.point[3][1] = YellowKey(self, 7*32, 1*32)
        self.point[3][2] = YellowKey(self, 7*32, 2*32)
        self.point[4][1] = YellowKey(self, 8*32, 1*32)
        self.point[4][2] = YellowKey(self, 8*32, 2*32)
        self.point[6][6] = YellowKey(self, 10*32, 6*32)
        self.point[9][1] = YellowKey(self, 13*32, 1*32)
        self.point[8][3] = RedLife(self, 12*32, 3*32)
        self.point[8][11] = RedLife(self, 12*32, 11*32)
        self.point[9][11] = RedLife(self, 13*32, 11*32)
        self.point[8][4] = RedCrystal(self, 12*32, 4*32)
        self.point[4][8] = BlueCrystal(self, 8*32, 8*32)
        self.point[4][9] = BlueCrystal(self, 8*32, 9*32)

        #门的坐标
        self.point[2][4] = YellowDoor(self, 6*32, 4*32)
        self.point[3][4] = YellowDoor(self, 7*32, 4*32)
        self.point[5][4] = YellowDoor(self, 9*32, 4*32)
        self.point[11][2] = YellowDoor(self, 15*32, 2*32)
        self.point[1][10] = YellowDoor(self, 5*32, 10*32)
        self.point[7][8] = YellowDoor(self, 11*32, 8*32)
        self.point[8][8] = YellowDoor(self, 12*32, 8*32)
        self.point[10][8] = YellowDoor(self, 14*32, 8*32)

        #楼梯坐标
        self.point[1][1] = Downstair(5*32, 1*32)
        self.point[11][11] = Upstair(15*32, 11*32)

    #遍历地图，绘制地图的元素
    def draw(self, screen, index, hero):
        for i in range(13):
            for j in range(13):
                if self.point[i][j] != 0:
                    self.point[i][j].draw(screen, index)

    def set_hero_pos(self, hero):
        if hero.floor_num == 6:
            if hero.stair == 1:
                hero.stair = 0
                hero.rect.left, hero.rect.top = 5*32, 3*32
            if hero.stair == 2:
                hero.stair = 0
                hero.rect.left, hero.rect.top = 15*32, 9*32

class Floor7(Floor):
    def __init__(self):
        super().__init__()

        for i in range(5):
            self.point[2][i+1] = Wall(6*32, (i+1)*32)
        for i in range(4):
            self.point[2][i+7] = Wall(6*32, (i+7)*32)
        for i in range(5):
            self.point[4][i+1] = Wall(8*32, (i+1)*32)
        for i in range(5):
            self.point[4][i+7] = Wall(8*32, (i+7)*32)
        for i in range(3):
            self.point[6][i+3] = Wall(10*32, (i+3)*32)
        for i in range(5):
            self.point[6][i+7] = Wall(10*32, (i+7)*32)
        for i in range(5):
            self.point[8][i+1] = Wall(12*32, (i+1)*32)
        for i in range(5):
            self.point[8][i+7] = Wall(12*32, (i+7)*32)
        for i in range(5):
            self.point[10][i+1] = Wall(14*32, (i+1)*32)
        for i in range(5):
            self.point[10][i+7] = Wall(14*32, (i+7)*32)

        #怪物坐标
        self.point[1][10] = GreenBall(self, 5*32, 10*32)
        self.point[3][10] = GreenBall(self, 7*32, 10*32)
        self.point[11][1] = GreenBall(self, 15*32, 1*32)
        self.point[11][3] = GreenBall(self, 15*32, 3*32)
        self.point[2][11] = RedBall(self, 6*32, 11*32)
        self.point[5][3] = RedBall(self, 9*32, 3*32)
        self.point[7][9] = RedBall(self, 11*32, 9*32)
        self.point[11][2] = RedBall(self, 15*32, 2*32)
        self.point[3][3] = SmallBat(self, 7*32, 3*32)
        self.point[5][9] = SmallBat(self, 9*32, 9*32)
        self.point[4][6] = SmallMaster(self, 8*32, 6*32)
        self.point[7][10] = SmallMaster(self, 11*32, 10*32)
        self.point[9][5] = SmallSkeleton(self, 13*32, 5*32)
        self.point[2][6] = MidSkeleton(self, 6*32, 6*32)
        self.point[7][3] = MidSkeleton(self, 11*32, 3*32)
        self.point[9][7] = MidSkeleton(self, 13*32, 7*32)

        #物品坐标
        self.point[5][10] = YellowKey(self, 9*32, 10*32)
        self.point[5][11] = YellowKey(self, 9*32, 11*32)
        self.point[9][1] = YellowKey(self, 13*32, 1*32)
        self.point[9][2] = YellowKey(self, 13*32, 2*32)
        self.point[9][10] = YellowKey(self, 13*32, 10*32)
        self.point[9][11] = YellowKey(self, 13*32, 11*32)
        self.point[3][2] = RedLife(self, 7*32, 2*32)
        self.point[9][3] = RedLife(self, 13*32, 3*32)
        self.point[7][11] = BlueLife(self, 11*32, 11*32)
        self.point[9][9] = BlueLife(self, 13*32, 9*32)
        self.point[3][1] = RedCrystal(self, 7*32, 1*32)
        self.point[7][1] = RedCrystal(self, 11*32, 1*32)
        self.point[5][1] = BlueCrystal(self, 9*32, 1*32)

        #门的坐标
        self.point[1][5] = YellowDoor(self, 5*32, 5*32)
        self.point[1][7] = YellowDoor(self, 5*32, 7*32)
        self.point[3][5] = YellowDoor(self, 7*32, 5*32)
        self.point[3][7] = YellowDoor(self, 7*32, 7*32)
        self.point[5][7] = YellowDoor(self, 9*32, 7*32)
        self.point[7][5] = YellowDoor(self, 11*32, 5*32)
        self.point[7][7] = YellowDoor(self, 11*32, 7*32)
        self.point[11][5] = YellowDoor(self, 15*32, 5*32)
        self.point[11][7] = YellowDoor(self, 15*32, 7*32)
        self.point[5][5] = BlueDoor(self, 9*32, 5*32)

        #楼梯坐标
        self.point[1][1] = Upstair(5*32, 1*32)
        self.point[11][11] = Downstair(15*32, 11*32)

    #遍历地图，绘制地图的元素
    def draw(self, screen, index, hero):
        for i in range(13):
            for j in range(13):
                if self.point[i][j] != 0:
                    self.point[i][j].draw(screen, index)

    def set_hero_pos(self, hero):
        if hero.floor_num == 7:
            if hero.stair == 1:
                hero.stair = 0
                hero.rect.left, hero.rect.top = 15*32, 9*32
            if hero.stair == 2:
                hero.stair = 0
                hero.rect.left, hero.rect.top = 5*32, 2*32

class Floor8(Floor):
    def __init__(self):
        super().__init__()

        for i in range(3):
            self.point[2][i+3] = Wall(6*32, (i+3)*32)
        for i in range(3):
            self.point[6][i+5] = Wall(10*32, (i+5)*32)
        for i in range(2):
            self.point[6][i+10] = Wall(10*32, (i+10)*32)
        for i in range(7):
            self.point[8][i+1] = Wall(12*32, (i+1)*32)
        for i in range(2):
            self.point[i+3][2] = Wall((i+7)*32, 2*32)
        for i in range(3):
            self.point[i+3][3] = Wall((i+7)*32, 3*32)
        for i in range(3):
            self.point[i+3][5] = Wall((i+7)*32, 5*32)
        for i in range(4):
            self.point[i+1][7] = Wall((i+5)*32, 7*32)
        for i in range(9):
            self.point[i+2][9] = Wall((i+6)*32, 9*32)
            
        self.point[7][3] = Wall(11*32, 3*32)
        self.point[9][4] = Wall(13*32, 4*32)
        self.point[9][7] = Wall(13*32, 7*32)
        self.point[11][4] = Wall(15*32, 4*32)
        self.point[11][7] = Wall(15*32, 7*32)
        self.point[3][10] = Wall(7*32, 10*32)
        self.point[9][10] = Wall(13*32, 10*32)

        #怪物坐标
        self.point[1][10] = GreenBall(self, 5*32, 10*32)
        self.point[3][6] = GreenBall(self, 7*32, 6*32)
        self.point[7][2] = GreenBall(self, 11*32, 2*32)
        self.point[2][6] = RedBall(self, 6*32, 6*32)
        self.point[4][6] = RedBall(self, 8*32, 6*32)
        self.point[2][11] = SmallBat(self, 6*32, 11*32)
        self.point[4][8] = SmallBat(self, 8*32, 8*32)
        self.point[7][7] = SmallBat(self, 11*32, 7*32)
        self.point[7][5] = SmallMaster(self, 11*32, 5*32)
        self.point[8][8] = SmallMaster(self, 12*32, 8*32)
        self.point[6][8] = SmallSkeleton(self, 10*32, 8*32)
        self.point[11][10] = SmallSkeleton(self, 15*32, 10*32)
        self.point[9][5] = SmallGuard(self, 13*32, 5*32)
        self.point[11][5] = SmallGuard(self, 15*32, 5*32)

        #物品坐标
        self.point[3][4] = YellowKey(self, 7*32, 4*32)
        self.point[4][4] = YellowKey(self, 8*32, 4*32)
        self.point[5][4] = YellowKey(self, 9*32, 4*32)
        self.point[4][11] = YellowKey(self, 8*32, 11*32)
        self.point[5][10] = YellowKey(self, 9*32, 10*32)
        self.point[7][11] = YellowKey(self, 11*32, 11*32)
        self.point[9][1] = YellowKey(self, 13*32, 1*32)
        self.point[11][1] = YellowKey(self, 15*32, 1*32)
        self.point[10][2] = RedKey(self, 14*32, 2*32)
        self.point[7][10] = BlueKey(self, 11*32, 10*32)
        self.point[1][5] = RedLife(self, 5*32, 5*32)
        self.point[11][3] = RedLife(self, 15*32, 3*32)
        self.point[8][10] = RedLife(self, 12*32, 10*32)
        self.point[4][10] = RedCrystal(self, 8*32, 10*32)
        self.point[5][11] = BlueCrystal(self, 9*32, 11*32)
        self.point[10][11] = MidSkeleton(self, 14*32, 11*32)

        #门的坐标
        self.point[1][3] = YellowDoor(self, 5*32, 3*32)
        self.point[1][9] = YellowDoor(self, 5*32, 9*32)
        self.point[3][1] = YellowDoor(self, 7*32, 1*32)
        self.point[4][1] = YellowDoor(self, 8*32, 1*32)
        self.point[5][7] = YellowDoor(self, 9*32, 7*32)
        self.point[6][3] = YellowDoor(self, 10*32, 3*32)
        self.point[10][7] = YellowDoor(self, 14*32, 7*32)
        self.point[9][11] = YellowDoor(self, 13*32, 11*32)
        self.point[11][9] = YellowDoor(self, 15*32, 9*32)
        self.point[3][11] = BlueDoor(self, 7*32, 11*32)
        self.point[10][4] = SpecialDoor(self, 14*32, 4*32)

        #楼梯坐标
        self.point[1][1] = Downstair(5*32, 1*32)
        self.point[6][1] = Upstair(10*32, 1*32)

    #遍历地图，绘制地图的元素
    def draw(self, screen, index, hero):
        for i in range(13):
            for j in range(13):
                if self.point[i][j] != 0:
                    self.point[i][j].draw(screen, index)

    def set_hero_pos(self, hero):
        if hero.floor_num == 8:
            if hero.stair == 1:
                hero.stair = 0
                hero.rect.left, hero.rect.top = 6*32, 1*32
            if hero.stair == 2:
                hero.stair = 0
                hero.rect.left, hero.rect.top = 9*32, 1*32

class Floor9(Floor):
    def __init__(self):
        super().__init__()

        for i in range(3):
            self.point[3][i+8] = Wall(7*32, (i+8)*32)
        for i in range(5):
            self.point[6][i+6] = Wall(10*32, (i+6)*32)
        for i in range(6):
            self.point[8][i+5] = Wall(12*32, (i+5)*32)
        for i in range(2):
            self.point[10][i+7] = Wall(14*32, (i+7)*32)
        for i in range(4):
            self.point[i+2][3] = Wall((i+6)*32, 3*32)
        for i in range(4):
            self.point[i+7][3] = Wall((i+11)*32, 3*32)
        for i in range(6):
            self.point[i+1][6] = Wall((i+5)*32, 6*32)
        for i in range(2):
            self.point[i+9][8] = Wall((i+13)*32, 8*32)
            
        self.point[4][2] = Wall(8*32, 2*32)
        self.point[4][4] = Wall(8*32, 4*32)
        self.point[8][2] = Wall(12*32, 2*32)
        self.point[9][5] = Wall(13*32, 5*32)
        self.point[11][5] = Wall(15*32, 5*32)
        self.point[10][7] = Wall(14*32, 7*32)
        self.point[2][9] = Wall(6*32, 9*32)
        self.point[4][9] = Wall(8*32, 9*32)

        #怪物坐标
        self.point[9][1] = GreenBall(self, 13*32, 1*32)
        self.point[10][2] = GreenBall(self, 14*32, 2*32)
        self.point[7][6] = RedBall(self, 11*32, 6*32)
        self.point[3][5] = SmallBat(self, 7*32, 5*32)
        self.point[7][10] = SmallBat(self, 11*32, 10*32)
        self.point[9][11] = SmallMaster(self, 13*32, 11*32)
        self.point[11][9] = SmallMaster(self, 15*32, 9*32)
        self.point[5][10] = SmallSkeleton(self, 9*32, 10*32)
        self.point[3][1] = SmallSkeleton(self, 7*32, 1*32)
        self.point[10][10] = SmallSkeleton(self, 14*32, 10*32)
        self.point[1][3] = MidSkeleton(self, 5*32, 3*32)
        self.point[1][8] = MidSkeleton(self, 5*32, 8*32)
        self.point[4][7] = MidSkeleton(self, 8*32, 7*32)
        self.point[11][6] = MidSkeleton(self, 15*32, 6*32)


        #物品坐标
        self.point[2][2] = YellowKey(self, 6*32, 2*32)
        self.point[2][4] = YellowKey(self, 6*32, 4*32)
        self.point[1][7] = YellowKey(self, 5*32, 7*32)
        self.point[5][4] = YellowKey(self, 9*32, 4*32)
        self.point[5][7] = YellowKey(self, 9*32, 7*32)
        self.point[7][4] = YellowKey(self, 11*32, 4*32)
        self.point[9][9] = YellowKey(self, 13*32, 9*32)
        self.point[11][1] = RedLife(self, 15*32, 1*32)
        self.point[2][10] = RedLife(self, 6*32, 10*32)
        self.point[11][11] = RedLife(self, 15*32, 11*32)
        self.point[6][5] = RedCrystal(self, 10*32, 5*32)
        self.point[11][4] = RedCrystal(self, 15*32, 4*32)
        self.point[1][5] = BlueCrystal(self, 5*32, 5*32)
        self.point[9][7] = BlueCrystal(self, 13*32, 7*32)

        #门的坐标
        self.point[1][9] = YellowDoor(self, 5*32, 9*32)
        self.point[3][7] = YellowDoor(self, 7*32, 7*32)
        self.point[4][1] = YellowDoor(self, 8*32, 1*32)
        self.point[4][5] = YellowDoor(self, 8*32, 5*32)
        self.point[5][9] = YellowDoor(self, 9*32, 9*32)
        self.point[6][11] = YellowDoor(self, 10*32, 11*32)
        self.point[8][1] = YellowDoor(self, 12*32, 1*32)
        self.point[8][4] = YellowDoor(self, 12*32, 4*32)
        self.point[8][11] = YellowDoor(self, 12*32, 11*32)
        self.point[9][4] = YellowDoor(self, 13*32, 4*32)
        self.point[11][8] = YellowDoor(self, 15*32, 8*32)
        self.point[10][5] = YellowDoor(self, 14*32, 5*32)
        self.point[6][3] = BlueDoor(self, 10*32, 3*32)
        self.point[3][11] = BlueDoor(self, 7*32, 11*32)

        #楼梯坐标
        self.point[1][11] = Upstair(5*32, 11*32)
        self.point[6][1] = Downstair(10*32, 1*32)

    #遍历地图，绘制地图的元素
    def draw(self, screen, index, hero):
        for i in range(13):
            for j in range(13):
                if self.point[i][j] != 0:
                    self.point[i][j].draw(screen, index)

    def set_hero_pos(self, hero):
        if hero.floor_num == 9:
            if hero.stair == 1:
                hero.stair = 0
                hero.rect.left, hero.rect.top = 9*32, 1*32
            if hero.stair == 2:
                hero.stair = 0
                hero.rect.left, hero.rect.top = 6*32, 11*32

class Floor10(Floor):
    def __init__(self):
        super().__init__()

        for i in range(3):
            self.point[2][i+9] = Wall(6*32, (i+9)*32)
        for i in range(6):
            self.point[4][i+5] = Wall(8*32, (i+5)*32)
        for i in range(3):
            self.point[5][i+7] = Wall(9*32, (i+7)*32)
        for i in range(3):
            self.point[7][i+7] = Wall(11*32, (i+7)*32)
        for i in range(6):
            self.point[8][i+5] = Wall(12*32, (i+5)*32)
        for i in range(3):
            self.point[10][i+9] = Wall(14*32, (i+9)*32)
        for i in range(4):
            self.point[i+1][2] = Wall((i+5)*32, 2*32)
        for i in range(2):
            self.point[i+4][3] = Wall((i+8)*32, 3*32)
        for i in range(4):
            self.point[i+8][2] = Wall((i+12)*32, 2*32)
        for i in range(2):
            self.point[i+7][3] = Wall((i+11)*32, 3*32)
        for i in range(4):
            self.point[i+1][5] = Wall((i+5)*32, 5*32)
        for i in range(4):
            self.point[i+8][5] = Wall((i+12)*32, 5*32)

        #怪物坐标
        self.point[4][11] = SmallMaster(self, 8*32, 11*32)
        self.point[8][11] = SmallMaster(self, 12*32, 11*32)
        self.point[1][6] = SmallSkeleton(self, 5*32, 6*32)
        self.point[3][6] = SmallSkeleton(self, 7*32, 6*32)
        self.point[9][6] = SmallSkeleton(self, 13*32, 6*32)
        self.point[11][6] = SmallSkeleton(self, 15*32, 6*32)
        self.point[2][7] = MidSkeleton(self, 6*32, 7*32)
        self.point[10][7] = MidSkeleton(self, 14*32, 7*32)
        self.point[1][3] = MidSkeleton(self, 5*32, 3*32)
        self.point[2][3] = MidSkeleton(self, 6*32, 3*32)
        self.point[3][3] = MidSkeleton(self, 7*32, 3*32)
        self.point[2][4] = MidSkeleton(self, 6*32, 4*32)
        self.point[9][3] = MidSkeleton(self, 13*32, 3*32)
        self.point[10][3] = MidSkeleton(self, 14*32, 3*32)
        self.point[10][4] = MidSkeleton(self, 14*32, 4*32)
        self.point[11][3] = MidSkeleton(self, 15*32, 3*32)
        self.point[6][4] = BigSkeleton(self, 10*32, 4*32)

        #物品坐标
        self.point[11][11] = BlueLife(self, 15*32, 11*32)
        self.point[10][6] = RedCrystal(self, 14*32, 6*32)
        self.point[2][6] = BlueCrystal(self, 6*32, 6*32)

        #门的坐标
        self.point[1][9] = YellowDoor(self, 5*32, 9*32)
        self.point[3][9] = YellowDoor(self, 7*32, 9*32)
        self.point[9][9] = YellowDoor(self, 13*32, 9*32)
        self.point[11][9] = YellowDoor(self, 15*32, 9*32)
        self.point[6][9] = RedDoor(self, 10*32, 9*32)
        self.point[4][4] = SpecialDoor(self, 8*32, 4*32)
        self.point[8][4] = SpecialDoor(self, 12*32, 4*32)

        #楼梯坐标
        self.point[1][11] = Downstair(5*32, 11*32)
        self.point[6][1] = Upstair(10*32, 1*32)

    #遍历地图，绘制地图的元素
    def draw(self, screen, index, hero):
        for i in range(13):
            for j in range(13):
                if self.point[i][j] != 0:
                    self.point[i][j].draw(screen, index)

    def set_hero_pos(self, hero):
        if hero.floor_num == 10:
            if hero.stair == 1:
                hero.stair = 0
                hero.rect.left, hero.rect.top = 5*32, 10*32
            if hero.stair == 2:
                hero.stair = 0
                hero.rect.left, hero.rect.top = 6*32, 2*32


