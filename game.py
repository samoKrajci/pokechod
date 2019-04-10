from easygame import *
from math import *
from random import *
from zombik import *
from bullets import *
from Player import *
from Mob import *


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
