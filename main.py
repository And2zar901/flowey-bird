from pygame import *
from random import randint

init()
window_size = 800, 600
window = display.set_mode(window_size)
display.set_caption("Flowey Bird")

clock = time.Clock()
FPS = 180

player_rect = Rect(100, 250, 100, 100)

def generate_tubes(count, tube_width = 140,
                    gap = 240,
                    min_height = 50,
                    max_height = 320,
                    distance = 650):
    tubes = []
    start_x = window_size[0]
    for i in range(count):
        height = randint(min_height, max_height)
        top_tube = Rect(start_x, 0, tube_width, height)
        bottom_tube = Rect(start_x, 
                           height + gap, 
                           tube_width, 
                           window_size[1] - height - gap)
        tubes.extend([top_tube, bottom_tube])
        start_x += distance

    return tubes

while 1:
    for e in event.get():
        if e.type == QUIT:
            quit()
    keys = key.get_pressed()
    if keys[K_w]: player_rect.y -= 5
    if keys[K_s]: player_rect.y += 5
    
    window.fill("sky blue")
    draw.rect(window, (255, 255, 0), player_rect)
    display.update()
    clock.tick(FPS)
