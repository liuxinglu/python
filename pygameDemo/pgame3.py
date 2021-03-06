# -*- coding: UTF-8 -*-
import sys
import random
import time
import pygame
from pygame.locals import *

def print_text(font, x, y, text, color=(255, 255, 255)):
    imgText = font.render(text, True, color);
    screen.blit(imgText, (x, y));
    

pygame.init();
screen = pygame.display.set_mode((600, 500));
pygame.display.set_caption("keyboard Demo");
font1 = pygame.font.Font(None, 24);
font2 = pygame.font.Font(None, 200);
white = 255, 255, 255;
yellow = 255, 255, 0;
color = 125, 100, 210;
key_flag = False;
correct_answer = 97;
seconds = 10;
score = 0;
clock_start = 0;
game_start = True;

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit();
            sys.exit();
        elif event.type == KEYDOWN:
            key_flag = True;
        elif event.type == KEYUP:
            key_flag = False;
    keys = pygame.key.get_pressed();
    if keys[K_ESCAPE]:
        sys.exit();
    if keys[K_RETURN]:
        if game_start:
            game_start = False;
            score = 0;
            seconds = 11;
            clock_start = time.clock();
    current = time.clock() - clock_start;
    speed = score * 6;
    if seconds - current < 0:
        game_start = True;
    elif current:
        if keys[correct_answer]:
            correct_answer = random.randint(97, 122);
            score += 1;

    screen.fill(color);
    print_text(font1, 0, 20, "Try to keep for 10 seconds.");

    if key_flag:
        print_text(font1, 450, 0, "you are keying.");
    if game_start:
        print_text(font1, 0, 80, "Time: " + str(int(seconds - current)));
    
    print_text(font1, 0, 100, "Speed: " + str(speed) + "letters/min");

    if game_start:
        print_text(font2, 0, 240, chr(correct_answer - 32), yellow);
    pygame.display.update();