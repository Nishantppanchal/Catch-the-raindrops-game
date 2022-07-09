# Import the necessary libraries.
from JMSSGraphics import *
import random

# Make the required variables
scr_width = 800
scr_height = 600
platform_w = 100
platform_h = 25
ball_w = 50
ball_h = 50
platform_yvel = 5
platform_xvel = 10
platform1_x = (scr_width-platform_w)/2
platform1_y = 10
player1_score = 0
game_state = 0
ball_xvel = 0
ball_yvel = 0
ball_x = 0
ball_y = 0
timer = 0

# Create the windows for the GUI
gamewindow = Graphics(width = scr_width, height = scr_height,title = "Pong Game!", fps = 60)

# Preload images into RAM
ball_image = gamewindow.loadImage('ball2.png')
platform1_image = gamewindow.loadImage('platform1.png')

# Create the necessary functions
def position(ball_y, ball_x, ball_xvel, ball_yvel):
    globals()[ball_xvel] = random.randint(-8, 8)
    globals()[ball_yvel] = random.randint(1, 15)

    globals()[ball_x] = random.randint(0, scr_width - ball_w)
    globals()[ball_y] = 500

def ball(a, b, c, d):
    global platform_w, platform_h, player1_score, platform1_x, scr_height

    ball_y = globals()[a]
    ball_x = globals()[b]

    ball_xvel = globals()[c]
    ball_yvel = globals()[d]

    ball_x -= ball_xvel
    ball_y -= ball_yvel

    if ball_y < -100:
        ball_y = 500
        ball_x = random.randint(0, (scr_width - ball_w))
        ball_xvel = random.randint(1, 15)
        ball_yvel = random.randint(1, 15)

    if ball_x < 0 or ball_x > (scr_width - ball_w):
        ball_xvel = ball_xvel * -1

    if ball_x >= platform1_x and ball_x <= platform1_x + platform_w and \
            ball_y + ball_h >= platform1_y and \
            ball_y <= platform1_y + platform_h:

        if ball_y < -100:
            ball_y = 500
            ball_x = random.randint(0, (scr_width - ball_w))
            ball_xvel = random.randint(1, 15)
            ball_yvel = random.randint(1, 15)

        if ball_x < 0 or ball_x > (scr_width - ball_w):
            ball_xvel = ball_xvel * -1

        if ball_x >= platform1_x and ball_x <= platform1_x + platform_w and \
                ball_y + ball_h >= platform1_y and \
                ball_y <= platform1_y + platform_h:
            player1_score += 1
            ball_x = random.randint(0, (scr_width - ball_w))
            ball_y = scr_height

            ball_xvel = random.randint(-8, 8)
            ball_yvel = random.randint(1, 15)

    globals()[a] = ball_y
    globals()[b] = ball_x
    globals()[c] = ball_xvel
    globals()[d] = ball_yvel

# Generate the position of the ball/s
position("ball_y", "ball_x", "ball_xvel", "ball_yvel")

# Everything below is a loop which show each frame
@gamewindow.mainloop
def game():
    global platform_w, platform_h, ball_w, ball_h, platform_yvel, platform_xvel, ball_xvel, ball_yvel, ball_x, ball_y, scr_width, scr_height, player1_score, platform1_x, platform1_y, timer

    timer += 1

    gamewindow.clear(0, 0, 0, 1)

    ball("ball_y", "ball_x", "ball_xvel", "ball_yvel")

    gamewindow.drawImage(platform1_image, x=platform1_x, y=platform1_y, height=platform_h, width=platform_w)
    gamewindow.drawImage(ball_image, x=ball_x, y=ball_y, height=ball_h, width=ball_w)
    gamewindow.drawText(str(player1_score), 100, scr_height - 50, fontSize=35, color=(0.1, 0.9, 0.3, 1))
    gamewindow.drawText(str(timer / 60), scr_width / 2, scr_height - 50, fontSize=35, color=(0.1, 0.9, 0.3, 1))

    if gamewindow.isKeyDown(KEY_RIGHT):
        platform1_x += 10
    if gamewindow.isKeyDown(KEY_LEFT):
        platform1_x -= 10
    if platform1_x < 0:
        platform1_x = 0
    if platform1_x > (scr_width - platform_w):
        platform1_x = scr_width - platform_w

    if timer >= 1200:
        exit()
gamewindow.run()