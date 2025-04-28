import bullet
import pygame

class Player:
    def __init__(self, position, radius):
        self.pos = position
        self.rad = radius

    def move_x(self, val):
        self.pos.x += val

    def move_y(self, val):
        self.pos.y += val

    def collision(self, bullet):
        above = abs(self.pos.y - bullet.top) < 15
        below = abs(bullet.top - self.pos.y) < 10
        left = abs(self.pos.x - bullet.left) < 15
        right = abs(bullet.left - self.pos.x) < 10
        if (left or right) and (below or above):
            print('COLLISION DTECTED')
            pygame.quit()


    