"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics_1 import BreakoutGraphics

FRAME_RATE = 1000 / 120  # 120 frames per second
NUM_LIVES = 3  # Number of attempts


def main():
    graphics = BreakoutGraphics()
    lives = NUM_LIVES
    dx = graphics.get_x_speed()
    dy = graphics.get_y_speed()

    while True:  # SET CONDITION FOR MOUSE CLICK LISTENER TO TURN THE PROGRAM ON(ONE WAY):
        pause(FRAME_RATE)
        if not graphics.opener:  # 初始值是True
            # STOP CONDITION SHOULD BE TESTED AFTER FUNCTIONS SET
            graphics.ball.move(dx, dy)
            dy = graphics.ball_touch(dy)

            if graphics.ball_bottom():
                lives -= 1
                if lives > 0:
                    graphics.reset_ball()
            if graphics.ball.x <= 0 or graphics.ball.x + graphics.ball.width >= graphics.window.width:
                dx = -dx
            if graphics.ball.y <= 0:
                dy = -dy


if __name__ == '__main__':
    main()
