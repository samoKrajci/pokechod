from math import *
from easygame import *


class Bullet:
    def __init__(self, x, y, mx, my, vel=10):
        self.x = x
        self.y = y
        self.vel = vel
        self.size = 4
        x_dif = mx - self.x
        y_dif = my - self.y
        self.x_dif_new = x_dif / sqrt(x_dif ** 2 + y_dif ** 2 + 1) * self.vel
        self.y_dif_new = y_dif / sqrt(x_dif ** 2 + y_dif ** 2 + 1) * self.vel

    def update(self):
        self.x += self.x_dif_new
        self.y += self.y_dif_new
        draw_circle(center=(self.x, self.y),
                    radius=self.size, color=(0, 0, 0, 1))
