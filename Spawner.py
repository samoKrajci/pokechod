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
                   position=(self.x, self.y))
        draw_circle(center=(self.x, self.y), radius=self.size,
                    color=(0, 0, 0, 1-self.hp/self.max_hp))
        print(self.hp)
