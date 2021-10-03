"""
File: 
Name:
-------------------------
TODO:
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked

# Constant
SIZE = 50

# Global
window = GWindow()
click = 0
circle = GOval(SIZE, SIZE)
x0 = 0
y0 = 0
x1 = 0
y1 = 0


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    onmouseclicked(draw)


def draw(mouse):
    global click, x0, x1, y0, y1
    click += 1
    if click % 2 == 1:
        circle.color = 'black'
        window.add(circle, mouse.x-SIZE//2, mouse.y-SIZE//2)
        x0 = mouse.x
        y0 = mouse.y
    else:
        window.remove(circle)
        x1 = mouse.x
        y1 = mouse.y
        line = GLine(x0, y0, x1, y1)
        window.add(line)





if __name__ == "__main__":
    main()
