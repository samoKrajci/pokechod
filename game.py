from easygame import *
from math import *
from random import *

window_height = 1000
window_width = 1000
map_width = 1000
map_height = 1000
open_window('Easy Game!', window_width, window_height)
should_quit = False
cam_pos = [0, 0]
set_camera(center=(window_width/2, window_height/2),
           position=(cam_pos[0], cam_pos[1]))
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


def hud():
    draw_text("HP: " + str(dick.hp), 'Fixedsys', 32, position=(
        cam_pos[0]-window_width/2+10, cam_pos[1]-window_height/2+10), color=(0, 0, 0, 1))


class Mob:
    def __init__(self, x, y, vel):
        self.x = x
        self.y = y
        self.dead = False
        self.vel = vel
        self.hitbox = (self.x-self.size*sqrt(2)/2, self.y-self.size*sqrt(2)/2,
                       self.x+self.size*sqrt(2)/2, self.y+self.size*sqrt(2)/2)

    def chase(self, target):
        x_dif = target.x-self.x
        y_dif = target.y-self.y
        x_dif_new = x_dif/sqrt(x_dif**2+y_dif**2+1)*self.vel
        y_dif_new = y_dif/sqrt(x_dif**2+y_dif**2+1)*self.vel
        self.x += x_dif_new
        self.y += y_dif_new

    def attack(self, player):
        vect = fix_rectangle_overlap(self.hitbox, player.hitbox)
        print(vect)
        if vect != (0, 0):
            player.hp -= 1

    def update(self):
        if self.x == dick.x and self.y == dick.y:
            return
        angle = atan2((self.y-dick.y), (self.x-dick.x))-degrees(90)
        draw_image(load_image('img/zombie.png'), position=(self.x, self.y), scale=1, rotation=angle, opacity=1)
        self.hitbox = (self.x - self.size * sqrt(2) / 2, self.y - self.size * sqrt(2) / 2,
                       self.x + self.size * sqrt(2) / 2, self.y + self.size * sqrt(2) / 2)

class Player:
    def __init__(self, size, vel, hp):
        self.x = 0
        self.y = 0
        self.vel = vel
        self.size = size
        self.hp = hp
        self.hitbox = (self.x-self.size*sqrt(2)/2, self.y-self.size*sqrt(2)/2,
                       self.x+self.size*sqrt(2)/2, self.y+self.size*sqrt(2)/2)

    def update(self):
        draw_circle(center=(self.x, self.y),
                    radius=self.size, color=(0, 0, 1, 1))
        self.hitbox = (self.x-self.size*sqrt(2)/2, self.y-self.size*sqrt(2)/2,
                       self.x+self.size*sqrt(2)/2, self.y+self.size*sqrt(2)/2)

    def move(self):
        if key['W']:
            self.y += self.vel
        if key['S']:
            self.y -= self.vel
        if key['A']:
            self.x -= self.vel
        if key['D']:
            self.x += self.vel


dick = Player(30, 3, 10)
spawnery = []
zombiky = []

while not should_quit:
    for event in poll_events():
        if type(event) is CloseEvent:
            should_quit = True
        if type(event) is KeyDownEvent:
            if event.key == 'P':
                spawnery.append([randint(-map_width/2, map_width/2),
                                 randint(-map_height/2, map_height/2)])
        tlacidka()

    fill(1, 1, 0)

    draw_polygon((-map_width/2, -map_height/2), (map_width/2, -map_height/2),
                 (map_width/2, map_height/2), (-map_width/2, map_height/2), color=(0, 1, 0, 1))
    hud()

    for i in spawnery:
        draw_circle(center=(i[0], i[1]),
                    radius=20, color=(1, 1, 0, 1))
        if randint(0, 1000) < 5:
            zombiky.append(Mob(i[0], i[1], 3, 10))

    for i in zombiky:
        i.chase(dick)
        i.update()

    dick.move()
    dick.update()

    move_camera(position=(0, 0), rotation=None, zoom=None)

    next_frame()

close_window()
