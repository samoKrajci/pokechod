from easygame import *
from math import *

window_height = 1000
window_width = 1800

open_window('Easy Game!', window_width, window_height)
should_quit = False
set_camera(center=(window_width/2, window_height/2), position=(0, 0))

key = {}
key['UP'] = False
key['DOWN'] = False
key['LEFT'] = False
key['RIGHT'] = False


def tlacidka():
    if type(event) is KeyDownEvent:
        key[event.key] = True
    if type(event) is KeyUpEvent:
        key[event.key] = False


class Mob:
    def __init__(self, x, y, size, vel):
        self.x = x
        self.y = y
        self.size = size
        self.dead = False
        self.vel = vel

    def chase(self, target):
        x_dif = target.x-self.x
        y_dif = target.y-self.y
        x_dif /= sqrt(x_dif**2+y_dif**2+1)*self.vel
        y_dif /= sqrt(x_dif**2+y_dif**2+1)*self.vel
        self.x += x_dif
        self.y += y_dif

    def update(self):
        draw_circle(center=(self.x, self.y),
                    radius=self.size, color=(1, 0, 0, 1))


class Player:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.vel = 10

    def update(self):
        draw_circle(center=(self.x, self.y), radius=100, color=(1, 1, 1, 1))

    def move(self):
        if key['UP']:
            self.y += self.vel
        if key['DOWN']:
            self.y -= self.vel
        if key['LEFT']:
            self.x -= self.vel
        if key['RIGHT']:
            self.x += self.vel


zombik = Mob(100, 100, 100, 15)
dick = Player()

while not should_quit:
    for event in poll_events():
        if type(event) is CloseEvent:
            should_quit = True
        tlacidka()

    fill(1, 1, 0)

    zombik.chase(dick)
    zombik.update()

    dick.move()
    dick.update()

    print()

    move_camera(position=(0, 0), rotation=None, zoom=None)

    next_frame()

close_window()
