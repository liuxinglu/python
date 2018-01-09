# -*- coding: UTF-8 -*-
import pygame
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((600, 500))
pygame.display.set_caption("The Mouse")
mouse_x, mouse_y = 0, 0;
move_x, move_y = 0, 0;
mouse_flag = 0;
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit();
        if event.type == MOUSEBUTTONDOWN:
            mouse_flag = 1;
        if event.type == MOUSEBUTTONUP:
            mouse_flag = 0;
        if mouse_flag == 1:
            if event.type == MOUSEMOTION:
                mouse_x, mouse_y = event.pos;
                move_x, move_y = event.rel;
                print mouse_x,mouse_y,move_x,move_y;
    pygame.display.update();
