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
map_width = 3000
map_height = 3000

koniec = False
open_window('PELKO', window_width, window_height)
should_quit = False
cam_pos = [0, 0]
dick = Player(map_width, map_height)
spawnery, zombiky, bullets = [], [], []
mouseX, mouseY, frameCount = 0, 0, 0
start = time.time()


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
        if event.key == 'X':
            dick.set_turbo()
        if event.key == 'C':
            for i in zombiky:
                i.frozen = sec(2)

    if type(event) is KeyUpEvent:
        key[event.key] = False


def hud():
    draw_text("HP: " + str(dick.hp), 'Fixedsys', 20, position=(
        cam_pos[0]-window_width/2+10, cam_pos[1]-window_height/2+10), color=(0, 0, 0, 1))
    draw_text("Turbo:  " + str(dick.cooldowns['turbo']), 'Fixedsys', 20, position=(
        cam_pos[0]-window_width/2+window_width/4, cam_pos[1]-window_height/2+10), color=(0, 0, 0, 1))
    draw_text("Ability 2:  " + str(dick.cooldowns['ability2']), 'Fixedsys', 20, position=(
        cam_pos[0]-window_width/2+window_width/2, cam_pos[1]-window_height/2+10), color=(0, 0, 0, 1))
    draw_text("Ability 3:  " + str(dick.cooldowns['ability3']), 'Fixedsys', 20, position=(
        cam_pos[0]-window_width/2+3*window_width/4, cam_pos[1]-window_height/2+10), color=(0, 0, 0, 1))


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

    if koniec:
        continue

    cam_pos = [(dick.x+mouseX)/2, (dick.y+mouseY)/2]
    set_camera(center=(window_width/2, window_height/2),
               position=(cam_pos[0], cam_pos[1]))

    if frameCount == sec(0.7)+10:
        bullets.append(Bullet(dick.x, dick.y, mouseX, mouseY))
        frameCount = 0
    else:
        frameCount += 1

    for i in zombiky:
        for j in zombiky:
            if i != j:
                separate(i, j)
        separate(i, dick)

    fill(0, 0, 0)
    draw_polygon((-map_width/2, -map_height/2), (map_width/2, -map_height/2),
                 (map_width/2, map_height/2), (-map_width/2, map_height/2), color=(0.5, 1, 0.5, 1))
    hud()

    if time.time() - start > 20:
        print(time.time(), start)
        create_spawner()
        start = time.time()

    for i in spawnery:
        i.update()
        if randint(0, 1000) < 5:
            zombiky.append(Mob(i.x, i.y, 2.8))

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
    zombiky = newzombiz

    newspawners = []
    for i in spawnery:
        if sqrt((dick.x-i.x)**2 + (dick.y-i.y)**2) < dick.size+i.size:
            i.hp -= 1
        if i.hp > 0:
            newspawners.append(i)
    spawnery = newspawners

    dick.move()
    dick.update(mouseX, mouseY)
    move_camera(position=(0, 0), rotation=None, zoom=None)

    if not dick.dead:
        next_frame()
    else:
        next_frame()
        draw_text('GAY OVER', 'Fixedsys', 100,
                  position=cam_pos, color=(1, 0, 0, 1))
        next_frame()
        koniec = True

close_window()
