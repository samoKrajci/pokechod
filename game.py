from easygame import *
from math import *
from random import *
from zombik import *
from bullets import *


def sec(a):
    return a*40


window_height = 1000
window_width = 1000
map_width = 1000
map_height = 1000
mob_cooldown = sec(5)

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


def hud():
    draw_text("HP: " + str(dick.hp), 'Fixedsys', 32, position=(
        cam_pos[0]-window_width/2+10, cam_pos[1]-window_height/2+10), color=(0, 0, 0, 1))


def separate(a, b):
    dif = fix_rectangle_overlap(a.hitbox, b.hitbox)
    a.x += dif[0]
    a.y += dif[1]


class Mob:
    def __init__(self, x, y, vel, size):
        self.x = x
        self.y = y
        self.cooldown = 0
        self.size = size
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
        draw_circle(center=(self.x, self.y),
                    radius=self.size, color=(0, 0, 0, 1))
        self.hitbox = (self.x-self.size*sqrt(2)/2, self.y-self.size*sqrt(2)/2,
                       self.x+self.size*sqrt(2)/2, self.y+self.size*sqrt(2)/2)


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
        if key['UP']:
            self.y += self.vel
        if key['DOWN']:
            self.y -= self.vel
        if key['LEFT']:
            self.x -= self.vel
        if key['RIGHT']:
            self.x += self.vel


dick = Player(30, 5, 10)
spawnery, zombiky, bullets = [], [], []
mouseX, mouseY, frameCount = 0, 0, 0
while not should_quit:
    for event in poll_events():
        if type(event) is CloseEvent:
            should_quit = True
        if type(event) is KeyDownEvent:
            if event.key == 'P':
                spawnery.append([randint(-map_width/2, map_width/2),
                                 randint(-map_height/2, map_height/2)])
        if type(event) is MouseMoveEvent:
            mouseX = event.x
            mouseY = event.y
        tlacidka()
    if frameCount == sec(0.7):
        bullets.append(Bullet(dick.x, dick.y, mouseX, mouseY))
        frameCount = 0
    else:
        frameCount += 1

    for i in zombiky:
        for j in zombiky:
            if i != j:
                separate(i, j)

    fill(1, 1, 0)

    draw_polygon((-map_width/2, -map_height/2), (map_width/2, -map_height/2),
                 (map_width/2, map_height/2), (-map_width/2, map_height/2), color=(0, 1, 0, 1))
    hud()

    for i in spawnery:
        draw_circle(center=(i[0], i[1]),
                    radius=20, color=(1, 1, 0, 1))
        if randint(0, 1000) < 5:
            zombiky.append(Mob(i[0], i[1], 3, 10))

    for i in bullets:
        i.update()

    for i in zombiky:
        i.chase(dick)
        i.update()

    dick.move()
    dick.update()

    move_camera(position=(0, 0), rotation=None, zoom=None)

    next_frame()

close_window()
