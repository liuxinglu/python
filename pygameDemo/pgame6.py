# -*- coding: UTF-8 -*-
import sys
import math
import random
import pygame
from pygame.locals import *
from datetime import datetime, date, time

def print_text(font, x, y, text, color=(25, 25, 255)):
    imgText = font.render(text, True, color)
    screen.blit(imgText, (x, y))

def wrap_angle(angle):
    return angle % 360

pygame.init()
screen = pygame.display.set_mode((600, 500))
pygame.display.set_caption("Clock Demo")
font = pygame.font.Font(None, 36)
orange = 220, 180, 0
white = 255, 255, 255
yellow = 255, 255, 0
pink = 255, 100, 100
pos_x, pos_y = 300, 250
radius = 250
angle = 360
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
    keys = pygame.key.get_pressed()
    if keys[K_ESCAPE]:
        sys.exit()
    screen.fill((0, 0, 100))
    pygame.draw.circle(screen, white, (pos_x, pos_y), radius, 6)
    for n in range(1, 13):
        angle = math.radians(n * (360 / 12) - 90)
        x = math.cos(angle) * (radius - 20) - 10
        y = math.sin(angle) * (radius - 20) - 10
        print_text(font, pos_x + x, pos_y + y, str(n))
    today = datetime.today()
    hours = today.hour % 12
    minutes = today.minute
    seconds = today.second

    hour_angle = math.radians(wrap_angle(hours * (360 / 12) - 90))
    hour_x = math.cos(hour_angle) * (radius - 80)
    hour_y = math.sin(hour_angle) * (radius - 80)
    target = (pos_x + hour_x, pos_y + hour_y)
    pygame.draw.line(screen, pink, (pos_x, pos_y), target, 25)
    min_angle = math.radians(wrap_angle(minutes * (360 /  60) - 90))
    min_x = math.cos(min_angle) * (radius - 60)
    min_y = math.sin(min_angle) * (radius - 60)
    target = (pos_x + min_x, pos_y + min_y)
    pygame.draw.line(screen, orange, (pos_x, pos_y), target, 12)
    sec_angle = math.radians(wrap_angle(seconds * (360 / 60) - 90))
    sec_x = math.cos(sec_angle) * (radius - 40)
    sec_y = math.sin(sec_angle) * (radius - 40)
    target = (pos_x + sec_x, pos_y + sec_y)
    pygame.draw.line(screen, yellow, (pos_x, pos_y), target, 6)
    print_text(font, 0, 0, str(hours) + ":" + str(minutes) + ":" + str(seconds))
    pygame.display.update()
        
