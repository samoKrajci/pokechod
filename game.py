from easygame import *
from math import *
from random import *
from Bullet import *
from Player import *
from Mob import *
from Spawner import *
from Particles import *
import time

window_width = 1800
window_height = 1000
map_width = 1800
map_height = 1000

score = 0
koniec = False
open_window('PELKO', window_width, window_height)
should_quit = False
cam_pos = [0, 0]
dick = Player(map_width, map_height)
stromy, sutre, spawnery, zombiky, bullets = [], [], [], [], []
mouseX, mouseY, frameCount = 0, 0, 0
start = time.time()
zombie_counter = 0

#poc_stromy = randint(0, map_width*map_height/200000)
#poc_sutre = randint(0, map_width*map_height/200000)
poc_stromy = randint(0, 6)
poc_sutre = randint(0, 6)
# print(poc_stromy)
# print(poc_sutre)

for i in range(poc_stromy):
    stromy.append(Tree(randint(0, map_width)-map_width /
                       2, randint(0, map_height)-map_height/2))
for i in range(poc_stromy):
    sutre.append(Rock(randint(0, map_width)-map_width /
                      2, randint(0, map_height)-map_height/2))


def create_spawner():
    spawnery.append(Spawner(
        randint(-map_width / 2, map_width / 2), randint(-map_height / 2, map_height / 2), 100))


def check(x, y, done):
    if x > map_width/2 or x < -map_width/2 or y > map_height/2 or y < -map_height/2 or done:
        return True
    return False


def tlacidka():
    if type(event) is KeyDownEvent:
        key[event.key] = True
        if event.key == 'X' and dick.cooldowns['turbo'] == 0:
            dick.set_turbo()
            dick.cooldowns['turbo'] = sec(10)
        if event.key == 'C' and dick.cooldowns['freeze'] == 0:
            dick.cooldowns['freeze'] = sec(15)
            for i in zombiky:
                i.frozen = sec(2)
        if event.key == 'V' and dick.cooldowns['as'] == 0:
            dick.cooldowns['as'] = sec(20)
            global frameCount
            frameCount = 10

    if type(event) is KeyUpEvent:
        key[event.key] = False


def hud():
    draw_polygon((cam_pos[0]-map_width/2, cam_pos[1]-map_height/2), (cam_pos[0]-map_width/2, cam_pos[1]-map_height/2+45),
                 (cam_pos[0]+map_width/2, cam_pos[1]-map_height/2+45), (cam_pos[0]+map_width/2, cam_pos[1]-map_height/2), color=(1, 1, 1, 1))
    draw_text("HP: " + str(dick.hp), 'Fixedsys', 20, position=(
        cam_pos[0]-window_width/2+10, cam_pos[1]-window_height/2+10), color=(0, 0, 0, 1))
    draw_text("Turbo:  " + str(int(dick.cooldowns['turbo']/40)), 'Fixedsys', 20, position=(
        cam_pos[0]-window_width/2+window_width/5, cam_pos[1]-window_height/2+10), color=(0, 0, 0, 1))
    draw_text("Freeze:  " + str(int(dick.cooldowns['freeze']/40)), 'Fixedsys', 20, position=(
        cam_pos[0]-window_width/2+2*window_width/5, cam_pos[1]-window_height/2+10), color=(0, 0, 0, 1))
    draw_text("Attack speed:  " + str(int(dick.cooldowns['as']/40)), 'Fixedsys', 20, position=(
        cam_pos[0]-window_width/2+3*window_width/5, cam_pos[1]-window_height/2+10), color=(0, 0, 0, 1))
    draw_text("Score:  " + str(score), 'Fixedsys', 20, position=(
        cam_pos[0] - window_width / 2 + 4*window_width/5, cam_pos[1] - window_height / 2 + 10), color=(0, 0, 0, 1))


def separate(a, b):
    dif = fix_rectangle_overlap(a.hitbox, b.hitbox)
    a.x += dif[0]
    a.y += dif[1]


for i in range(3):
    create_spawner()

while not should_quit:
    for event in poll_events():
        if type(event) is CloseEvent:
            should_quit = True
        if type(event) is MouseMoveEvent:
            mouseX = event.x - window_width/2 + cam_pos[0]
            mouseY = event.y - window_height/2 + cam_pos[1]
        tlacidka()
        if type(event) is MouseDownEvent:
            if event.button == 'LEFT' and frameCount <= 0:
                bullets.append(Bullet(dick.x, dick.y, mouseX, mouseY))
                frameCount = 30

    if koniec:
        continue

    if frameCount > sec(0.7) + 10:
        bullets.append(Bullet(dick.x, dick.y, mouseX, mouseY))
        frameCount = 0
    else:
        frameCount += 1

    cam_pos = [(dick.x+mouseX)/2, (dick.y+mouseY)/2]
    set_camera(center=(window_width/2, window_height/2),
               position=(cam_pos[0], cam_pos[1]))

    for i in zombiky:
        for j in zombiky:
            if i != j:
                separate(i, j)
        separate(i, dick)

    fill(0, 0, 0)
    draw_polygon((-map_width/2, -map_height/2), (map_width/2, -map_height/2),
                 (map_width/2, map_height/2), (-map_width/2, map_height/2), color=(0.5, 1, 0.5, 1))

    if time.time() - start > 20:
        create_spawner()
        start = time.time()

    for i in spawnery:
        i.update()
        if randint(0, 1000) < 5 and zombie_counter < 10:
            zombiky.append(Mob(i.x, i.y, 2.8))
            zombie_counter += 1

    newbullets = []
    for i in bullets:
        if not check(i.x, i.y, i.gone):
            i.update()
            newbullets.append(i)
    bullets = newbullets

    newzombiz = []
    for i in zombiky:
        i.chase(dick, bullets)
        if not i.dead:
            i.update(dick.x, dick.y)
            newzombiz.append(i)
        else:
            zombie_counter -= 1
    zombiky = newzombiz

    newspawners = []
    for i in spawnery:
        if sqrt((dick.x-i.x)**2 + (dick.y-i.y)**2) < dick.size+i.size:
            i.hp -= 1
        if i.hp > 0:
            newspawners.append(i)
        else:
            score += 1
    spawnery = newspawners

    dick.move()
    dick.update(mouseX, mouseY)
    move_camera(position=(0, 0), rotation=None, zoom=None)

    for suter in sutre:
        suter.update()
        separate(dick, suter)
        for zom in zombiky:
            separate(zom, suter)
    for strom in stromy:
        strom.update()
        separate(dick, strom)
        for zom in zombiky:
            separate(zom, strom)

    hud()

    if not dick.dead:
        next_frame()
    else:
        next_frame()
        draw_text('GAY OVER', 'Fixedsys', 100,
                  position=cam_pos, color=(1, 0, 0, 1))
        next_frame()
        koniec = True

close_window()
