from easygame import *


class Spawner:
    def __init__(self, x, y, hp):
        self.x = x
        self.y = y
        self.size = 20
        self.hp = hp

    def update(self):
        if self.hp > 0:
            draw_circle(center=(self.x, self.y), radius=self.size, color=(1/(101-self.hp), 0, 0, 1))