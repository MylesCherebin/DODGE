import pygame
import random

class Bullet:
    def __init__(self,player_position,x,y):
        self.goal_x = player_position.x
        self.goal_y = player_position.y
        self.left = x
        self.top = y
        self.rect = pygame.Rect(self.left,self.top,5,5)
        self.dist_x = player_position.x - self.left
        self.dist_y = player_position.y - self.top
        self.speed_x = self.dist_x / 50
        self.speed_y = self.dist_y / 50

    def move(self):
       self.rect = self.rect.move(self.speed_x,self.speed_y)