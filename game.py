from easygame import *

open_window('Easy Game!', 800, 600)
should_quit = False

key = {}
key['UP'] = False
key['DOWN'] = False
key['LEFT'] = False
key['RIGHT'] = False


def move(vect, vel):
    if key['UP']:
        vect[1] += vel
    if key['DOWN']:
        vect[1] -= vel
    if key['LEFT']:
        vect[0] -= vel
    if key['RIGHT']:
        vect[0] += vel
    return vect


def tlacidka():
    if type(event) is KeyDownEvent:
        key[event.key] = True
    if type(event) is KeyUpEvent:
        key[event.key] = False


vect = [100, 100]

while not should_quit:
    for event in poll_events():
        if type(event) is CloseEvent:
            should_quit = True
        tlacidka()

    vect = move(vect, 10)

    fill(1, 1, 0)
    draw_circle((vect[0], vect[1]), 100, color=(0.4, 0.3, 0.2, 1))
    move_camera(position=(0, 0), rotation=None, zoom=None)
    next_frame()

close_window()
