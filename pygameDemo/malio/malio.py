# coding:utf-8
import pygame
from pygame.locals import *
import sys
global malioX, malioY
class malio:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((960, 720), 0, 32)
        self.background = pygame.image.load("assets/bg.png").convert()
        self.malio = pygame.image.load(u"assets/马里奥-右-1.png").convert_alpha()
        malioX = 480
        malioY = 50
        self.move_x, self.move_y = 0, 0
        self.bottomIsWall = 0
        self.leftIsWall = 0
        self.rightIsWall = 0
        self.topIsWall = 0
        self.verticalSpeed = 0
        self.isMove = 0
        self.gravity = 1
        self.f = floor()

    def malioMove(self):
        if self.topIsWall == 1:
            self.verticalSpeed = 0
            malioY = (malioY // 64) * 64
        if self.rightIsWall == 0:
            pass
        keys = pygame.key.get_pressed()
        if self.leftIsWall == 0 and keys[K_LEFT]:
            self.isMove = 1
            self.move_x -= 4
        if self.rightIsWall == 0 and keys[K_RIGHT]:
            self.isMove = 1
            self.move_x += 4
        if self.bottomIsWall == 0:
            self.malioY += self.verticalSpeed
            self.verticalSpeed += self.gravity
            if self.verticalSpeed < -8:
                self.verticalSpeed = -8
        else:
            self.malioY = (self.malioY // 64) * 64
            if keys[K_UP]:
                self.verticalSpeed = 15


    def exe(self):
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    sys.exit()
            self.malioMove()
            self.f.exe(self.screen, self.move_x)
            self.screen.blit(self.background, (0, 0))
            self.screen.blit(self.f.floor, (self.f.x, self.f.floor_originY))
            self.screen.blit(self.malio, (self.malioX, self.malioY))
            pygame.display.update()
            self.topIsWall = self.leftIsWall = self.rightIsWall = self.bottomIsWall = self.isMove = 0

class floor:
    x_, y_ = 0, 0
    def __init__(self):
        self.floor_originX, self.floor_originY = 400, 640
        self.floor = pygame.image.load("assets/floor5.png").convert_alpha()
        self.x, self.y = 0, 0

    def exe(self, screen, move_x):
        self.x = self.floor_originX - move_x
        abs()



if __name__ == '__main__':
    m = malio()
    m.exe()