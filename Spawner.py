from easygame import *


class Spawner:
    def __init__(self, x, y, hp):
        self.x = x
        self.y = y
        self.size = 90
        self.hp = hp
        self.max_hp = hp

    def update(self):
        draw_image(load_image('img/spawner.png'),
                   position=(self.x, self.y), opacity=self.hp/self.max_hp)
