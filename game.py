from easygame import *
from math import *
from random import *

window_height = 600
window_width = 1000
map_width = 1000
map_height = 600
open_window('Easy Game!', window_width, window_height)
should_quit = False
cam_pos = [0, 0]
set_camera(center=(window_width/2, window_height/2),
           position=(cam_pos[0], cam_pos[1]))
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
        draw_image(load_image('img/zombie_lvl1.png'), position=(self.x, self.y), scale=0.15, opacity=1)


class Player:
    def __init__(self, vel):
        self.x = 0
        self.y = 0
        self.vel = vel

    def update(self):
        draw_circle(center=(self.x, self.y), radius=50, color=(1, 1, 1, 1))

    def move(self):
        if key['UP']:
            self.y += self.vel
        if key['DOWN']:
            self.y -= self.vel
        if key['LEFT']:
            self.x -= self.vel
        if key['RIGHT']:
            self.x += self.vel


spawnery = []
zombiky = []
dick = Player(3)

while not should_quit:
    for event in poll_events():
        if type(event) is CloseEvent:
            should_quit = True
        if type(event) is KeyDownEvent:
            if event.key == 'P':
                spawnery.append([randint(-map_width, map_width), randint(-map_height, map_height)])
        tlacidka()

    fill(1, 1, 0)
    draw_polygon((-map_width/2, -map_height/2), (map_width/2, -map_height/2), (map_width/2, map_height/2), (-map_width/2, map_height/2), color=(0, 1, 0, 1))

    for i in spawnery:
        draw_circle(center=(i[0], i[1]),
                    radius=20, color=(1, 1, 0, 1))
        if randint(0, 1000) < 5:
            zombiky.append(Mob(i[0], i[1], 100, 1))

    for i in zombiky:
        i.chase(dick)
        i.update()

    dick.move()
    dick.update()

    move_camera(position=(0, 0), rotation=None, zoom=None)

    next_frame()

close_window()
