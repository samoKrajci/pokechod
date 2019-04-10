from easygame import *
from math import *


def sec(a):
    return a*40


key = {'W': False, 'S': False, 'A': False, 'D': False}


class Player:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.vel = 5
        self.startingVel = 5
        self.size = 30
        self.hp = 10
        self.turbo = 0
        self.hitbox = (self.x-self.size*sqrt(2)/2, self.y-self.size*sqrt(2)/2,
                       self.x+self.size*sqrt(2)/2, self.y+self.size*sqrt(2)/2)
        self.cooldowns = {'ability1': 5, 'ability2': 10, 'ability3': 30}

    def update(self, mouseX, mouseY, window_width, window_height):
        angle = atan2((self.y - mouseY),
                      (self.x - mouseX)) + pi/2
        #angle = 0
        self.turbo -= 1
        if self.turbo > 0:
            self.vel = self.startingVel * 2
        else:
            self.vel = self.startingVel
        draw_image(load_image('img/hrac.png'),
                   position=((self.x, self.y)), rotation=angle)
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

    def set_turbo(self):
        self.turbo = sec(4)
