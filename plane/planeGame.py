import pygame
import time
from pygame.locals import *
import random

class BasePlane(object):
    '''飞机类'''
    def __init__(self,screen_temp,x,y,image_name):
        self.x = x
        self.y = y
        self.screen = screen_temp  #游戏窗口
        self.image = pygame.image.load(image_name)
        self.bullet_list = []    #存储发射出去的子弹

    def display(self):
        # 加载飞机到窗口
        self.screen.blit(self.image,(self.x,self.y))
        #控制子弹
        for bullet in self.bullet_list:
            bullet.display()
            bullet.move()
            if bullet.judge():   #判断子弹是否越界
                self.bullet_list.remove(bullet)

class HeroPlane(BasePlane):
    '''玩家飞机'''
    def __init__(self,screen_temp):
        BasePlane.__init__(self,screen_temp,210,700,'resources/image/hero1.png')

    def move_left(self):
        self.x -= 5

    def move_right(self):
        self.x += 5

    def fire(self):
        #发射子弹
        self.bullet_list.append(Bullet(self.screen,self.x,self.y))

class EnemyPlane(BasePlane):
    '''敌方飞机'''
    def __init__(self, screen_temp):
        BasePlane.__init__(self, screen_temp, 0, 0, 'resources/image/enemy0.png')
        self.direction = 'right'     #定义敌机默认往右移动

    def move(self):
        if self.direction == 'right':
            self.x += 8
        elif self.direction == 'left':
            self.x -= 8

        if self.x > 430:
            self.direction = 'left'
        elif self.x < 0:
            self.direction = 'right'

    def fire(self):
        # 发射子弹
        random_num = random.randint(1,50)
        if random_num == 10 or random_num == 40:
            self.bullet_list.append(EnemyBullet(self.screen,self.x,self.y))

class BaseBullet(object):
    '''子弹类'''
    def __init__(self,screen_temp,x,y,image_name):
        self.x = x
        self.y = y
        self.screen = screen_temp
        self.image = pygame.image.load(image_name)

    def display(self):
        self.screen.blit(self.image,(self.x,self.y))

class Bullet(BaseBullet):
    '''玩家子弹'''
    def __init__(self,screen_temp,x,y):
        BaseBullet.__init__(self,screen_temp,x+40,y-20,'resources/image/bullet.png')

    def move(self):
        self.y -= 20

    def judge(self):
        if self.y < 0:
            return True
        else:
            return False

class EnemyBullet(BaseBullet):
    '''敌机子弹'''
    def __init__(self,screen_temp,x,y):
        BaseBullet.__init__(self, screen_temp, x + 25, y + 40, 'resources/image/bullet1.png')

    def move(self):
        self.y += 10

    def judge(self):
        if self.y > 852:
            return True
        else:
            return False

def key_control(hero_temp):
    for event in pygame.event.get():
        # 判断是否是点击了退出按钮
        if event.type == QUIT:
            print("exit")
            exit()
        # 判断是否是按下了键
        elif event.type == KEYDOWN:
            if event.key == K_a or event.key == K_LEFT:
                print('left')
                hero_temp.move_left()

            elif event.key == K_d or event.key == K_RIGHT:
                print('right')
                hero_temp.move_right()
            elif event.key == K_SPACE:
                print('space')
                hero_temp.fire()

def main():
    #1.创建窗口
    screen = pygame.display.set_mode((480,852),0,0)
    #2 创建一个背景图片
    background = pygame.image.load('resources/image/background.png')
    #3 创建一个飞机对象
    hero = HeroPlane(screen)
    #4 创建一个敌机对象
    enemy = EnemyPlane(screen)

    while True:
        #把背景图片放到窗口显示
        screen.blit(background,(0,0))
        #显示玩家飞机到定义的（x,y）坐标位置
        hero.display()      #显示玩家飞机
        enemy.display()     #显示敌机
        enemy.move()        #玩家飞机移动
        enemy.fire()        #玩家飞机发射子弹
        pygame.display.update()    #刷新
        #检测键盘，控制玩家飞机移动
        key_control(hero)
        time.sleep(0.05)

if __name__ == '__main__':
    main()