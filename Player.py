from easygame import *
from math import *


key = {}
key['W'] = False
key['S'] = False
key['A'] = False
key['D'] = False


class Player:
    def __init__(self, size, vel, hp):
        self.x = 0
        self.y = 0
        self.vel = vel
        self.size = size
        self.hp = hp
        self.hitbox = (self.x-self.size*sqrt(2)/2, self.y-self.size*sqrt(2)/2,
                       self.x+self.size*sqrt(2)/2, self.y+self.size*sqrt(2)/2)

    def update(self):
        draw_circle(center=(self.x, self.y),
                    radius=self.size, color=(0, 0, 1, 1))
        self.hitbox = (self.x-self.size*sqrt(2)/2, self.y-self.size*sqrt(2)/2,
                       self.x+self.size*sqrt(2)/2, self.y+self.size*sqrt(2)/2)

    def move(self):
        if key['W']:
            self.y += self.vel
        if key['S']:
            self.y -= self.vel
        if key['A']:
            self.x -= self.vel
        if key['D']:
            self.x += self.vel
