import tty
import termios
import sys
import os
from Classes.Hero import Hero


def getchar():
    """
    Returns a single character from standard input
    """
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch


def cls():
    """
    Очищаем консоль
    """
    os.system(['clear', 'cls'][os.name == 'nt'])


def render(field, status_bar):
    for line_f, line_inv in zip(field, status_bar):
        print(" ".join(line_f + [' '] + line_inv))
    print("Press 'q' to Exit")
    print("'a' - move left")
    print("'d' - move right")
    print("'w' - move up")
    print("'s' - move down")


# Локация
field = [
    ['#', '#', '#', '#', '#', '#', '#', '#', ' ', '#', '#', '#', '#', '#'],
    ['#', '⬜', '.', '.', '.', '.', '.', '#', '#', '#', '.', '.', '.', '#'],
    ['#', 'H', '.', '.', '.', '.', '.', '.', '|', '.', '.', '.', '.', '#'],
    ['#', '.', '.', '.', '.', '#', '#', '#', '#', '#', '.', '.', '.', '#'],
    ['#', '.', '.', '.', '.', '#', 'f', '#', ' ', '#', '#', '#', '#', '#'],
    ['#', '.', '.', '.', '.', '#', '.', '#', ' ', '#', '.', '.', '.', '#'],
    ['#', '#', '#', '.', '#', '#', '.', '#', '#', '#', '.', '.', '.', '#'],
    ['#', '.', '.', '.', '.', '.', '.', '#', '.', '#', '.', '.', '.', '#'],
    ['#', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '#'],
    ['#', '.', '.', '.', '.', '.', '✳', '#', '.', '#', '.', '.', '.', '#'],
    ['#', '.', '.', '.', '.', '.', '.', '#', '.', '#', '#', '#', '#', '#'],
    ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', ' ', ' ', ' ', ' ']
]
status_bar = [
    ['+', '=', '=', '=', '=', '=', '=', '=', '=', '+'],
    ['|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|'],
    ['|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|'],
    ['|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|'],
    ['|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|'],
    ['+', '=', '=', '=', '=', '=', '=', '=', '=', '+']
]
for i in range(len(field)):
    try:
        status_bar[i]
    except IndexError:
        status_bar.append([])
# Инициализация
unit = Hero(field, status_bar)
cls()
render(field, status_bar)

ch = ''
while ch != 'q':
    ch = getchar()
    unit.events(ch)
    unit.update()
    cls()
    render(field, status_bar)
    print('You pressed', ch)
    print(unit.HP)
