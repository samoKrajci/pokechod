from easygame import *
from math import *


key = {}
key['W'] = False
key['S'] = False
key['A'] = False
key['D'] = False


class Player:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.vel = 5
        self.size = 30
        self.hp = 10
        self.hitbox = (self.x-self.size*sqrt(2)/2, self.y-self.size*sqrt(2)/2,
                       self.x+self.size*sqrt(2)/2, self.y+self.size*sqrt(2)/2)
        self.cooldowns = {'ability1': 5, 'ability2': 10, 'ability3': 30}

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
