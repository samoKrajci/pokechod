from math import *
from easygame import *


def sec(a):
    return a*40


mob_cooldown = sec(5)


class Mob:
    def __init__(self, x, y, vel):
        self.x = x
        self.y = y
        self.cooldown = 0
        self.size = 50
        self.vel = vel
        self.hitbox = (self.x-self.size*sqrt(2)/2, self.y-self.size*sqrt(2)/2,
                       self.x+self.size*sqrt(2)/2, self.y+self.size*sqrt(2)/2)

    def chase(self, target):
        if self.cooldown != 0:
            self.cooldown -= 1
            return
        x_dif = target.x-self.x
        y_dif = target.y-self.y
        x_dif_new = x_dif/sqrt(x_dif**2+y_dif**2+1)*self.vel
        y_dif_new = y_dif/sqrt(x_dif**2+y_dif**2+1)*self.vel
        self.x += x_dif_new
        self.y += y_dif_new
        vect = fix_rectangle_overlap(self.hitbox, target.hitbox)
        if vect != (0, 0):
            target.hp -= 1
            self.cooldown = mob_cooldown

    def update(self):
        draw_image(load_image('img/mob.png'),
                   position=(self.x, self.y))
        self.hitbox = (self.x-self.size*sqrt(2)/2, self.y-self.size*sqrt(2)/2,
                       self.x+self.size*sqrt(2)/2, self.y+self.size*sqrt(2)/2)
