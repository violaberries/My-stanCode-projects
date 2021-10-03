"""
File: 
Name:
----------------------
TODO: Welcome to the book club "BOOK DIGEST"!
"""

from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.graphics.gwindow import GWindow


def main():
    window = GWindow(600, 520, 'Mydrawing')
    rect = GRect(600, 520)
    rect.filled = True
    rect.fill_color = '#28468f'
    window.add(rect)

    book = GRect(120, 150, x=180, y=170)
    book2 = GRect(120, 150, x=310, y=170)
    window.add(book)
    window.add(book2)

    dot = GOval(120, 120, x=180, y=117)
    window.add(dot)
    dot.filled = True
    dot.color = '#f89aba'
    dot.fill_color = '#2f89aba'

    dot = GOval(120, 120, x=310, y=117)
    window.add(dot)
    dot.filled = True
    dot.color = '#f89aba'
    dot.fill_color = '#2f89aba'

    dot = GOval(120, 120, x=180, y=290)
    window.add(dot)
    dot.filled = True
    dot.color = '#28468f'
    dot.fill_color = '#28468f'

    dot = GOval(120, 120, x=310, y=290)
    window.add(dot)
    dot.filled = True
    dot.color = '#28468f'
    dot.fill_color = '#28468f'

    book.filled = True
    book.color = '#f89aba'
    book.fill_color = '#f89aba'

    book2.filled = True
    book2.color = '#f89aba'
    book2.fill_color = '#f89aba'

    text = GLabel('@BOOKDIGEST__TW', x=170, y=400)
    text.font = 'Dialog-27-italic-bold'
    text.filled = True
    text.color = 'white'
    window.add(text)


if __name__ == '__main__':
    main()
