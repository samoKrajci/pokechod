from easygame import *
from math import *
from random import *
from Bullet import *
from Player import *
from Mob import *
from Spawner import *


window_width = 800
window_height = 600
map_width = 800
map_height = 600

open_window('Easy Game!', window_width, window_height)
should_quit = False
cam_pos = [0, 0]
set_camera(center=(window_width/2, window_height/2),
           position=(cam_pos[0], cam_pos[1]))
dick = Player()
spawnery, zombiky, bullets = [], [], []
mouseX, mouseY, frameCount = 0, 0, 0


def check(x, y):
    if x > map_width/2 or x < -map_width/2 or y > map_height/2 or y < -map_height/2:
        return True
    return False


def tlacidka():
    if type(event) is KeyDownEvent:
        key[event.key] = True
        if event.key == 'P':
            spawnery.append(Spawner(
                randint(-map_width / 2, map_width / 2), randint(-map_height / 2, map_height / 2), 1000))
    if type(event) is KeyUpEvent:
        key[event.key] = False


def hud():
    draw_text("HP: " + str(dick.hp), 'Fixedsys', 20, position=(
        cam_pos[0]-window_width/2+10, cam_pos[1]-window_height/2+10), color=(0, 0, 0, 1))
    draw_text("Ability 1:  " + str(dick.cooldowns['ability1']), 'Fixedsys', 20, position=(
        cam_pos[0]-window_width/2+window_width/4, cam_pos[1]-window_height/2+10), color=(0, 0, 0, 1))
    draw_text("Ability 2:  " + str(dick.cooldowns['ability2']), 'Fixedsys', 20, position=(
        cam_pos[0]-window_width/2+window_width/2, cam_pos[1]-window_height/2+10), color=(0, 0, 0, 1))
    draw_text("Ability 3:  " + str(dick.cooldowns['ability3']), 'Fixedsys', 20, position=(
        cam_pos[0]-window_width/2+3*window_width/4, cam_pos[1]-window_height/2+10), color=(0, 0, 0, 1))


def separate(a, b):
    dif = fix_rectangle_overlap(a.hitbox, b.hitbox)
    a.x += dif[0]
    a.y += dif[1]


while not should_quit:
    for event in poll_events():
        if type(event) is CloseEvent:
            should_quit = True
        if type(event) is MouseMoveEvent:
            mouseX = event.x
            mouseY = event.y
        tlacidka()
    if frameCount == sec(0.7):
        bullets.append(Bullet(dick.x, dick.y, mouseX -
                              window_width/2, mouseY-window_height/2))
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
        i.update()
        if i.hp > 0 and randint(0, 1000) < 5:
            zombiky.append(Mob(i.x, i.y, 2.8, 10))

    for i in bullets:
        if check(i.x, i.y):
            i, bullets[len(bullets)-1] = bullets[len(bullets)-1], i
            bullets.pop()
        else:
            i.update()

    for i in zombiky:
        i.chase(dick)
        i.update(dick.x, dick.y)

    for i in spawnery:
        if sqrt((dick.x-i.x)**2 + (dick.y-i.y)**2) < dick.size+i.size:
            i.hp -= 1
    #print(dick.x, dick.y)
    dick.move()
    dick.update(mouseX, mouseY, window_width, window_height)
    move_camera(position=(0, 0), rotation=None, zoom=None)
    next_frame()

close_window()
