from pygame import *
from random import randint

init()
window_size = 800, 600
window = display.set_mode(window_size)
display.set_caption("Flowey Bird")

clock = time.Clock()
FPS = 180

player_rect = Rect(100, 250, 75, 75)

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

tubes = generate_tubes(150)

gravity = 0.2
y_vel = 0.0
IMPULSE = -5.0
sped = 2

lose = False

while 1:
    for e in event.get():
        if e.type == QUIT:
            quit()

    y_vel += gravity
    player_rect.y += int(y_vel)

    keys = key.get_pressed()
    if keys[K_w]: y_vel = IMPULSE

    if player_rect.bottom >= window_size[1]:
        player_rect.bottom = window_size[1]
        lose = True
        y_vel = 0

    if player_rect.top <= 0:
            player_rect.top = 0
    
    window.fill("sky blue")
    for tube in tubes[:]:
        if not lose:
            tube.x -= sped
        if tube.right < 0:
            tubes.remove(tube)
            sped += 0.1
            continue
        draw.rect(window, (0, 255, 0), tube)
        if player_rect.colliderect(tube):
            lose = True
            y_vel = 0

    if len(tubes) < 8:
        tubes += generate_tubes(150)
    
    draw.rect(window, (255, 255, 0), player_rect)
    display.update()
    clock.tick(FPS)
