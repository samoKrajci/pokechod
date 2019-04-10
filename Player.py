from easygame import *
from math import *


def check(x, y, x2, y2):
    if x > x2/2 or x < -x2/2 or y > y2/2 or y < -y2/2:
        return True
    return False


def sec(a):
    return a*40


key = {'W': False, 'S': False, 'A': False, 'D': False}


class Player:
    def __init__(self, mw, mh):
        self.x = 0
        self.y = 0
        self.mw = mw
        self.mh = mh
        self.vel = 5
        self.startingVel = 5
        self.size = 30
        self.hp = 5
        self.turbo = 0
        self.hitbox = (self.x-self.size*sqrt(2)/2, self.y-self.size*sqrt(2)/2,
                       self.x+self.size*sqrt(2)/2, self.y+self.size*sqrt(2)/2)
        self.cooldowns = {'turbo': 15, 'ability2': 20, 'ability3': 30}
        self.dead = False

    def update(self, mouseX, mouseY):
        if self.hp <= 0:
            self.dead = True
        angle = atan2((self.y - mouseY),
                      (self.x - mouseX)) + pi/2
        self.turbo -= 1
        if self.turbo > 0:
            self.vel = self.startingVel * 2
        else:
            self.vel = self.startingVel
        draw_image(load_image('img/hrac.png'),
                   position=(self.x, self.y), rotation=angle)
        self.hitbox = (self.x-self.size*sqrt(2)/2, self.y-self.size*sqrt(2)/2,
                       self.x+self.size*sqrt(2)/2, self.y+self.size*sqrt(2)/2)

    def move(self):
        if key['W'] and not check(self.x, self.y + self.vel, self.mw, self.mh):
            self.y += self.vel
        if key['S'] and not check(self.x, self.y - self.vel, self.mw, self.mh):
            self.y -= self.vel
        if key['A'] and not check(self.x - self.vel, self.y, self.mw, self.mh):
            self.x -= self.vel
        if key['D'] and notcheck(self.x + self.vel, self.y, self.mw, self.mh):
            self.x += self.vel

    def set_turbo(self):
        self.turbo = sec(4)
