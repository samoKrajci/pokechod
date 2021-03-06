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
        self.vel = vel+2
        self.dead = False
        self.frozen = 0
        self.hitbox = (self.x-self.size*sqrt(2)/2, self.y-self.size*sqrt(2)/2,
                       self.x+self.size*sqrt(2)/2, self.y+self.size*sqrt(2)/2)

    def chase(self, target, bullets):
        if self.frozen == 0:
            if self.cooldown != 0:
                self.cooldown -= 1
                for i in bullets:
                    vect = fix_rectangle_overlap(self.hitbox, i.hitbox)
                    if vect != (0, 0):
                        i.gone = True
                        self.dead = True
                        break
                return
            x_dif = target.x-self.x
            y_dif = target.y-self.y
            x_dif_new = x_dif/sqrt(x_dif**2+y_dif**2+1)*self.vel
            y_dif_new = y_dif/sqrt(x_dif**2+y_dif**2+1)*self.vel
            self.x += x_dif_new
            self.y += y_dif_new
        else:
            self.frozen -= 1
            return
        vect = fix_rectangle_overlap(self.hitbox, target.hitbox)
        if vect != (0, 0):
            target.hp -= 1
            self.cooldown = mob_cooldown
        for i in bullets:
            vect = fix_rectangle_overlap(self.hitbox, i.hitbox)
            if vect != (0, 0):
                i.gone = True
                self.dead = True
                break

    def update(self, dickX, dickY):
        angle = atan2((self.y - dickY), (self.x - dickX)) + degrees(90)
        draw_image(load_image('img/mob.png'),
                   position=(self.x, self.y), rotation=angle)
        self.hitbox = (self.x-self.size*sqrt(2)/2, self.y-self.size*sqrt(2)/2,
                       self.x+self.size*sqrt(2)/2, self.y+self.size*sqrt(2)/2)
