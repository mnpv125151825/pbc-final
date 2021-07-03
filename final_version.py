import pygame.freetype
import sys
import pygame
import random
import math
from pygame.locals import *
from sys import exit

# 初始化
pygame.init()
# 建立 window 視窗畫布，大小為 800x600
screen = pygame.display.set_mode((800, 600))
# 設置視窗標題
pygame.display.set_caption('抓到哩丟災')
# 清除畫面並填滿背景色
screen.fill((255, 255, 255))

# 遊戲開始畫面
background = pygame.image.load('background1.png').convert_alpha()
background = pygame.transform.scale(background, (800, 600))
screen.blit(background, (0, 0))  # 對齊的座標
beginPolice = pygame.image.load('begin.png').convert_alpha()
beginPolice = pygame.transform.scale(beginPolice, (350, 350))
screen.blit(beginPolice, (0, 50))  # 對齊的座標

# 宣告 font 文字物件
word = pygame.font.Font('NotoSansMonoCJKtc-Bold.otf', 60)
# 渲染方法會回傳 surface 物件
text_surface = word.render('抓到哩丟災', True, (250, 155, 0))
# blit 用來把其他元素渲染到另外一個 surface 上，這邊是 window 視窗
screen.blit(text_surface, (400, 200))

# 背景音樂
pygame.mixer.init()
pygame.mixer.music.load('BGM.mp3')
pygame.mixer.music.set_volume(0.7)  # 設音量
pygame.mixer.music.play(-1)



# 宣告按鈕
class Button(object):
    def __init__(self, upimage, downimage, position):
        self.imageUp = pygame.image.load(upimage).convert_alpha()
        self.imageUp = pygame.transform.scale(self.imageUp, (250, 100))
        self.imageDown = pygame.image.load(downimage).convert_alpha()
        self.imageDown = pygame.transform.scale(self.imageDown, (250, 100))
        self.position = position

    def isOver(self):  # 若按鈕位置重疊 兩個按鈕都會計算
        point_x, point_y = pygame.mouse.get_pos()
        x, y = self.position
        w, h = self.imageUp.get_size()

        in_x = x - w / 2 < point_x < x + w / 2
        in_y = y - h / 2 < point_y < y + h / 2
        return in_x and in_y

    def render(self):  # 畫
        w, h = self.imageUp.get_size()
        x, y = self.position

        if self.isOver():
            screen.blit(self.imageDown, (x - w / 2, y - h / 2))
        else:
            screen.blit(self.imageUp, (x - w / 2, y - h / 2))


# 退出本關的按鈕
class Button_exit(object):
    def __init__(self, upimage, downimage, position):
        self.imageUp = pygame.image.load(upimage).convert_alpha()
        self.imageUp = pygame.transform.scale(self.imageUp, (60, 60))
        self.imageDown = pygame.image.load(downimage).convert_alpha()
        self.imageDown = pygame.transform.scale(self.imageDown, (60, 60))
        self.position = position

    def isOver(self):  # 若按鈕位置重疊 兩個按鈕都會計算
        point_x, point_y = pygame.mouse.get_pos()
        x, y = self.position
        w, h = self.imageUp.get_size()

        in_x = x - w / 2 < point_x < x + w / 2
        in_y = y - h / 2 < point_y < y + h / 2
        return in_x and in_y

    def render(self):  # 畫
        w, h = self.imageUp.get_size()
        x, y = self.position

        if self.isOver():
            screen.blit(self.imageDown, (x - w / 2, y - h / 2))
        else:
            screen.blit(self.imageUp, (x - w / 2, y - h / 2))

# start按鈕
upImageFilename = 'start.png'
downImageFilename = 'start1.png'
button1 = Button(upImageFilename, downImageFilename, (500, 500))

# 更新畫面，等所有操作完成後一次更新（若沒更新，則元素不會出現）
pygame.display.update()


# 遊戲說明頁面
def Instruction():
    word = pygame.font.Font("NotoSansMonoCJKtc-Bold.otf", 50)
    text = word.render("遊戲說明:", True, (0, 0, 70))
    screen.blit(text, (20, 10))
    word1 = pygame.font.Font("NotoSansMonoCJKtc-Bold.otf", 30)
    text1 = word1.render("以鍵盤空白鍵控制手銬去抓犯人，↑鍵控制丟炸彈，", True, (0, 0, 70))
    screen.blit(text1, (20, 90))
    text2 = word1.render("抓到不同的犯人可以得到不同的業績，", True, (0, 0, 70))
    screen.blit(text2, (20, 135))
    text3 = word1.render("若沒在時間限制內超過目標業績則失敗。", True, (0, 0, 70))
    screen.blit(text3, (20, 180))
    text4 = word1.render("每次通關後可在商店購買道具，使下一關更順利，", True, (0, 0, 70))
    screen.blit(text4, (20, 225))
    text5 = word1.render("也可以投注業績進行下注，每位偵探有不同的破案機率。", True, (0, 0, 70))
    screen.blit(text5, (20, 270))
    text6 = word1.render("若偵探成功破案即可直接通關。", True, (0, 0, 70))
    screen.blit(text6, (20, 315))


def Instruction1():
    word = pygame.font.Font("NotoSansMonoCJKtc-Bold.otf", 50)
    text = word.render("計分方式:", True, (0, 0, 70))
    screen.blit(text, (20, 10))
    word1 = pygame.font.Font("NotoSansMonoCJKtc-Bold.otf", 25)
    text7 = word1.render("每關共30秒，夾到物品時把字打完才能獲得業績，並扣除相對時間", True, (0, 0, 70))
    screen.blit(text7, (20, 80))
    image_k = pygame.image.load('killer.png').convert_alpha()
    image_k = pygame.transform.scale(image_k, (30, 45))
    screen.blit(image_k, (20, 130))
    text1 = word1.render("殺人犯: 業績加 500，花費 4 秒", True, (0, 0, 70))
    screen.blit(text1, (80, 130))
    image_b = pygame.image.load('bad.png').convert_alpha()
    image_b = pygame.transform.scale(image_b, (30, 45))
    screen.blit(image_b, (20, 180))
    text2 = word1.render("壞蛋:   業績加 250，花費 3 秒", True, (0, 0, 70))
    screen.blit(text2, (80, 180))
    image_sc = pygame.image.load('scammer.png').convert_alpha()
    image_sc = pygame.transform.scale(image_sc, (40, 40))
    screen.blit(image_sc, (20, 230))
    text3 = word1.render("詐欺犯: 業績加 100，花費 2 秒", True, (0, 0, 70))
    screen.blit(text3, (80, 230))
    image_st = pygame.image.load('stealer.png').convert_alpha()
    image_st = pygame.transform.scale(image_st, (30, 45))
    screen.blit(image_st, (20, 280))
    text4 = word1.render("竊賊:   業績加 50，花費 1 秒", True, (0, 0, 70))
    screen.blit(text4, (80, 280))
    image_tr = pygame.image.load('triangle.png').convert_alpha()
    image_tr = pygame.transform.scale(image_tr, (30, 45))
    screen.blit(image_tr, (20, 330))
    text5 = word1.render("三角錐: 業績加 30，打字完成花 1 秒，未完成花 5 秒", True, (0, 0, 70))
    screen.blit(text5, (80, 330))
    image_tnt = pygame.image.load('tnt.png').convert_alpha()
    image_tnt = pygame.transform.scale(image_tnt, (40, 40))
    screen.blit(image_tnt, (20, 380))
    text6 = word1.render("炸彈:   業績加 0，會炸掉周圍的物品", True, (0, 0, 70))
    screen.blit(text6, (80, 380))
    image_d = pygame.image.load('drink.png').convert_alpha()
    image_d = pygame.transform.scale(image_d, (40, 40))
    screen.blit(image_d, (20, 430))
    text8 = word1.render("酒駕犯: 業績加 600，花費 1 秒", True, (0, 0, 70))
    screen.blit(text8, (80, 430))


# next按鈕
upImageFilename = 'next.png'
downImageFilename = 'next1.png'
button2 = Button(upImageFilename, downImageFilename, (400, 530))

# 本關目標業績畫面
background1 = pygame.image.load('goal.png').convert_alpha()  # 背景
background1 = pygame.transform.scale(background1, (800, 600))

# 正式遊戲畫面
background2 = pygame.image.load('background3.png').convert_alpha()
background2 = pygame.transform.scale(background2, (800, 600))

# 更新畫面，等所有操作完成後一次更新（若沒更新，則元素不會出現）
pygame.display.update()

stop = ''
# 事件迴圈監聽事件，進行事件處理
while True:
    if '10' not in stop:  # 起始頁
        button1.render()
    else:  # 遊戲說明頁面
        screen.fill((255, 255, 255))
        screen.blit(background, (0, 0))
        Instruction()
        break
    # 迭代整個事件迴圈，若有符合事件則對應處理
    for event in pygame.event.get():
        # 當使用者結束視窗，程式也結束
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if button1.isOver() is True:
                stop += '1'
        # 如果釋放滑鼠按鈕
        elif event.type == pygame.MOUSEBUTTONUP:
            if button1.isOver() is True:
                stop += '0'
    pygame.display.update()

stop = ''
# 事件迴圈監聽事件，進行事件處理
while True:
    if '10' not in stop:  # 起始頁
        button2.render()
    else:  # 詳細介紹頁面
        screen.fill((255, 255, 255))
        screen.blit(background, (0, 0))
        Instruction1()
        break
    # 迭代整個事件迴圈，若有符合事件則對應處理
    for event in pygame.event.get():
        # 當使用者結束視窗，程式也結束
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if button1.isOver() is True:
                stop += '1'
        # 如果釋放滑鼠按鈕
        elif event.type == pygame.MOUSEBUTTONUP:
            if button1.isOver() is True:
                stop += '0'
    pygame.display.update()


def curr_goal(now_level):  # 目標業績頁面
    screen.fill((200, 200, 200))
    screen.blit(background1, (0, 0))
    word1 = pygame.font.Font("NotoSansMonoCJKtc-Bold.otf", 120)
    text = word1.render('$' + str(goal[now_level]), True, (250, 155, 0))
    screen.blit(text, (300, 300))  # 對齊
    pygame.display.flip()
    pygame.time.wait(2000)
    screen.fill((255, 255, 255))
    pygame.display.update()


goal = [750, 1620, 2810, 4560, 6666, 7900, 9900, 12500, 14330, 16666]  # 目標業績
now_level = 0  # 現在關卡
stop = ''
# 事件迴圈監聽事件，進行事件處理(遊戲說明)
while True:
    if '10' not in stop:
        button2.render()
    else:
        curr_goal(now_level)
        break
    # 迭代整個事件迴圈，若有符合事件則對應處理
    for event in pygame.event.get():
        # 當使用者結束視窗，程式也結束
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if button2.isOver() is True:
                stop += '1'
        # 如果釋放鼠標
        elif event.type == pygame.MOUSEBUTTONUP:
            if button2.isOver() is True:
                stop += '0'
    pygame.display.update()

# 初始化部分
fps = 40
ani = 4
clock = pygame.time.Clock()
pygame.init()

# 設遊戲視窗
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("抓到哩丟災")
background = pygame.image.load("background3.png").convert_alpha()
background = pygame.transform.scale(background, (800, 600))
# 放警察
police = pygame.image.load("police.png").convert_alpha()
police = pygame.transform.scale(police, (40, 70))

# 放字體
head_font = pygame.font.Font('NotoSansMonoCJKtc-Bold.otf', 30)
current_goal = 0
curr_goal_text = head_font.render('業績:     $' + str(current_goal), True, (200, 255, 255))

# 時間文字
time_text = head_font.render('時間', True, (200, 255, 255))

# 提早退出關卡
upImageFilename = 'exit.png'
downImageFilename = 'exit light.png'
button3 = Button_exit(upImageFilename, downImageFilename, (600, 50))

# 關卡
level = []
for i in range(1, 100):
    level.append(int(i))

pygame.display.flip()
clock.tick(fps)


# 精靈們


class Killer(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('killer.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (75, 130))
        self.image.set_colorkey(ALPHA)
        self.rect = self.image.get_rect()


class Bad(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('bad.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (60, 110))
        self.image.set_colorkey(ALPHA)
        self.rect = self.image.get_rect()


class Scammer(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('scammer.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.image.set_colorkey(ALPHA)
        self.rect = self.image.get_rect()


class Stealer(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('stealer.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (25, 35))
        self.image.set_colorkey(ALPHA)
        self.rect = self.image.get_rect()


class Triangle(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('triangle.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (30, 38))
        self.image.set_colorkey(ALPHA)
        self.rect = self.image.get_rect()


class Drink(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('drink.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (25, 35))
        self.image.set_colorkey(ALPHA)
        self.rect = self.image.get_rect()


class Tnt(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('tnt.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (60, 80))
        self.image.set_colorkey(ALPHA)
        self.rect = self.image.get_rect()


ALPHA = (0, 0, 0)


# 每關分布
class Level():
    def Criminal(lvl):
        killer_list = pygame.sprite.Group()
        scammer_list = pygame.sprite.Group()
        stealer_list = pygame.sprite.Group()
        triangle_list = pygame.sprite.Group()
        criminal_list = pygame.sprite.Group()
        bad_list = pygame.sprite.Group()
        global tnt_list
        tnt_list = pygame.sprite.Group()
        drink_list = pygame.sprite.Group()
        if lvl == 1:
            pos_x = [120, 650]
            pos_y = [380, 350]
            for i in range(2):
                killer = Killer()
                killer.rect.x = pos_x[i]
                killer.rect.y = pos_y[i]
                killer_list.add(killer)
            pos_x = [50, 340, 550]
            pos_y = [250, 450, 350]
            for i in range(3):
                scammer = Scammer()
                scammer.rect.x = pos_x[i]
                scammer.rect.y = pos_y[i]
                scammer_list.add(scammer)
            pos_x = [100, 250, 380, 650, 725]
            pos_y = [200, 350, 230, 200, 250]
            for i in range(5):
                stealer = Stealer()
                stealer.rect.x = pos_x[i]
                stealer.rect.y = pos_y[i]
                stealer_list.add(stealer)
            pos_x = [120, 300, 500, 680]
            pos_y = [280, 350, 400, 300]
            for i in range(4):
                triangle = Triangle()
                triangle.rect.x = pos_x[i]
                triangle.rect.y = pos_y[i]
                triangle_list.add(triangle)
            criminal_list.add(killer_list)
            criminal_list.add(scammer_list)
            criminal_list.add(stealer_list)
            criminal_list.add(triangle_list)
        if lvl == 2:
            pos_x = [30]
            pos_y = [430]
            for i in range(1):
                killer = Killer()
                killer.rect.x = pos_x[i]
                killer.rect.y = pos_y[i]
                killer_list.add(killer)
            pos_x = [40, 750, 500]
            pos_y = [250, 500, 350]
            for i in range(3):
                scammer = Scammer()
                scammer.rect.x = pos_x[i]
                scammer.rect.y = pos_y[i]
                scammer_list.add(scammer)
            pos_x = [100, 250, 420, 610, 720]
            pos_y = [200, 350, 400, 170, 150]
            for i in range(5):
                stealer = Stealer()
                stealer.rect.x = pos_x[i]
                stealer.rect.y = pos_y[i]
                stealer_list.add(stealer)
            pos_x = [30, 110, 110, 650]
            pos_y = [380, 250, 460, 240]
            for i in range(4):
                triangle = Triangle()
                triangle.rect.x = pos_x[i]
                triangle.rect.y = pos_y[i]
                triangle_list.add(triangle)
            pos_x = [330, 700]
            pos_y = [450, 240]
            for i in range(2):
                bad = Bad()
                bad.rect.x = pos_x[i]
                bad.rect.y = pos_y[i]
                bad_list.add(bad)
            criminal_list.add(killer_list)
            criminal_list.add(bad_list)
            criminal_list.add(scammer_list)
            criminal_list.add(stealer_list)
            criminal_list.add(triangle_list)
        if lvl == 3:
            pos_x = [150]
            pos_y = [430]
            for i in range(1):
                killer = Killer()
                killer.rect.x = pos_x[i]
                killer.rect.y = pos_y[i]
                killer_list.add(killer)
            pos_x = [70, 700]
            pos_y = [290, 180]
            for i in range(2):
                scammer = Scammer()
                scammer.rect.x = pos_x[i]
                scammer.rect.y = pos_y[i]
                scammer_list.add(scammer)
            pos_x = [130, 140, 190]
            pos_y = [160, 225, 180]
            for i in range(3):
                stealer = Stealer()
                stealer.rect.x = pos_x[i]
                stealer.rect.y = pos_y[i]
                stealer_list.add(stealer)
            pos_x = [125, 580, 520, 640]
            pos_y = [380, 180, 240, 250]
            for i in range(4):
                triangle = Triangle()
                triangle.rect.x = pos_x[i]
                triangle.rect.y = pos_y[i]
                triangle_list.add(triangle)
            pos_x = [370]
            pos_y = [260]
            for i in range(1):
                bad = Bad()
                bad.rect.x = pos_x[i]
                bad.rect.y = pos_y[i]
                bad_list.add(bad)
            pos_x = [73, 583]
            pos_y = [200, 230]
            for i in range(2):
                drink = Drink()
                drink.rect.x = pos_x[i]
                drink.rect.y = pos_y[i]
                drink_list.add(drink)
            criminal_list.add(killer_list)
            criminal_list.add(bad_list)
            criminal_list.add(scammer_list)
            criminal_list.add(stealer_list)
            criminal_list.add(triangle_list)
            criminal_list.add(drink_list)
        if lvl == 4:
            pos_x = [50, 700]
            pos_y = [430, 440]
            for i in range(2):
                killer = Killer()
                killer.rect.x = pos_x[i]
                killer.rect.y = pos_y[i]
                killer_list.add(killer)
            pos_x = [70]
            pos_y = [270]
            for i in range(1):
                scammer = Scammer()
                scammer.rect.x = pos_x[i]
                scammer.rect.y = pos_y[i]
                scammer_list.add(scammer)
            pos_x = [90, 330]
            pos_y = [130, 425]
            for i in range(2):
                stealer = Stealer()
                stealer.rect.x = pos_x[i]
                stealer.rect.y = pos_y[i]
                stealer_list.add(stealer)
            pos_x = [130, 210, 650]
            pos_y = [140, 390, 240]
            for i in range(3):
                triangle = Triangle()
                triangle.rect.x = pos_x[i]
                triangle.rect.y = pos_y[i]
                triangle_list.add(triangle)
            pos_x = [240, 530]
            pos_y = [450, 390]
            for i in range(2):
                bad = Bad()
                bad.rect.x = pos_x[i]
                bad.rect.y = pos_y[i]
                bad_list.add(bad)
            pos_x = [33, 370, 700]
            pos_y = [320, 455, 290]
            for i in range(3):
                drink = Drink()
                drink.rect.x = pos_x[i]
                drink.rect.y = pos_y[i]
                drink_list.add(drink)
            criminal_list.add(killer_list)
            criminal_list.add(bad_list)
            criminal_list.add(scammer_list)
            criminal_list.add(stealer_list)
            criminal_list.add(triangle_list)
            criminal_list.add(drink_list)
        if lvl == 5:
            pos_x = [50, 660]
            pos_y = [350, 440]
            for i in range(2):
                killer = Killer()
                killer.rect.x = pos_x[i]
                killer.rect.y = pos_y[i]
                killer_list.add(killer)
            pos_x = [400]
            pos_y = [300]
            for i in range(1):
                stealer = Stealer()
                stealer.rect.x = pos_x[i]
                stealer.rect.y = pos_y[i]
                stealer_list.add(stealer)
            pos_x = [660]
            pos_y = [230]
            for i in range(1):
                triangle = Triangle()
                triangle.rect.x = pos_x[i]
                triangle.rect.y = pos_y[i]
                triangle_list.add(triangle)
            pos_x = [270]
            pos_y = [450]
            for i in range(1):
                bad = Bad()
                bad.rect.x = pos_x[i]
                bad.rect.y = pos_y[i]
                bad_list.add(bad)
            pos_x = [63, 180, 115, 190, 400, 600, 720]
            pos_y = [110, 190, 485, 520, 480, 250, 280]
            for i in range(7):
                drink = Drink()
                drink.rect.x = pos_x[i]
                drink.rect.y = pos_y[i]
                drink_list.add(drink)
            pos_x = [100, 470]
            pos_y = [130, 400]
            for i in range(2):
                tnt = Tnt()
                tnt.rect.x = pos_x[i]
                tnt.rect.y = pos_y[i]
                tnt_list.add(tnt)
            criminal_list.add(killer_list)
            criminal_list.add(tnt_list)
            criminal_list.add(bad_list)
            criminal_list.add(stealer_list)
            criminal_list.add(triangle_list)
            criminal_list.add(drink_list)
        if lvl == 6:
            pos_x = [60]
            pos_y = [300]
            for i in range(1):
                triangle = Triangle()
                triangle.rect.x = pos_x[i]
                triangle.rect.y = pos_y[i]
                triangle_list.add(triangle)
            pos_x = [23, 355, 480, 230, 570, 400, 270, 540, 720]
            pos_y = [340, 150, 150, 350, 350, 520, 520, 520, 350]
            for i in range(9):
                drink = Drink()
                drink.rect.x = pos_x[i]
                drink.rect.y = pos_y[i]
                drink_list.add(drink)
            tnt_list = pygame.sprite.Group()
            pos_x = [400, 290, 490, 200, 580]
            pos_y = [130, 300, 300, 450, 450]
            for i in range(5):
                tnt = Tnt()
                tnt.rect.x = pos_x[i]
                tnt.rect.y = pos_y[i]
                tnt_list.add(tnt)
            criminal_list.add(tnt_list)
            criminal_list.add(triangle_list)
            criminal_list.add(drink_list)
        if lvl == 7:
            pos_x = [70, 360, 550]
            pos_y = [400, 450, 420]
            for i in range(3):
                killer = Killer()
                killer.rect.x = pos_x[i]
                killer.rect.y = pos_y[i]
                killer_list.add(killer)
            pos_x = [300, 330, 390, 450, 600, 670, 730]
            pos_y = [200, 300, 150, 310, 200, 330, 155]
            for i in range(7):
                triangle = Triangle()
                triangle.rect.x = pos_x[i]
                triangle.rect.y = pos_y[i]
                triangle_list.add(triangle)
            pos_x = [710]
            pos_y = [460]
            for i in range(1):
                bad = Bad()
                bad.rect.x = pos_x[i]
                bad.rect.y = pos_y[i]
                bad_list.add(bad)
            pos_x = [100, 180]
            pos_y = [150, 230]
            for i in range(2):
                stealer = Stealer()
                stealer.rect.x = pos_x[i]
                stealer.rect.y = pos_y[i]
                stealer_list.add(stealer)
            pos_x = [40, 70]
            pos_y = [350, 540]
            for i in range(2):
                drink = Drink()
                drink.rect.x = pos_x[i]
                drink.rect.y = pos_y[i]
                drink_list.add(drink)
            pos_x = [680]
            pos_y = [205]
            for i in range(1):
                tnt = Tnt()
                tnt.rect.x = pos_x[i]
                tnt.rect.y = pos_y[i]
                tnt_list.add(tnt)
            criminal_list.add(killer_list)
            criminal_list.add(tnt_list)
            criminal_list.add(bad_list)
            criminal_list.add(stealer_list)
            criminal_list.add(triangle_list)
            criminal_list.add(drink_list)
        if lvl == 8:
            pos_x = [70, 460]
            pos_y = [400, 400]
            for i in range(2):
                killer = Killer()
                killer.rect.x = pos_x[i]
                killer.rect.y = pos_y[i]
                killer_list.add(killer)
            pos_x = [710]
            pos_y = [355]
            for i in range(1):
                triangle = Triangle()
                triangle.rect.x = pos_x[i]
                triangle.rect.y = pos_y[i]
                triangle_list.add(triangle)
            pos_x = [360]
            pos_y = [410]
            for i in range(1):
                bad = Bad()
                bad.rect.x = pos_x[i]
                bad.rect.y = pos_y[i]
                bad_list.add(bad)
            pos_x = [370, 680]
            pos_y = [200, 200]
            for i in range(2):
                scammer = Scammer()
                scammer.rect.x = pos_x[i]
                scammer.rect.y = pos_y[i]
                scammer_list.add(scammer)
            pos_x = [40, 200, 300, 620, 760]
            pos_y = [290, 200, 540, 355, 430]
            for i in range(5):
                drink = Drink()
                drink.rect.x = pos_x[i]
                drink.rect.y = pos_y[i]
                drink_list.add(drink)
            pos_x = [30, 200]
            pos_y = [150, 460]
            for i in range(2):
                tnt = Tnt()
                tnt.rect.x = pos_x[i]
                tnt.rect.y = pos_y[i]
                tnt_list.add(tnt)
            criminal_list.add(killer_list)
            criminal_list.add(tnt_list)
            criminal_list.add(bad_list)
            criminal_list.add(scammer_list)
            criminal_list.add(triangle_list)
            criminal_list.add(drink_list)
        if lvl == 9:
            pos_x = [500]
            pos_y = [460]
            for i in range(1):
                killer = Killer()
                killer.rect.x = pos_x[i]
                killer.rect.y = pos_y[i]
                killer_list.add(killer)
            pos_x = [40, 130]
            pos_y = [410, 350]
            for i in range(2):
                bad = Bad()
                bad.rect.x = pos_x[i]
                bad.rect.y = pos_y[i]
                bad_list.add(bad)
            pos_x = [690]
            pos_y = [350]
            for i in range(1):
                scammer = Scammer()
                scammer.rect.x = pos_x[i]
                scammer.rect.y = pos_y[i]
                scammer_list.add(scammer)
            pos_x = [40, 300, 480, 400, 755]
            pos_y = [140, 210, 210, 480, 400]
            for i in range(5):
                drink = Drink()
                drink.rect.x = pos_x[i]
                drink.rect.y = pos_y[i]
                drink_list.add(drink)
            pos_x = [70, 220, 400, 565]
            pos_y = [150, 220, 220, 220]
            for i in range(4):
                tnt = Tnt()
                tnt.rect.x = pos_x[i]
                tnt.rect.y = pos_y[i]
                tnt_list.add(tnt)
            pos_x = [150, 650]
            pos_y = [250, 130]
            for i in range(2):
                stealer = Stealer()
                stealer.rect.x = pos_x[i]
                stealer.rect.y = pos_y[i]
                stealer_list.add(stealer)
            criminal_list.add(killer_list)
            criminal_list.add(tnt_list)
            criminal_list.add(bad_list)
            criminal_list.add(scammer_list)
            criminal_list.add(stealer_list)
            criminal_list.add(drink_list)
        if lvl == 10:
            pos_x = [40, 470]
            pos_y = [450, 400]
            for i in range(2):
                killer = Killer()
                killer.rect.x = pos_x[i]
                killer.rect.y = pos_y[i]
                killer_list.add(killer)
            pos_x = [90, 190, 680]
            pos_y = [200, 470, 200]
            for i in range(3):
                triangle = Triangle()
                triangle.rect.x = pos_x[i]
                triangle.rect.y = pos_y[i]
                triangle_list.add(triangle)
            pos_x = [710]
            pos_y = [410]
            for i in range(1):
                bad = Bad()
                bad.rect.x = pos_x[i]
                bad.rect.y = pos_y[i]
                bad_list.add(bad)
            pos_x = [50, 120, 470, 550, 730]
            pos_y = [360, 430, 330, 540, 160]
            for i in range(5):
                scammer = Scammer()
                scammer.rect.x = pos_x[i]
                scammer.rect.y = pos_y[i]
                scammer_list.add(scammer)
            pos_x = [70, 160, 190]
            pos_y = [140, 170, 230]
            for i in range(3):
                stealer = Stealer()
                stealer.rect.x = pos_x[i]
                stealer.rect.y = pos_y[i]
                stealer_list.add(stealer)
            criminal_list.add(killer_list)
            criminal_list.add(bad_list)
            criminal_list.add(scammer_list)
            criminal_list.add(stealer_list)
            criminal_list.add(triangle_list)

        return criminal_list


# 警車手銬
class Policecar(pygame.sprite.Sprite):
    def __init__(self, width, height):
        super().__init__()
        self.raw_image = pygame.image.load("policecar.png").convert_alpha()
        self.image = pygame.transform.scale(self.raw_image, (width, height))
        self.image = pygame.transform.rotate(self.image, 0)
        self.rect = self.image.get_rect()
        self.rect.topleft = (350, 30)
        self.org_image = self.image.copy()
        self.angle = 0
        self.direction = pygame.Vector2(1, 0)
        self.pos = pygame.Vector2(self.rect.center)

    def update(self, events, dt, angle):
        for e in events:
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_SPACE:
                    self.groups()[0].add(Handcuff(self.rect.center, self.direction.normalize(), 25, 15))
        self.angle = math.sin(angle) * 70
        self.direction = pygame.Vector2(0, 1).rotate(-self.angle)
        self.image = pygame.transform.rotate(self.org_image, self.angle)
        self.rect = self.image.get_rect(center=self.rect.center)


class Handcuff(pygame.sprite.Sprite):
    def __init__(self, pos, direction, width, height):
        super().__init__()
        self.raw_image = pygame.image.load("handcuff.png").convert_alpha()
        self.image = pygame.transform.scale(self.raw_image, (width, height))
        self.rect = self.image.get_rect()
        self.rect.topleft = (350, 30)
        self.org_image = self.image.copy()
        self.rect = self.image.get_rect(center=pos)
        self.direction = direction
        self.pos = pygame.Vector2(self.rect.center)
        self.lives = 15
        self.angle = 0

    def update(self, events, dt, angle):
        # where we would move next
        next_pos = self.pos + self.direction * dt

        # set the new position
        self.pos = next_pos
        self.rect.center = self.pos
        self.angle += 40
        self.image = pygame.transform.rotate(self.org_image, self.angle)
        self.rect = self.image.get_rect(center=self.rect.center)


boom_switch = False
clock_switch = False
donut_switch = False
remove_switch = False
dec1_switch = False
dec2_switch = False
dec3_switch = False
dec4_switch = False


# 恭喜通關
def Congrats():
    global boom_switch
    global clock_switch
    global donut_switch
    global remove_switch
    global dec1_switch
    global dec2_switch
    global dec3_switch
    global dec4_switch
    boom_switch = False
    clock_switch = False
    donut_switch = False
    remove_switch = False
    dec1_switch = False
    dec2_switch = False
    dec3_switch = False
    dec4_switch = False

    window_surface = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('抓到哩丟災')  # 命名
    background = pygame.image.load('achieve.png').convert_alpha()  # 背景
    background = pygame.transform.scale(background, (800, 600))
    window_surface.blit(background, (0, 0))
    pygame.display.flip()
    pygame.time.wait(2000)

    window_surface.fill((255, 255, 255))
    # 商店背景
    background = pygame.image.load('store1.png').convert_alpha()
    background = pygame.transform.smoothscale(background, (800, 600))

    # 下注背景
    de_background = pygame.image.load('gamblewithoutdetec.png').convert_alpha()
    de_background = pygame.transform.smoothscale(de_background, (800, 600))

    # 叫字體
    notoSans_40 = pygame.font.Font('NotoSansMonoCJKtc-Bold.otf', 40)
    notoSans_20 = pygame.font.Font('NotoSansMonoCJKtc-Bold.otf', 20)

    # 讓字換行啦(要講的話)(開始位置)(下移級距)(大小)(顏色)
    def blitText(text, position, y_move, fontsize=notoSans_20, color=(41, 36, 33)):
        blitlist = text.split('\n')
        x = position[0]
        y = position[1]
        for line in blitlist:
            currenttext = fontsize.render(line, True, color)
            window_surface.blit(currenttext, (x, y))
            y += y_move
        return text

    class Button(object):
        def __init__(self, upimage, downimage, position, scale):
            self.imageUp = pygame.image.load(upimage).convert_alpha()
            self.imageUp = pygame.transform.scale(self.imageUp, scale)
            self.imageDown = pygame.image.load(downimage).convert_alpha()
            self.imageDown = pygame.transform.scale(self.imageDown, scale)
            self.position = position
            self.upimage = upimage

        def isOver(self):
            point_x, point_y = pygame.mouse.get_pos()
            x, y = self.position
            w, h = self.imageUp.get_size()

            in_x = x < point_x < x + w
            in_y = y < point_y < y + h
            return in_x and in_y

        def render(self, text=None, messenger=None, text_position=None, messenger_position=None, fontsize=notoSans_20,
                   color=(41, 36, 33)):
            w, h = self.imageUp.get_size()
            x, y = self.position

            if self.isOver():
                window_surface.blit(self.imageDown, (x, y))
                if messenger != None:
                    window_surface.blit(messenger, messenger_position)
                if text != None:
                    blitText(text, text_position, 25, fontsize, color)
            else:
                window_surface.blit(self.imageUp, (x, y))

        def itemtype(self):
            if self.upimage == 'boom.png':
                item = 'boom'
            elif self.upimage == 'clock.png':
                item = 'clock'
            elif self.upimage == 'donut.png':
                item = 'donut'
            elif self.upimage == 'remove.png':
                item = 'remove'
            return item

    # 叫按鍵
    bet = 'bet.png'
    bet_pressed = 'bet1.png'
    bet_button = Button(bet, bet_pressed, (0, 525), (150, 75))

    passbuttom = 'pass.png'
    passbuttom_pressed = 'pass1.png'
    passbuttom = Button(passbuttom, passbuttom_pressed, (0, 0), (150, 75))

    b2store = 'store button.png'
    b2store_pressed = 'store button dark.png'
    b2store_button = Button(b2store, b2store_pressed, (0, 0), (150, 75))

    # 叫對話框
    messenger = pygame.image.load('text.png')
    messenger = pygame.transform.scale(messenger, (350, 350))
    g_messenger = pygame.image.load('—Pngtree—certificate border_2241181.png')
    g_messenger = pygame.transform.scale(g_messenger, (600, 180))

    # 叫道具
    boom = 'boom.png'
    boom_pressed = 'boom ver.dark.png'
    boom_scale = (90, 108)

    clock = 'clock.png'
    clock_pressed = 'clock ver.dark.png'
    clock_scale = (100, 100)

    donut = 'donut.png'
    donut_pressed = 'donut ver.dark.png'
    donut_scale = (125, 100)

    remove = 'remove.png'
    remove_pressed = 'remove ver.dark.png'
    remove_scale = (100, 100)

    # 叫偵探
    dec1 = "detective1.png"
    dec1_pressed = 'detective1 dark.png'
    dec1_scale = (140, 140)
    dec1_buttom = Button(dec1, dec1_pressed, (80, 150), dec1_scale)

    dec2 = "detective5.png"
    dec2_pressed = 'detective5 dark.png'
    dec2_scale = (150, 150)
    dec2_buttom = Button(dec2, dec2_pressed, (235, 145), dec2_scale)

    dec3 = "detective3.png"
    dec3_pressed = 'detective3 dark.png'
    dec3_scale = (160, 160)
    dec3_buttom = Button(dec3, dec3_pressed, (400, 135), dec3_scale)

    dec4 = "detective4.png"
    dec4_pressed = 'detective4 dark.png'
    dec4_scale = (140, 140)
    dec4_buttom = Button(dec4, dec4_pressed, (560, 150), dec4_scale)

    # 建偵探字
    d1_text = '一位破案機率40%的名偵探'
    d2_text = '一位破案機率50%的名偵探'
    d3_text = '一位破案機率60%的名偵探'
    d4_text = '一位破案機率70%的名偵探'

    # 建偵探字tuple
    decs_text_tuple = [(dec1, dec1_buttom, d1_text), (dec2, dec2_buttom, d2_text), (dec3, dec3_buttom, d3_text),
                       (dec4, dec4_buttom, d4_text)]

    # 叫價錢版
    pricetag = pygame.image.load('price2.png')
    pricetag = pygame.transform.smoothscale(pricetag, (130, 65))
    g_pricetag = pygame.image.load('price4.png')
    g_pricetag = pygame.transform.smoothscale(g_pricetag, (130, 65))

    # 產生隨機價錢
    def randomprice():
        price_num = random.randint(1, 500)
        randomprice = '$' + str(price_num)
        price = notoSans_40.render(randomprice, True, (255, 245, 238))
        return price_num, price

    # 建現在資金
    global current_goal
    money = notoSans_40.render('現有資金: $' + str(current_goal), True, (255, 250, 250))  # 位置要調

    # 建偵探價格
    d1_price = notoSans_20.render('$500', True, (255, 250, 250))
    d2_price = notoSans_20.render('$700', True, (255, 250, 250))
    d3_price = notoSans_20.render('$900', True, (255, 250, 250))
    d4_price = notoSans_20.render('$1100', True, (255, 250, 250))

    # 產生隨機道具
    k = random.randint(2, 3)

    items = [(boom, boom_pressed, boom_scale), (clock, clock_pressed, clock_scale), (donut, donut_pressed, donut_scale),
             (remove, remove_pressed, remove_scale)]
    currentitems = random.sample(items, k)

    for i, item in enumerate(currentitems):
        if i == 0:
            item1 = item[0]
            item_buttom1 = Button(item[0], item[1], (200, 100), item[2])
            pricenum1, price1 = randomprice()
            currentitems[0] = (item1, item_buttom1)
        elif i == 1:
            item2 = item[0]
            item_buttom2 = Button(item[0], item[1], (200, 230), item[2])
            pricenum2, price2 = randomprice()
            currentitems[1] = (item2, item_buttom2)
            item_num = 2
        elif i == 2:
            item3 = item[0]
            item_buttom3 = Button(item[0], item[1], (200, 380), item[2])
            pricenum3, price3 = randomprice()
            currentitems[2] = (item3, item_buttom3)
            item_num = 3

    # 博士要說的話
    def whichitem(item):
        if item == boom:
            text = '按方向鍵上↑可炸\n掉手銬上不想通緝\n的人物或物品，可\n節省時間抓其他犯\n人。'
        elif item == clock:
            text = '總時間變為兩倍。'
        elif item == donut:
            text = '將所有句子變成單\n子，加快抓到犯人\n的速度。'
        elif item == remove:
            text = '拆除地圖上的TNT。'
        return text

    def turnswitchon(item):
        global boom_switch
        global clock_switch
        global donut_switch
        global remove_switch
        if item == 'boom':
            boom_switch = True
            for item_tuple in currentitems:
                if item_tuple[0] == boom:
                    currentitems.remove(item_tuple)
        elif item == 'clock':
            clock_switch = True
            for item_tuple in currentitems:
                if item_tuple[0] == clock:
                    currentitems.remove(item_tuple)
        elif item == 'donut':
            donut_switch = True
            for item_tuple in currentitems:
                if item_tuple[0] == donut:
                    currentitems.remove(item_tuple)
        elif item == 'remove':
            remove_switch = True
            for item_tuple in currentitems:
                if item_tuple[0] == remove:
                    currentitems.remove(item_tuple)

    def switchonornot(item):
        global boom_switch
        global clock_switch
        global donut_switch
        global remove_switch
        if item == 'boom':
            return boom_switch
        if item == 'clock':
            return clock_switch
        if item == 'donut':
            return donut_switch
        if item == 'remove':
            return remove_switch

    stop = []
    # 事件迴圈監聽事件，進行事件處理
    while True:
        if '1' not in stop:  # 商店
            money = notoSans_40.render('現有資金: $' + str(current_goal), True, (255, 250, 250))
            window_surface.blit(background, (0, 0))
            bet_button.render()
            passbuttom.render()
            window_surface.blit(money, (450, 0))
            if item_num == 2:
                window_surface.blit(pricetag, (320, 100))
                window_surface.blit(price1, (345, 105))
                window_surface.blit(pricetag, (320, 230))
                window_surface.blit(price2, (345, 235))
            elif item_num == 3:
                window_surface.blit(pricetag, (320, 100))
                window_surface.blit(price1, (345, 105))
                window_surface.blit(pricetag, (320, 230))
                window_surface.blit(price2, (345, 235))
                window_surface.blit(pricetag, (320, 360))
                window_surface.blit(price3, (345, 365))
            if len(currentitems) != 0:
                for item_tuple in currentitems:
                    text = whichitem(item_tuple[0])
                    item_tuple[1].render(text, messenger, (525, 150), (430, 50), notoSans_20, (41, 36, 33))

        else:  # 下注
            money = notoSans_40.render('現有資金: $' + str(current_goal), True, (255, 250, 250))
            window_surface.blit(de_background, (0, 0))
            window_surface.blit(money, (375, 0))
            b2store_button.render()
            window_surface.blit(g_pricetag, (85, 350))
            window_surface.blit(g_pricetag, (250, 350))
            window_surface.blit(g_pricetag, (400, 350))
            window_surface.blit(g_pricetag, (550, 350))
            window_surface.blit(g_messenger, (100, 400))
            window_surface.blit(d1_price, (125, 365))
            window_surface.blit(d2_price, (290, 365))
            window_surface.blit(d3_price, (445, 365))
            window_surface.blit(d4_price, (590, 365))
            if len(decs_text_tuple) != 0:
                for currentdec in decs_text_tuple:
                    text = currentdec[2]
                    currentdec[1].render(text, text_position=(150, 430), fontsize=notoSans_40,
                                         color=(255, 250, 250))
        if '2' in stop:
            stop = []
            break

        # 迭代整個事件迴圈，若有符合事件則對應處理
        for event in pygame.event.get():
            # 當使用者結束視窗，程式也結束
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if bet_button.isOver() is True:
                    push = 0
                elif b2store_button.isOver() is True and stop != []:
                    push = 1
                elif passbuttom.isOver() is True and stop == []:
                    push = 2
                if item_num == 2:
                    if item_buttom1.isOver() is True:
                        push = 3
                    elif item_buttom2.isOver() is True:
                        push = 4
                elif item_num == 3:
                    if item_buttom1.isOver() is True:
                        push = 3
                    elif item_buttom2.isOver() is True:
                        push = 4
                    elif item_buttom3.isOver() is True:
                        push = 5
                if dec1_buttom.isOver() is True:
                    push = 6
                elif dec2_buttom.isOver() is True:
                    push = 7
                elif dec3_buttom.isOver() is True:
                    push = 8
                elif dec4_buttom.isOver() is True:
                    push = 9
            # 如果釋放滑鼠按鈕
            elif event.type == pygame.MOUSEBUTTONUP:
                check = pygame.mixer.Sound('check.mp3')
                if bet_button.isOver() is True:
                    if push == 0:
                        stop.append('1')
                elif b2store_button.isOver() is True and stop != []:
                    if push == 1:
                        stop.remove('1')
                elif passbuttom.isOver() is True and stop == []:
                    if push == 2:
                        stop.append('2')
                if item_num == 2:
                    if item_buttom1.isOver() is True and current_goal >= pricenum1 and '1' not in stop:
                        check.play()
                        item = item_buttom1.itemtype()
                        if switchonornot(item) != True:
                            turnswitchon(item)
                            current_goal -= pricenum1

                    elif item_buttom2.isOver() is True and current_goal >= pricenum2 and '1' not in stop:
                        check.play()
                        item = item_buttom2.itemtype()
                        if switchonornot(item) != True:
                            turnswitchon(item)
                            current_goal -= pricenum2
                if item_num == 3:
                    if item_buttom1.isOver() is True and current_goal >= pricenum1 and '1' not in stop:
                        check.play()
                        item = item_buttom1.itemtype()
                        if switchonornot(item) != True:
                            turnswitchon(item)
                            current_goal -= pricenum1
                    elif item_buttom2.isOver() is True and current_goal >= pricenum2 and '1' not in stop:
                        check.play()
                        item = item_buttom2.itemtype()
                        if switchonornot(item) != True:
                            turnswitchon(item)
                            current_goal -= pricenum2
                    elif item_buttom3.isOver() is True and current_goal >= pricenum3 and '1' not in stop:
                        check.play()
                        item = item_buttom3.itemtype()
                        if switchonornot(item) != True:
                            turnswitchon(item)
                            current_goal -= pricenum3
                if dec1_buttom.isOver() and current_goal >= 500 and '1' in stop:
                    check.play()
                    if dec1_switch != True:
                        dec1_switch = True
                        for currentdec in decs_text_tuple:
                            if currentdec[0] == dec1:
                                decs_text_tuple.remove(currentdec)
                        current_goal -= 500
                elif dec2_buttom.isOver() and current_goal >= 700 and '1' in stop:
                    check.play()
                    if dec2_switch != True:
                        dec2_switch = True
                        for currentdec in decs_text_tuple:
                            if currentdec[0] == dec2:
                                decs_text_tuple.remove(currentdec)
                        current_goal -= 700
                elif dec3_buttom.isOver() and current_goal >= 900 and '1' in stop:
                    check.play()
                    if dec3_switch != True:
                        dec3_switch = True
                        for currentdec in decs_text_tuple:
                            if currentdec[0] == dec3:
                                decs_text_tuple.remove(currentdec)
                        current_goal -= 900
                elif dec4_buttom.isOver() and current_goal >= 1100 and '1' in stop:
                    check.play()
                    if dec4_switch != True:
                        dec4_switch = True
                        for currentdec in decs_text_tuple:
                            if currentdec[0] == dec4:
                                decs_text_tuple.remove(currentdec)
                        current_goal -= 1100

        pygame.display.update()


# 遊戲結束
def Gameover():
    # 初始化
    pygame.init()
    window_surface = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('抓到哩丟災')  # 命名
    window_surface.fill((255, 255, 255))

    background = pygame.image.load('gameover.png').convert_alpha()  # 背景
    background = pygame.transform.scale(background, (800, 600))
    window_surface.blit(background, (0, 0))
    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        pygame.display.update()


def select_word():
    path = '7000.txt'
    with open(path, 'r', encoding='UTF-8') as f1:
        word_list = []
        for w in f1.readlines():
            w = w.strip('\n ')
            word_list.append(str(w))
    num_of_elements = len(word_list)
    i = random.randint(0, num_of_elements - 1)
    return word_list[i]


def select_sentence():
    path = '100_sentence.txt'
    with open(path, 'r', encoding='UTF-8') as f2:
        sentence_list = []
        for w in f2.readlines():
            w = w.strip('\n ')
            sentence_list.append(str(w))
    num_of_elements = len(sentence_list)
    i = random.randint(0, num_of_elements - 1)
    return sentence_list[i]


def cut_head_char(word):
    return word[1:]


def is_empty_word(word):
    return not word

freeze_sound = pygame.mixer.Sound('Freeze.mp3')
arrest_sound = pygame.mixer.Sound('super-mario-coin-sound.mp3')

def run_type(catch_item='hi'):
    global boom_switch
    freeze_sound.play()
    pygame.init()
    word = select_word()
    counter, text = 10, '10'.rjust(0)
    pygame.time.set_timer(pygame.USEREVENT, 1000)
    font = pygame.font.Font('NotoSansMonoCJKtc-Bold.otf', 100)
    font2 = pygame.font.Font('NotoSansMonoCJKtc-Bold.otf', 30)
    font3 = pygame.font.Font('NotoSansMonoCJKtc-Bold.otf', 60)
    while True:
        screen.fill((255, 255, 255))
        sf_word = font.render(word, True, (0, 0, 0))
        item_text = font3.render(catch_item, True, (30, 30, 30))
        center_x = screen.get_rect().width / 2 - sf_word.get_rect().width / 2
        screen.blit(sf_word, (center_x, 200))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.USEREVENT:
                counter -= 1
                text = str(counter).rjust(0)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and boom_switch == True:
                    boom_switch = False
                    return 0
                elif event.unicode == word[0]:
                    word = cut_head_char(word)
                    if is_empty_word(word):
                        arrest_sound.play()
                        return is_empty_word(word)

            elif counter == 0:
                return False
        else:
            screen.blit(font.render(text, True, (0, 0, 0)), (400, 0))
            screen.blit(item_text, (0, 0))
            clock.tick(60)
            pygame.display.flip()


def run_type_sentence(catch_item='hi'):
    global boom_switch
    freeze_sound.play()
    pygame.init()
    sentence = select_sentence()
    counter, text = 30, '30'.rjust(0)
    pygame.time.set_timer(pygame.USEREVENT, 1000)
    font = pygame.font.Font('NotoSansMonoCJKtc-Bold.otf', 30)
    font2 = pygame.font.Font('NotoSansMonoCJKtc-Bold.otf', 100)
    font3 = pygame.font.Font('NotoSansMonoCJKtc-Bold.otf', 60)
    while True:
        screen.fill((255, 255, 255))
        sf_sentence = font.render(sentence, True, (0, 0, 0))
        item_text = font3.render(catch_item, True, (30, 30, 30))
        center_x = screen.get_rect().width / 2 - sf_sentence.get_rect().width / 2
        screen.blit(sf_sentence, (center_x, 200))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.USEREVENT:
                counter -= 1
                text = str(counter).rjust(0)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and boom_switch == True:
                    boom_switch = False
                    return 3
                elif event.unicode == sentence[0]:
                    sentence = cut_head_char(sentence)
                    if is_empty_word(sentence):
                        arrest_sound.play()
                        return is_empty_word(sentence)

            elif counter == 0:
                return False
        else:
            screen.blit(font2.render(text, True, (0, 0, 0)), (400, 0))
            screen.blit(item_text, (0, 0))
            clock.tick(60)
            pygame.display.flip()


explosion_anim = {}
explosion_anim['lg'] = []
explosion_anim['sm'] = []
for i in range(9):
    filename = 'regularExplosion0{}.png'.format(i)
    img = pygame.image.load(filename).convert()
    img.set_colorkey((0, 0, 0))
    img_lg = pygame.transform.scale(img, (250, 250))
    explosion_anim['lg'].append(img_lg)
    img_sm = pygame.transform.scale(img, (600, 600))
    explosion_anim['sm'].append(img_sm)


# TNT爆炸
class Explosion(pygame.sprite.Sprite):
    def __init__(self, center, size):
        pygame.sprite.Sprite.__init__(self)
        self.size = size
        self.image = explosion_anim[self.size][0]
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.frame = 0
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 50

    def update(self, events, dt, angle):
        now = pygame.time.get_ticks()
        explode_sound = pygame.mixer.Sound('explode.mp3')
        explode_sound.set_volume(0.3)
        explode_sound.play()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1
            if self.frame == len(explosion_anim[self.size]):
                self.kill()
            else:
                center = self.rect.center
                self.image = explosion_anim[self.size][self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center


# 第一關
sprites = pygame.sprite.Group(Policecar(32, 50))
dt = 0
criminal_list = Level.Criminal(now_level + 1)
goal_text = head_font.render('目標業績: $' + str(goal[now_level]), True, (200, 255, 255))
if now_level < 9:
    level_text = head_font.render('Level ' + str(level[now_level]), True, (200, 255, 255))
elif now_level == 9:
    level_text = head_font.render('Level ' + str('10'), True, (200, 255, 255))

# 計時器
counter, text = 30, '30'.rjust(3)
pygame.time.set_timer(pygame.USEREVENT, 1000)
font = pygame.font.Font('NotoSansMonoCJKtc-Bold.otf', 30)
angle = math.pi / -6

stop = ''
# 遊戲中
while True:
    events = pygame.event.get()
    angle += math.pi / 100
    if '10' not in stop:
        button3.render()  # 退出本關的按鈕
    else:
        if current_goal >= goal[now_level]:
            Congrats()
            stop = ''
            now_level += 1
            if now_level == 10:
                break
            if clock_switch == True:
                counter = 62
            else:
                counter = 32
            criminal_list = Level.Criminal(lvl=now_level + 1)
            if remove_switch == True:
                if tnt_list != []:
                    criminal_list.remove(tnt_list)
            goal_text = head_font.render('目標業績: $' + str(goal[now_level]), True, (200, 255, 255))
            level_text = head_font.render('Level ' + str(level[now_level]), True, (200, 255, 255))
            curr_goal(now_level)
        else:
            possibility = random.randint(1, 100)
            if dec1_switch == True and possibility <= 40:
                current_goal = goal[now_level]
                continue
            if dec2_switch == True and possibility <= 50:
                current_goal = goal[now_level]
                continue
            if dec3_switch == True and possibility <= 60:
                current_goal = goal[now_level]
                continue
            if dec4_switch == True and possibility <= 70:
                current_goal = goal[now_level]
                continue
            Gameover()
    for e in events:
        if e.type == pygame.QUIT:
            sys.exit()
        elif e.type == pygame.MOUSEBUTTONDOWN:
            if button3.isOver() is True:
                stop += '1'
        # 如果釋放鼠標
        elif e.type == pygame.MOUSEBUTTONUP:
            if button3.isOver() is True:
                stop += '0'
        if e.type == pygame.USEREVENT:
            counter -= 1
            if counter >= 0:
                text = str(counter).rjust(3)
            else:
                if current_goal >= goal[now_level]:
                    Congrats()
                    now_level += 1
                    if now_level == 10:
                        break
                    if clock_switch == True:
                        counter = 62
                    else:
                        counter = 32
                    criminal_list = Level.Criminal(lvl=now_level + 1)
                    if remove_switch == True:
                        if tnt_list != []:
                            criminal_list.remove(tnt_list)
                    goal_text = head_font.render('目標業績: $' + str(goal[now_level]), True, (200, 255, 255))
                    level_text = head_font.render('Level ' + str(level[now_level]), True, (200, 255, 255))
                    curr_goal(now_level)
                    # 更新資訊
                else:
                    possibility = random.randint(1, 100)
                    if dec1_switch == True and possibility <= 40:
                        current_goal = goal[now_level]
                        continue
                    if dec2_switch == True and possibility <= 50:
                        current_goal = goal[now_level]
                        continue
                    if dec3_switch == True and possibility <= 60:
                        current_goal = goal[now_level]
                        continue
                    if dec4_switch == True and possibility <= 70:
                        current_goal = goal[now_level]
                        continue
                    Gameover()
        if e.type == pygame.QUIT:
            break
    else:  # 遊戲畫面
        killed = {}
        sprites.update(events, dt, angle)
        sprites.draw(screen)
        dt = clock.tick(80)
        screen.blit(font.render(text, True, (200, 255, 255)), (720, 10))
        pygame.display.flip()

        clock.tick(80)
        screen.fill((255, 255, 255))
        screen.blit(background, (0, 0))
        screen.blit(police, (425, 20))
        screen.blit(curr_goal_text, (5, 10))
        screen.blit(goal_text, (5, 50))
        screen.blit(time_text, (650, 10))
        screen.blit(level_text, (650, 50))
        criminal_list.draw(screen)
        killed = pygame.sprite.groupcollide(sprites, criminal_list, dokilla=sprites, dokillb=criminal_list,
                                            collided=pygame.sprite.collide_mask)
        killed_list = list(killed.values())
        killedstr = "".join('%s' % id for id in killed_list)
        if "Killer" in killedstr:
            if donut_switch == True:
                judge = run_type(catch_item='殺人犯(500)')
            else:
                judge = run_type_sentence(catch_item='殺人犯(500)')
            if judge != 0:
                counter -= 4
            if judge:
                current_goal += 500
        elif "Bad" in killedstr:
            judge = run_type(catch_item='壞蛋(250)')
            if judge != 0:
                counter -= 3
            if judge:
                current_goal += 250
        elif "Scammer" in killedstr:
            judge = run_type(catch_item='詐欺犯(100)')
            if judge != 0:
                counter -= 2
            if judge:
                current_goal += 100
        elif "Stealer" in killedstr:
            judge = run_type(catch_item='竊賊(50)')
            if judge != 0:
                counter -= 1
            if judge:
                current_goal += 50
        elif "Drink" in killedstr:
            if donut_switch == True:
                judge = run_type(catch_item='酒駕犯(600)')
            else:
                judge = run_type_sentence(catch_item='酒駕犯(600)')
            if judge != 0:
                counter -= 1
            if judge:
                current_goal += 600
        elif "Triangle" in killedstr:
            if donut_switch == True:
                judge = run_type(catch_item='三角錐(30)')
            else:
                judge = run_type_sentence(catch_item='三角錐(30)')
            if judge:
                current_goal += 30
                counter -= 1
            elif judge == False:
                counter -= 5
        elif "Tnt" in killedstr:
            for kill in killed:
                expl = Explosion(kill.rect.center, 'lg')
                sprites.add(expl)
                pygame.sprite.groupcollide(criminal_list, sprites, dokilla=criminal_list, dokillb=False,
                                           collided=pygame.sprite.collide_mask)
        curr_goal_text = head_font.render('業績:     $' + str(current_goal), True, (200, 255, 255))
        continue
    break

# 10關全部破關
pygame.mixer.music.stop
pygame.mixer.music.load('promote.mp3')
pygame.mixer.music.set_volume(0.7)  # 設音量
pygame.mixer.music.play(0)
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('finish')  # 命名

background = pygame.image.load('—Pngtree—cartoon superhero policeman with red_1161365.png').convert_alpha()  # 背景
background = pygame.transform.scale(background, (800, 600))
screen.blit(background, (0, 0))

pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    pygame.display.update()
