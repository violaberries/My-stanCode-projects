"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
BRICK_WIDTH = 40       # Height of a brick (in pixels).
BRICK_HEIGHT = 15      # Height of a brick (in pixels).
BRICK_ROWS = 10        # Number of rows of bricks.
BRICK_COLS = 10        # Number of columns of bricks.
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels).
BALL_RADIUS = 20       # Radius of the ball (in pixels).
PADDLE_WIDTH = 75      # Width of the paddle (in pixels).
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels).
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels).


INITIAL_Y_SPEED = 7  # Initial vertical speed for the ball.
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball.


class BreakoutGraphics:

    def __init__(self, ball_radius = BALL_RADIUS, paddle_width = PADDLE_WIDTH,
                 paddle_height = PADDLE_HEIGHT, paddle_offset = PADDLE_OFFSET,
                 brick_rows = BRICK_ROWS, brick_cols = BRICK_COLS,
                 brick_width = BRICK_WIDTH, brick_height = BRICK_HEIGHT,
                 brick_offset = BRICK_OFFSET, brick_spacing = BRICK_SPACING,
                 title='Breakout'):

        self.paddle_offset = paddle_offset
        self.paddle_width = paddle_width
        self.ball_radius = ball_radius
        self.opener = True

        # Create a graphical window, with some extra space
        self.window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        self.window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=self.window_width, height=self.window_height, title=title)

        # Create a paddle
        self.paddle = GRect(width=paddle_width, height=paddle_height, x=(self.window_width-paddle_width)/2,
                            y=self.window_height-paddle_offset)
        self.paddle.filled = True
        self.paddle.color = 'black'
        self.window.add(self.paddle)
        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius, ball_radius,x=(self.window_width-ball_radius)/2,
                          y=(self.window_height-ball_radius)/2)
        self.ball.filled = True
        self.window.add(self.ball)

        self.__dx = random.randint(1, MAX_X_SPEED)

        if random.random() > 0.5:
            self.__dx = -self.__dx

        self.__dy = self.__dy = INITIAL_Y_SPEED

        # Default initial velocity for the ball

        # Initialize our mouse listeners
        onmouseclicked(self.click_opener)
        onmousemoved(self.set_paddle)

        # Draw bricks
        for i in range(BRICK_ROWS):
            for j in range(BRICK_COLS):
                self.bricks = GRect(width=BRICK_WIDTH, height=BRICK_HEIGHT, x=i*(BRICK_WIDTH+BRICK_SPACING),
                                    y=j*(BRICK_HEIGHT+BRICK_SPACING)+BRICK_OFFSET)
                self.bricks.filled = True
                if j <= 1:
                    self.bricks.color = 'red'
                    self.bricks.fill_color = 'red'
                if 2 <= j <= 3:
                    self.bricks.color = 'orange'
                    self.bricks.fill_color = 'orange'
                if 4 <= j <= 5:
                    self.bricks.color = 'yellow'
                    self.bricks.fill_color = 'yellow'
                if 6 <= j <= 7:
                    self.bricks.color = 'green'
                    self.bricks.fill_color = 'green'
                if 8 <= j <= 9:
                    self.bricks.color = 'blue'
                    self.bricks.fill_color = 'blue'
                self.window.add(self.bricks)

    def click_opener(self, event):
        self.opener = False

    def ball_touch(self, y_speed):
        x1 = self.ball.x
        x2 = self.ball.x + self.ball_radius * 2
        y1 = self.ball.y
        y2 = self.ball.y + self.ball_radius * 2

        ball_1 = self.window.get_object_at(x1, y1)
        ball_2 = self.window.get_object_at(x2, y1)
        ball_3 = self.window.get_object_at(x1, y2)
        ball_4 = self.window.get_object_at(x2, y2)
        
        if ball_1 is None and ball_2 is None and ball_3 is None and ball_4 is None:
            return y_speed
        else:
            if self.ball.y > self.window_height//2:
                y_speed = -y_speed
                print('2')
                return y_speed
            else:
                print('3')
                y_speed = -y_speed
                self.window.remove(ball_1)
                self.window.remove(ball_2)
                self.window.remove(ball_3)
                self.window.remove(ball_4)
                return y_speed

    def set_paddle(self, mouse):
        self.paddle.x = mouse.x - self.paddle.width/2
        if mouse.x < 0:
            self.paddle.x = 0
        elif mouse.x > self.window_width - self.paddle.width:
            self.paddle.x = self.window_width - self.paddle.width

    def get_x_speed(self):
        return self.__dx

    def get_y_speed(self):
        return self.__dy

    def reset_ball(self):
        self.set_ball_position()
        self.opener = True

    def set_ball_position(self):
        self.ball.x = self.window_width/2
        self.ball.y = self.window_height/2

    # ball falls over window bottom
    def ball_bottom(self):
        return self.ball.y > self.window_height












