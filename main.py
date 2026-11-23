from pygame import *
from random import randint
import sounddevice as sd
import numpy as np
from pygame import mixer

import json
mixer.init()

mixer.music.load("FlowerMan.mp3")
mixer.music.set_volume(0.2)
mixer.music.play(-1)

def load_settings():
    with open("settings.json", "r") as f:
        return json.load(f)

settings = load_settings()
voice_mode = settings["voice_mode"]

init()
window_size = 800, 600
window = display.set_mode(window_size)
display.set_caption("Flowey Bird")

clock = time.Clock()
FPS = 180

player_rect = Rect(100, 250, 75, 75)

background = image.load("back.jpg")
background = transform.scale(background, window_size)

bird = image.load("bird_.png")
bird = transform.scale(bird, (75, 75))

tube_top_image = image.load("tube_top.png")
tube_bottom_image = image.load("tube_bottom.png")

sr = 16000
block = 256
mic_level = 0.0

def audio_cb(indata, frames, time, status):
    global mic_level
    if status:
        return
    rms = float(np.sqrt(np.mean(indata ** 2)))
    mic_level = 0.85 * mic_level + 0.15 * rms

THRESH = 0.02
voice_cooldown = 0

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

gravity = 0.1
y_vel = 0.0
IMPULSE = -4.0
sped = 2

lose = False
score = 0
my_font = font.Font(None, 50)

with sd.InputStream(samplerate=sr,
                    channels=1,
                    blocksize=block,
                    callback=audio_cb
):

    while 1:
        for e in event.get():
            if e.type == QUIT:
                quit()
        keys = key.get_pressed()
        if voice_cooldown > 0:
            voice_cooldown -= 1
        if voice_mode:
            if mic_level > THRESH and not lose and voice_cooldown == 0:
                y_vel = IMPULSE
                voice_cooldown = 21
        else:
            if keys[K_w] or keys[K_SPACE]:
                if not lose:
                    y_vel = IMPULSE
                    mixer.Sound("jump_sound.mp3").play()

        if not lose:
            y_vel += gravity
            player_rect.y += int(y_vel)

       

        if keys[K_r] and lose == True:
            lose = False
            score = 0
            tubes = generate_tubes(150)
            player_rect.x = 100
            player_rect.y = 250
            gravity = 0.1
            y_vel = 0.0
            IMPULSE = -4.0
            sped = 4
            voice_cooldown = 0

        if player_rect.bottom >= window_size[1]:
            player_rect.bottom = window_size[1]
            lose = True
            y_vel = 0

        if player_rect.top <= 0:
                player_rect.top = 0
        
        window.blit(background, (0, 0))
        for tube in tubes[:]:
            if not lose:
                tube.x -= sped
            if tube.right < 0:
                tubes.remove(tube)
                score += 0.5
                sped += 0.1
                continue
            if tube.y == 0:
                pipe_image = tube_top_image
            else:
                pipe_image = tube_bottom_image
            pipe = transform.scale(pipe_image, (tube.width, tube.height))
            window.blit(pipe, tube)
            if player_rect.colliderect(tube):
                lose = True
                y_vel = 0

        if len(tubes) < 8:
            tubes += generate_tubes(150)
        
        window.blit(bird, player_rect)

        score_text = my_font.render(f"{int(score)}", True, "white")
        window.blit(score_text, (390, 20))

        if lose:
            lose_text = my_font.render(f"You loose!", True, "yellow")
            window.blit(lose_text, (310, 250))
            lose_text2 = my_font.render(f"Press R to restart", True, "yellow")
            window.blit(lose_text2, (260, 300))

        display.update()
        clock.tick(FPS)
