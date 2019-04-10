from easygame import *

open_window('Easy Game!', 800, 600)
should_quit = False


while not should_quit:
    for event in poll_events():
        if type(event) is CloseEvent:
            should_quit = True

    fill(1, 1, 0)
    draw_circle((400, 300), 300, color=(0.4, 0.3, 0.2, 1))
    move_camera(position=(10, 10), rotation=None, zoom=None)
    next_frame()

close_window()
