"""
File: 
Name:
-------------------------
TODO:
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked


VX = 5
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40

open1 = False   # if the ball bouncing
count = 0

window = GWindow(800, 500, title='bouncing_ball.py')


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    global open1,count
    speed = 0
    ball = set_up_ball()
    window.add(ball, START_X, START_Y)
    # onmouseclicked 不影響順序 是獨立的 不用放在while或if else裡
    onmouseclicked(start)
    while True:
        if open1 and count < 3:
            ball.move(VX, speed)
            speed += GRAVITY
            if ball.y >= window.height-SIZE:
                speed = -0.9 * speed
            if ball.x >= window.width + 100:
                ball.x = START_X
                ball.y = START_Y
                count += 1
                open1 = False
        pause(DELAY)


def start(mouse):
    global open1
    open1 = True


def set_up_ball():
    ball = GOval(SIZE, SIZE)
    ball.filled = True
    return ball


if __name__ == "__main__":
    main()
