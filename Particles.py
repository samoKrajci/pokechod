from easygame import *
from math import *


class Tree:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = 30
        self.hitbox = (self.x-self.size*sqrt(2)/2, self.y-self.size*sqrt(2)/2,
                       self.x+self.size*sqrt(2)/2, self.y+self.size*sqrt(2)/2)

    def update(self):
        draw_image(load_image('img/strom.png'),
                   position=((self.x, self.y)))


class Rock:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = 130
        self.hitbox = (self.x-self.size*sqrt(2)/2, self.y-self.size*sqrt(2)/2,
                       self.x+self.size*sqrt(2)/2, self.y+self.size*sqrt(2)/2)

    def update(self):
        draw_image(load_image('img/suter.png'),
                   position=((self.x, self.y)))
