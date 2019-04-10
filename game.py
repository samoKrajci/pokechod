from easygame import *
from math import *
from random import *
from Player import *
from Mob import *
from Spawner import *


window_height = 600
window_width = 800
map_width = 1000
map_height = 1000

open_window('Easy Game!', window_width, window_height)
should_quit = False
cam_pos = [0, 0]
set_camera(center=(window_width/2, window_height/2),
           position=(cam_pos[0], cam_pos[1]))


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


dick = Player()
spawnery = []
zombiky = []

while not should_quit:
    for event in poll_events():
        if type(event) is CloseEvent:
            should_quit = True
        if type(event) is KeyDownEvent:
            if event.key == 'P':
                spawnery.append(Spawner(randint(-map_width/2, map_width/2), randint(-map_height/2, map_height/2), 100))
        tlacidka()

    for i in zombiky:
        for j in zombiky:
            if i != j:
                separate(i, j)

    fill(1, 1, 0)
    draw_polygon((-map_width/2, -map_height/2), (map_width/2, -map_height/2),
                 (map_width/2, map_height/2), (-map_width/2, map_height/2), color=(0, 1, 0, 1))
    hud()

    for i in spawnery:
        i.update()
        if randint(0, 1000) < 5:
            zombiky.append(Mob(i.x, i.y, 2.8, 10))

    for i in zombiky:
        i.chase(dick)
        i.update()

    for i in spawnery:
        if sqrt((dick.x-i.x)**2 + (dick.y-i.y)**2) < dick.size+i.size:
            i.hp -= 1

    dick.move()
    dick.update()
    move_camera(position=(0, 0), rotation=None, zoom=None)
    next_frame()

close_window()
