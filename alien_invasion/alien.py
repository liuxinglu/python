import pygame
import random
from pygame.sprite import Sprite


class Alien(Sprite):
    """docstring for Alien"""

    def __init__(self, game_setting, screen):
        super(Alien, self).__init__()
        self.screen = screen
        self.game_setting = game_setting
        self.image = pygame.image.load('images/外星飞船.png').convert_alpha()
        self.width, self.height = self.image.get_size()
        self.image = pygame.transform.smoothscale(self.image, (self.width // 2, self.height // 2))
        self.rect = self.image.get_rect()
        # self.width,self.height = self.image.get_size()
        # self.width == self.width // 20
        # self.height == self.height // 20
        # self.image = pygame.transform.smoothscale(self.image,(self.width,self.height))
        # self.rect.width = self.rect.width // 30
        # self.rect.height = self.rect.height // 30
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.health = 0;

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        ranfactor = random.randint(1, 3)
        self.y += (self.game_setting.alien_speed_factor * ranfactor)
        self.rect.y = self.y

    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True
