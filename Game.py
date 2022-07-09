# Import the necessary libraries.
from JMSSGraphics import *
import random

# define the required variables
scr_width = 800
scr_height = 600
platform_w = 118
platform_h = 200
ball_w = 42
ball_h = 60
platform_yvel = 5
platform_xvel = 10
platform1_x = (scr_width-platform_w)/2
platform1_y = 50
player1_score = 0
game_state = 0
ball_xvel = 0
ball_yvel = 0
ball_x = 0
ball_y = 0
timer = 0
n = 0
n1 = 0
read = 1
contents = 0
p = 0
p1 = 0
# Amount of ball is randomly generated here
x = random.randint(0, 20)

# Create the windows for the GUI
gamewindow = Graphics(width = scr_width, height = scr_height,title = "Game", fps = 60)

# Preload required images into RAM
ball_image = gamewindow.loadImage('ball2.png')
platform_ball1 = gamewindow.loadImage('1.png')
platform_ball2 = gamewindow.loadImage('2.png')
platform_ball3 = gamewindow.loadImage('3.png')
platform_ball4 = gamewindow.loadImage('4.png')
platform_ball5 = gamewindow.loadImage('5.png')
platform_ball6 = gamewindow.loadImage('6.png')
platform_ball7 = gamewindow.loadImage('7.png')
platform_ball8 = gamewindow.loadImage('8.png')
platform_ball9 = gamewindow.loadImage('9.png')
platform_ball10 = gamewindow.loadImage('10.png')
platform_ball11 = gamewindow.loadImage('11.png')
platform_ball12 = gamewindow.loadImage('12.png')
platform_ball13 = gamewindow.loadImage('13.png')
platform_ball14 = gamewindow.loadImage('14.png')
platform_ball15 = gamewindow.loadImage('15.png')
platform_ball16 = gamewindow.loadImage('16.png')
title1 = gamewindow.loadImage('frame_00_delay-0.04s.png')
title2 = gamewindow.loadImage('frame_01_delay-0.04s.png')
title3 = gamewindow.loadImage('frame_02_delay-0.04s.png')
title4 = gamewindow.loadImage('frame_03_delay-0.04s.png')
title5 = gamewindow.loadImage('frame_04_delay-0.04s.png')
title6 = gamewindow.loadImage('frame_05_delay-0.04s.png')
title7 = gamewindow.loadImage('frame_06_delay-0.04s.png')
title8 = gamewindow.loadImage('frame_07_delay-0.04s.png')
title9 = gamewindow.loadImage('frame_08_delay-0.04s.png')
title10 = gamewindow.loadImage('frame_09_delay-0.04s.png')
title11 = gamewindow.loadImage('frame_10_delay-0.04s.png')
title12 = gamewindow.loadImage('frame_11_delay-0.04s.png')
title13 = gamewindow.loadImage('frame_12_delay-0.04s.png')
title14 = gamewindow.loadImage('frame_13_delay-0.04s.png')
title15 = gamewindow.loadImage('frame_14_delay-0.04s.png')
title16 = gamewindow.loadImage('frame_15_delay-0.04s.png')
title17 = gamewindow.loadImage('frame_16_delay-0.04s.png')
title18 = gamewindow.loadImage('frame_17_delay-0.04s.png')
title19 = gamewindow.loadImage('frame_18_delay-0.04s.png')
title20 = gamewindow.loadImage('frame_19_delay-0.04s.png')
title21 = gamewindow.loadImage('frame_20_delay-0.04s.png')
title22 = gamewindow.loadImage('frame_21_delay-0.04s.png')
title23 = gamewindow.loadImage('frame_22_delay-0.04s.png')
title24 = gamewindow.loadImage('frame_23_delay-0.04s.png')
title25 = gamewindow.loadImage('frame_24_delay-0.04s.png')
title26 = gamewindow.loadImage('frame_25_delay-0.04s.png')
title27 = gamewindow.loadImage('frame_26_delay-0.04s.png')
title28 = gamewindow.loadImage('frame_27_delay-0.04s.png')
background = gamewindow.loadImage('background.png')
# Loads the sound effects to the RAM
sizzle = gamewindow.loadSound('sizzle.wav', streaming=False)

#       Create the necessary functions

# This function generates the position of the ball
def position(ball_y, ball_x, ball_xvel, ball_yvel):
    globals()[ball_xvel] = random.randint(-8, 8) #sets the global variable ball_xvel to a randiant value
    globals()[ball_yvel] = random.randint(1, 15) #sets the global variable ball_yvel to a randiant value

    globals()[ball_x] = random.randint(0, scr_width - ball_w) #sets the global variable ball_x to a randiant value
    globals()[ball_y] = 500 #sets the global variable ball_y to 500

# This function moves and bounces the ball
def ball(a, b, c, d):
    global platform_w, platform_h, player1_score, platform1_x, scr_height, sizzle

    # Places global variables in to local ones.
    ball_y = globals()[a]
    ball_x = globals()[b]
    ball_xvel = globals()[c]
    ball_yvel = globals()[d]

    ball_x -= ball_xvel
    ball_y -= ball_yvel

    # Defines what the ball does if it go below the screen
    if ball_y < -100:
        # Minus the score
        player1_score -= 1
        # Teleports the ball to the top of the screen with a random x position
        ball_y = 500
        ball_x = random.randint(0, (scr_width - ball_w))
        # Generates random x and y velocity
        ball_xvel = random.randint(1, 15)
        ball_yvel = random.randint(1, 15)

    # Bounces the ball of the wall on the side.
    if ball_x < 0 or ball_x > (scr_width - ball_w):
        ball_xvel = ball_xvel * -1

    # Defines if the ball hits the platform.
    if ball_x >= platform1_x and ball_x <= platform1_x + platform_w and \
            ball_y + ball_h >= platform1_y and \
            ball_y <= platform1_y + platform_h:
        player1_score += 1 # Adds a point the score
        gamewindow.playSound(sizzle, loop=False) # Plays sound effect
        # Teleports the ball to the top of the screen with a random x position
        ball_x = random.randint(0, (scr_width - ball_w))
        ball_y = scr_height
        # Generates random x and y velocity
        ball_xvel = random.randint(-8, 8)
        ball_yvel = random.randint(1, 15)

    # Place the values in the local variable into the global variables.
    globals()[a] = ball_y
    globals()[b] = ball_x
    globals()[c] = ball_xvel
    globals()[d] = ball_yvel

# This function draws the ball
def ball_draw(number):
    # set the local variable to the global variable counterpart.
    ball_y = globals()[str("ball_y" + str(number))]
    ball_x = globals()[str("ball_x" + str(number))]
    # Draws the ball on the screen.
    gamewindow.drawImage(ball_image, x=ball_x, y=ball_y, height=ball_h, width=ball_w)

# Generate the starting position of the ball/s for how many balls there are (variable x)
for i in range(x):
    position(str("ball_y" + str(i)), str("ball_x" + str(i)), str("ball_xvel" + str(i)), str("ball_yvel" + str(i)))

# Everything below is a loop which show each frame
@gamewindow.mainloop
def game():
    # All the neccessary variable made global
    global platform_w, platform_h, ball_w, ball_h, platform_yvel, platform_xvel, ball_xvel, ball_yvel, ball_x, ball_y, scr_width, scr_height, player1_score, platform1_x, platform1_y, game_state, timer, n, n1, read, contents, f, p, p1, sizzle, x
    global platform_ball1, platform_ball2, platform_ball3, platform_ball4, platform_ball5, platform_ball6, platform_ball7, platform_ball8, platform_ball9, platform_ball10, platform_ball11, platform_ball12, platform_ball13, platform_ball14, platform_ball15, platform_ball16, platform_ball17, platform_ball18
    global title1, title2, title3, title4, title5, title6, title7, title8, title9, title10, title11, title12, title13, title14, title15, title16, title17, title18, title19, title20, title21, title22, title23, title24, title25, title26, title27, title28
    global ball_y3, ball_x3, ball_xvel3, ball_yvel3, ball_y4, ball_x4, ball_xvel4, ball_yvel4
    # Clears the screen
    gamewindow.clear(0, 0, 0, 1)

    # Determine which screen will be shown
    if game_state == 0:
    # This is the title screen
        # Set player score to 0
        player1_score = 0
        if gamewindow.isMousePressed(MOUSE_BUTTON_LEFT):
            # Enters game if screen is left clicked
            game_state = 1

        # plays animation in the background
        if p == 0:
            gamewindow.drawImage(title1, x=0, y=0, height=scr_height, width=scr_width)
            p1 += 1
            if p1 == 3:
                p += 1
                p1 = 0
        if p == 1:
            gamewindow.drawImage(title2, x=0, y=0, height=scr_height, width=scr_width)
            p1 += 1
            if p1 == 3:
                p += 1
                p1 = 0
        if p == 2:
            gamewindow.drawImage(title3, x=0, y=0, height=scr_height, width=scr_width)
            p1 += 1
            if p1 == 3:
                p += 1
                p1 = 0
        if p == 3:
            gamewindow.drawImage(title4, x=0, y=0, height=scr_height, width=scr_width)
            p1 += 1
            if p1 == 3:
                p += 1
                p1 = 0
        if p == 4:
            gamewindow.drawImage(title5, x=0, y=0, height=scr_height, width=scr_width)
            p1 += 1
            if p1 == 3:
                p += 1
                p1 = 0
        if p == 5:
            gamewindow.drawImage(title6, x=0, y=0, height=scr_height, width=scr_width)
            p1 += 1
            if p1 == 3:
                p += 1
                p1 = 0
        if p == 6:
            gamewindow.drawImage(title7, x=0, y=0, height=scr_height, width=scr_width)
            p1 += 1
            if p1 == 3:
                p += 1
                p1 = 0
        if p == 7:
            gamewindow.drawImage(title8, x=0, y=0, height=scr_height, width=scr_width)
            p1 += 1
            if p1 == 3:
                p += 1
                p1 = 0
        if p == 8:
            gamewindow.drawImage(title9, x=0, y=0, height=scr_height, width=scr_width)
            p1 += 1
            if p1 == 3:
                p += 1
                p1 = 0
        if p == 9:
            gamewindow.drawImage(title10, x=0, y=0, height=scr_height, width=scr_width)
            p1 += 1
            if p1 == 3:
                p += 1
                p1 = 0
        if p == 10:
            gamewindow.drawImage(title11, x=0, y=0, height=scr_height, width=scr_width)
            p1 += 1
            if p1 == 3:
                p += 1
                p1 = 0
        if p == 11:
            gamewindow.drawImage(title12, x=0, y=0, height=scr_height, width=scr_width)
            p1 += 1
            if p1 == 3:
                p += 1
                p1 = 0
        if p == 12:
            gamewindow.drawImage(title13, x=0, y=0, height=scr_height, width=scr_width)
            p1 += 1
            if p1 == 3:
                p += 1
                p1 = 0
        if p == 13:
            gamewindow.drawImage(title14, x=0, y=0, height=scr_height, width=scr_width)
            p1 += 1
            if p1 == 3:
                p += 1
                p1 = 0
        if p == 14:
            gamewindow.drawImage(title15, x=0, y=0, height=scr_height, width=scr_width)
            p1 += 1
            if p1 == 3:
                p += 1
                p1 = 0
        if p == 15:
            gamewindow.drawImage(title16, x=0, y=0, height=scr_height, width=scr_width)
            p1 += 1
            if p1 == 3:
                p += 1
                p1 = 0
        if p == 16:
            gamewindow.drawImage(title17, x=0, y=0, height=scr_height, width=scr_width)
            p1 += 1
            if p1 == 3:
                p += 1
                p1 = 0
        if p == 17:
            gamewindow.drawImage(title18, x=0, y=0, height=scr_height, width=scr_width)
            p1 += 1
            if p1 == 3:
                p += 1
                p1 = 0
        if p == 18:
            gamewindow.drawImage(title19, x=0, y=0, height=scr_height, width=scr_width)
            p1 += 1
            if p1 == 3:
                p += 1
                p1 = 0
        if p == 19:
            gamewindow.drawImage(title20, x=0, y=0, height=scr_height, width=scr_width)
            p1 += 1
            if p1 == 3:
                p += 1
                p1 = 0
        if p == 20:
            gamewindow.drawImage(title21, x=0, y=0, height=scr_height, width=scr_width)
            p1 += 1
            if p1 == 3:
                p += 1
                p1 = 0
        if p == 21:
            gamewindow.drawImage(title22, x=0, y=0, height=scr_height, width=scr_width)
            p1 += 1
            if p1 == 3:
                p += 1
                p1 = 0
        if p == 22:
            gamewindow.drawImage(title23, x=0, y=0, height=scr_height, width=scr_width)
            p1 += 1
            if p1 == 3:
                p += 1
                p1 = 0
        if p == 23:
            gamewindow.drawImage(title24, x=0, y=0, height=scr_height, width=scr_width)
            p1 += 1
            if p1 == 3:
                p += 1
                p1 = 0
        if p == 24:
            gamewindow.drawImage(title25, x=0, y=0, height=scr_height, width=scr_width)
            p1 += 1
            if p1 == 3:
                p += 1
                p1 = 0
        if p == 25:
            gamewindow.drawImage(title26, x=0, y=0, height=scr_height, width=scr_width)
            p1 += 1
            if p1 == 3:
                p += 1
                p1 = 0
        if p == 26:
            gamewindow.drawImage(title27, x=0, y=0, height=scr_height, width=scr_width)
            p1 += 1
            if p1 == 3:
                p += 1
                p1 = 0
        if p == 27:
            gamewindow.drawImage(title28,x = 0, y = 0, height = scr_height, width = scr_width)
            p1 += 1
            if p1 == 3:
                p = 0
                p1 = 0
        # Draw text on the screen
        gamewindow.drawText('Click Anywhere To Play', x=250, y=100, fontSize=20,
                            color=(0.5, 1, 0.1, 1))
    # This is the game screen
    if game_state == 1:
        # Starts the timer
        timer += 1

        # Generates the values required for the movement of the ball/s.
        for i in range(x):
            ball(str("ball_y" + str(i)), str("ball_x" + str(i)), str("ball_xvel" + str(i)), str("ball_yvel" + str(i)))

        # Draws a background element
        gamewindow.drawImage(background, x=0, y=-225, height=600, width=800)

        # Draw the ball/s (amount defined by x)
        for i in range(x):
            ball_draw(i)



        # Animation for the ball
        if n == 0:
            gamewindow.drawImage(platform_ball1,x = platform1_x, y = platform1_y, height = platform_h, width = platform_w)
            n1 += 1
            if n1 == 5:
                n += 1
                n1 = 0
        if n == 1:
            gamewindow.drawImage(platform_ball2,x = platform1_x, y = platform1_y, height = platform_h, width = platform_w)
            n1 += 1
            if n1 == 5:
                n += 1
                n1 = 0
        if n == 2:
            gamewindow.drawImage(platform_ball3,x = platform1_x, y = platform1_y, height = platform_h, width = platform_w)
            n1 += 1
            if n1 == 5:
                n += 1
                n1 = 0
        if n == 3:
            gamewindow.drawImage(platform_ball4,x = platform1_x, y = platform1_y, height = platform_h, width = platform_w)
            n1 += 1
            if n1 == 5:
                n += 1
                n1 = 0
        if n == 4:
            gamewindow.drawImage(platform_ball5,x = platform1_x, y = platform1_y, height = platform_h, width = platform_w)
            n1 += 1
            if n1 == 5:
                n += 1
                n1 = 0
        if n == 5:
            gamewindow.drawImage(platform_ball6,x = platform1_x, y = platform1_y, height = platform_h, width = platform_w)
            n1 += 1
            if n1 == 5:
                n += 1
                n1 = 0
        if n == 6:
            gamewindow.drawImage(platform_ball7,x = platform1_x, y = platform1_y, height = platform_h, width = platform_w)
            n1 += 1
            if n1 == 5:
                n += 1
                n1 = 0
        if n == 7:
            gamewindow.drawImage(platform_ball8,x = platform1_x, y = platform1_y, height = platform_h, width = platform_w)
            n1 += 1
            if n1 == 5:
                n += 1
                n1 = 0
        if n == 8:
            gamewindow.drawImage(platform_ball9,x = platform1_x, y = platform1_y, height = platform_h, width = platform_w)
            n1 += 1
            if n1 == 5:
                n += 1
                n1 = 0
        if n == 9:
            gamewindow.drawImage(platform_ball10,x = platform1_x, y = platform1_y, height = platform_h, width = platform_w)
            n1 += 1
            if n1 == 5:
                n += 1
                n1 = 0
        if n == 10:
            gamewindow.drawImage(platform_ball11,x = platform1_x, y = platform1_y, height = platform_h, width = platform_w)
            n1 += 1
            if n1 == 5:
                n += 1
                n1 = 0
        if n == 11:
            gamewindow.drawImage(platform_ball12, x=platform1_x, y=platform1_y, height=platform_h, width=platform_w)
            n1 += 1
            if n1 == 5:
                n += 1
                n1 = 0
        if n == 12:
            gamewindow.drawImage(platform_ball13,x = platform1_x, y = platform1_y, height = platform_h, width = platform_w)
            n1 += 1
            if n1 == 5:
                n += 1
                n1 = 0
        if n == 13:
            gamewindow.drawImage(platform_ball14,x = platform1_x, y = platform1_y, height = platform_h, width = platform_w)
            n1 += 1
            if n1 == 5:
                n += 1
                n1 = 0
        if n == 14:
            gamewindow.drawImage(platform_ball15,x = platform1_x, y = platform1_y, height = platform_h, width = platform_w)
            n1 += 1
            if n1 == 5:
                n += 1
                n1 = 0
        if n == 15:
            gamewindow.drawImage(platform_ball16,x = platform1_x, y = platform1_y, height = platform_h, width = platform_w)
            n1 += 1
            if n1 == 5:
                n = 0
                n1 = 0

        # Displays the score
        gamewindow.drawText("score: " + str(player1_score), 100, scr_height - 50, fontSize=35, color=(0, 0.4, 0.8, 1))
        # Displays the time left
        gamewindow.drawText("time left: " + str(int(round(10-(timer/60), 0))), scr_width/2, scr_height - 50, fontSize=35, color=(0, 0.4, 0.8, 1))

        # Retrieves the mouses position
        mouse_pos = gamewindow.getMousePos()
        # Assign the platforms position to position of the mouse
        platform1_x = mouse_pos[0] - 65
        platform1_y = mouse_pos[1] - 35

        # Prevents the platform from leaving the screen
        if platform1_x < 0:
            platform1_x = 0
        if platform1_x > (scr_width - platform_w):
            platform1_x = scr_width - platform_w

        # Enters the finish screen if the timer is reaches 10 seconds
        if timer >= 600:
            game_state = 2
            # Activates the retrieval of the highest score
            read = 1
            # Resets timer
            timer = 0

    # This is the finish screen
    if game_state == 2:

        # Background animation
        if p == 0:
            gamewindow.drawImage(title1, x=0, y=0, height=scr_height, width=scr_width)
            p1 += 1
            if p1 == 3:
                p += 1
                p1 = 0
        if p == 1:
            gamewindow.drawImage(title2, x=0, y=0, height=scr_height, width=scr_width)
            p1 += 1
            if p1 == 3:
                p += 1
                p1 = 0
        if p == 2:
            gamewindow.drawImage(title3, x=0, y=0, height=scr_height, width=scr_width)
            p1 += 1
            if p1 == 3:
                p += 1
                p1 = 0
        if p == 3:
            gamewindow.drawImage(title4, x=0, y=0, height=scr_height, width=scr_width)
            p1 += 1
            if p1 == 3:
                p += 1
                p1 = 0
        if p == 4:
            gamewindow.drawImage(title5, x=0, y=0, height=scr_height, width=scr_width)
            p1 += 1
            if p1 == 3:
                p += 1
                p1 = 0
        if p == 5:
            gamewindow.drawImage(title6, x=0, y=0, height=scr_height, width=scr_width)
            p1 += 1
            if p1 == 3:
                p += 1
                p1 = 0
        if p == 6:
            gamewindow.drawImage(title7, x=0, y=0, height=scr_height, width=scr_width)
            p1 += 1
            if p1 == 3:
                p += 1
                p1 = 0
        if p == 7:
            gamewindow.drawImage(title8, x=0, y=0, height=scr_height, width=scr_width)
            p1 += 1
            if p1 == 3:
                p += 1
                p1 = 0
        if p == 8:
            gamewindow.drawImage(title9, x=0, y=0, height=scr_height, width=scr_width)
            p1 += 1
            if p1 == 3:
                p += 1
                p1 = 0
        if p == 9:
            gamewindow.drawImage(title10, x=0, y=0, height=scr_height, width=scr_width)
            p1 += 1
            if p1 == 3:
                p += 1
                p1 = 0
        if p == 10:
            gamewindow.drawImage(title11, x=0, y=0, height=scr_height, width=scr_width)
            p1 += 1
            if p1 == 3:
                p += 1
                p1 = 0
        if p == 11:
            gamewindow.drawImage(title12, x=0, y=0, height=scr_height, width=scr_width)
            p1 += 1
            if p1 == 3:
                p += 1
                p1 = 0
        if p == 12:
            gamewindow.drawImage(title13, x=0, y=0, height=scr_height, width=scr_width)
            p1 += 1
            if p1 == 3:
                p += 1
                p1 = 0
        if p == 13:
            gamewindow.drawImage(title14, x=0, y=0, height=scr_height, width=scr_width)
            p1 += 1
            if p1 == 3:
                p += 1
                p1 = 0
        if p == 14:
            gamewindow.drawImage(title15, x=0, y=0, height=scr_height, width=scr_width)
            p1 += 1
            if p1 == 3:
                p += 1
                p1 = 0
        if p == 15:
            gamewindow.drawImage(title16, x=0, y=0, height=scr_height, width=scr_width)
            p1 += 1
            if p1 == 3:
                p += 1
                p1 = 0
        if p == 16:
            gamewindow.drawImage(title17, x=0, y=0, height=scr_height, width=scr_width)
            p1 += 1
            if p1 == 3:
                p += 1
                p1 = 0
        if p == 17:
            gamewindow.drawImage(title18, x=0, y=0, height=scr_height, width=scr_width)
            p1 += 1
            if p1 == 3:
                p += 1
                p1 = 0
        if p == 18:
            gamewindow.drawImage(title19, x=0, y=0, height=scr_height, width=scr_width)
            p1 += 1
            if p1 == 3:
                p += 1
                p1 = 0
        if p == 19:
            gamewindow.drawImage(title20, x=0, y=0, height=scr_height, width=scr_width)
            p1 += 1
            if p1 == 3:
                p += 1
                p1 = 0
        if p == 20:
            gamewindow.drawImage(title21, x=0, y=0, height=scr_height, width=scr_width)
            p1 += 1
            if p1 == 3:
                p += 1
                p1 = 0
        if p == 21:
            gamewindow.drawImage(title22, x=0, y=0, height=scr_height, width=scr_width)
            p1 += 1
            if p1 == 3:
                p += 1
                p1 = 0
        if p == 22:
            gamewindow.drawImage(title23, x=0, y=0, height=scr_height, width=scr_width)
            p1 += 1
            if p1 == 3:
                p += 1
                p1 = 0
        if p == 23:
            gamewindow.drawImage(title24, x=0, y=0, height=scr_height, width=scr_width)
            p1 += 1
            if p1 == 3:
                p += 1
                p1 = 0
        if p == 24:
            gamewindow.drawImage(title25, x=0, y=0, height=scr_height, width=scr_width)
            p1 += 1
            if p1 == 3:
                p += 1
                p1 = 0
        if p == 25:
            gamewindow.drawImage(title26, x=0, y=0, height=scr_height, width=scr_width)
            p1 += 1
            if p1 == 3:
                p += 1
                p1 = 0
        if p == 26:
            gamewindow.drawImage(title27, x=0, y=0, height=scr_height, width=scr_width)
            p1 += 1
            if p1 == 3:
                p += 1
                p1 = 0
        if p == 27:
            gamewindow.drawImage(title28,x = 0, y = 0, height = scr_height, width = scr_width)
            p1 += 1
            if p1 == 3:
                p = 0
                p1 = 0

        # Retrieves the highest screen from a txt file called score
        if read == 1:
            # Clears screen
            gamewindow.clear(0, 0, 0, 1)
            # File is opened with read permission to prevent the file being wiped
            f = open("score.txt", "r")
            # Places highest score into the variable contents.
            contents = f.readlines()
            # Prevents rereading of the file after it is updated.
            read = 0
        # Defines what happens if the player score is higher then the highest score
        if int(contents[0]) < player1_score:
            # The files is open with w+ right which wipes the file
            f = open("score.txt", "w+")
            # Writes the score to the file
            f.write(str(player1_score))
            # Draws text on the screen
            gamewindow.drawText("You got a new high score of " + str(player1_score) + "!", x=230, y=200, fontSize=20,color=(0.1, 0.9, 0.3, 1))
            gamewindow.drawText("Click Anywhere to Restart", x=255, y=150, fontSize=20, color=(0.1, 0.9, 0.3, 1))
        # Defines what happens if the player score is the same as the highest score
        if int(contents[0]) == player1_score:
            # Some text is drawn
            gamewindow.drawText("You reached you highest score of " + str(player1_score) + "!", x=210, y=380, fontSize=20,color=(0.1, 0.9, 0.3, 1))
            gamewindow.drawText("Try harder next time to pass it.", x=240,y=(scr_height/2), fontSize=20, color=(0.1, 0.9, 0.3, 1))
            gamewindow.drawText("Click Anywhere to Restart", x=240, y=225, fontSize=20, color=(0.1, 0.9, 0.3, 1))
        # Defines what happens if the player score is below the highest score.
        if int(contents[0]) > player1_score:
            # Draws some text
            gamewindow.drawText("You got " + str(player1_score) + " points!", x=265, y=380, fontSize=20,color=(0.1, 0.9, 0.3, 1))
            gamewindow.drawText("The highest score is " + str(contents[0]), x=255, y=(scr_height/2), fontSize=20,color=(0.1, 0.9, 0.3, 1))
            gamewindow.drawText("Click Anywhere to Restart", x=240, y=225, fontSize=20, color=(0.1, 0.9, 0.3, 1))
        # If the screen is clicked, the game is played again
        if gamewindow.isMousePressed(MOUSE_BUTTON_LEFT):
            # Sets the score to 0
            player1_score = 0
            # Close the file that was opened
            f.close()
            # Enters the game screen
            game_state = 1

# Runs the window.
gamewindow.run()