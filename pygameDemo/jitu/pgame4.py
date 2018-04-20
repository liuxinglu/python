# -*- coding: UTF-8 -*-
from datetime import datetime, date, time
import pygame, sys, random, math
from pygame.locals import *
import EventManager

class ImageButton(object):
    def __init__(self, *args):
        super(ImageButton, self).__init__(*args))
    
    def setImage(imagePath):
        icon = pygame.image.load(imagePath).convert_alpha()

        

pygame.init();
screen = pygame.display.set_mode((1136, 640));
pygame.display.set_caption("鸡兔同笼");
font = pygame.font.Font(None, 75);
black = 80, 80, 80;
bg = pygame.image.load("jitu/bg_mengWuZhiDuoShaoYouXi.png").convert_alpha();
rabit = pygame.image.load("jitu/img_tuZi.png").convert_alpha();
chicken = pygame.image.load("jitu/img_xiaoJi.png").convert_alpha();
icon_head = pygame.image.load("jitu/img_touTuBiao.png").convert_alpha();
icon_foot = pygame.image.load("jitu/img_jiaoTuBiao.png").convert_alpha();
icon_wing = pygame.image.load("jitu/img_chiBangTuBiao.png").convert_alpha();
icon_mask = pygame.image.load("jitu/img_chiBangZheZhao.png").convert_alpha();
text_head = font.render("0", True, black);
text_foot = font.render("0", True, black);
text_wing = font.render("0", True, black);
screen.blit(bg, (0, 0));
screen.blit(rabit, (100, 250));
screen.blit(chicken, (870, 250));
screen.blit(icon_head, (320, 55));
screen.blit(icon_foot, (500, 55));
screen.blit(icon_wing, (700, 55));
screen.blit(text_head, (390, 70));
screen.blit(text_foot, (570, 70));
screen.blit(text_wing, (770, 70));
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit();
            sys.exit();
    keys = pygame.key.get_pressed();
    if keys[K_ESCAPE]:
        sys.exit();
    x, y = pygame.mouse.get_pos()
    
    pygame.display.update();
