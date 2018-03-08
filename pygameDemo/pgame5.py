# -*- coding: UTF-8 -*-
import sys
import random
import pygame
import time
from pygame.locals import *

def print_text(font, x, y, text, color=(25, 25, 255)):
    imgText = font.render(text, True, color)
    screen.blit(imgText, (x, y))

pygame.init()
screen = pygame.display.set_mode((600, 500))
pygame.display.set_caption("Ball Demo")
font1 = pygame.font.Font(None, 24)
font2 = pygame.font.Font(None, 200)
white = 255, 255, 255
yellow = 255, 255, 0
color = 125, 100, 210
game_over = False
lives = 3
score = 0
pos_x, pos_y = 300, 460
bomb_x, bomb_y = random.randint(0, 500), -50
vel_y = 4

while True:
    while game_over != True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEMOTION:
                pos_x, _ = event.pos
            elif event.type == MOUSEBUTTONUP:
                if game_over == True:
                    game_over = False
                    lives = 3
                    score = 0
        keys = pygame.key.get_pressed()
        if keys[K_ESCAPE]:
            pygame.quit()
            sys.exit()
        elif keys[K_RIGHT]:
            pos_x += 10
        elif keys[K_LEFT]:
            pos_x -= 10
        screen.fill(white)      

        if pos_x < 0:
            pos_x = 0
        elif pos_x > 500:
            pos_x = 500
        pygame.draw.rect(screen, (30, 0, 0), (pos_x, pos_y, 120, 40), 0)

        bomb_y += vel_y
        # time.sleep(0.1)
        if bomb_y > 500:
            bomb_x = random.randint(0, 500)
            bomb_y = -50
            lives -= 1
            vel_y = random.randint(3, 6)
            if lives == 0:
                game_over = True
        elif bomb_y > pos_y:
            if bomb_x > pos_x and bomb_x < pos_x + 120:
                score += 1
                bomb_x = random.randint(0, 500)
                bomb_y = -50
                vel_y = 4 + score/10
        pygame.draw.circle(screen, ((score * 3 + 80) % 255, (score * 3 + 80) % 255, (score + 10) % 255), (bomb_x, bomb_y), 30, 0)
        print_text(font1, 0, 0, "LIVES:" + str(lives))
        print_text(font1, 500, 0, "SCORE:" + str(score))
        pygame.display.update()  
    
    for event in pygame.event.get():
        if event.type == MOUSEBUTTONUP:
            game_over = False
            lives = 3
            score = 0
    screen.fill(yellow)
    print_text(font1, 200, 300, '<CLICK TO PLAY>')
    pygame.display.update()
