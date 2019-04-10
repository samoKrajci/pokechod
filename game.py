from easygame import *
from math import *

window_height = 1000
window_width = 1800

open_window('Easy Game!', window_width, window_height)
should_quit = False
set_camera(center=(window_width/2, window_height/2), position=(0, 0))

key = {}
key['W'] = False
key['S'] = False
key['A'] = False
key['D'] = False


def tlacidka():
    if type(event) is KeyDownEvent:
        key[event.key] = True
    if type(event) is KeyUpEvent:
        key[event.key] = False


class Mob:
    def __init__(self, x, y, vel):
        self.x = x
        self.y = y
        self.dead = False
        self.vel = vel

    def chase(self, target):
        x_dif = target.x-self.x
        y_dif = target.y-self.y
        x_dif_new = x_dif/sqrt(x_dif**2+y_dif**2+1)*self.vel
        y_dif_new = y_dif/sqrt(x_dif**2+y_dif**2+1)*self.vel
        self.x += x_dif_new
        self.y += y_dif_new

    def update(self):
        if self.x == dick.x and self.y == dick.y:
            return
        angle = atan2((self.y-dick.y), (self.x-dick.x))-degrees(90)
        draw_image(load_image('img/zombie.png'), position=(self.x, self.y), scale=1, rotation=angle, opacity=1)


class Player:
    def __init__(self, vel):
        self.x = 0
        self.y = 0
        self.vel = vel

    def update(self):
        draw_circle(center=(self.x, self.y), radius=50, color=(1, 1, 1, 1))

    def move(self):
        if key['W']:
            self.y += self.vel
        if key['S']:
            self.y -= self.vel
        if key['A']:
            self.x -= self.vel
        if key['D']:
            self.x += self.vel


zombik = Mob(100, 100, 1)
dick = Player(3)

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

    move_camera(position=(0, 0), rotation=None, zoom=None)

    next_frame()

close_window()
