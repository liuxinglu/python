# -*- coding: UTF-8 -*-
import pygame
import math
from pygame.locals import *
pygame.init();

screen = pygame.display.set_mode((600, 500));
pygame.display.set_caption("Drawing Rect");
pos_x = 300;
pos_y = 250;
vel_x = 2;
vel_y = 1;
# myfont = pygame.font.Font(None, 60)
white = 255, 255, 255
blue = 0, 0, 200;
# textImage = myfont.render("hello pygame", True, white)
while True:
    for event in pygame.event.get():
        if event.type in (QUIT, KEYDOWN):
            pygame.quit();
            exit();
            break;
    screen.fill(blue);
    # screen.blit(textImage, (100, 100))
    pos_x += vel_x;
    pos_y += vel_y;
    if pos_x > 500 or pos_x < 0:
        vel_x = -vel_x;
    if pos_y > 400 or pos_y < 0:
        vel_y = -vel_y;
    width = 0;
    pos = pos_x, pos_y, 100, 100;
    pygame.draw.rect(screen, white, pos, width)
    # pygame.draw.line(screen, white, (100, 100), (500, 400), 3)
    color = 255, 0, 255;
    position = 200, 150, 200, 200;
    start_angle = math.radians(0);
    end_angle = math.radians(180);
    width = 10;
    pygame.draw.arc(screen, color, position, start_angle, end_angle, width);
    
    pygame.display.update();