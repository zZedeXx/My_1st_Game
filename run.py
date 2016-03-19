import tty
import termios
import sys
import os
from Classes.Hero import Hero, Logs

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
    for line_f, line_stat in zip(field, status_bar):
        print(" ".join(line_f + ['   '] + line_stat))
    print("Press 'q' to Exit")
    print("'a' - move left")
    print("'d' - move right")
    print("'w' - move up")
    print("'s' - move down")


# Локация
fields = {
'1': [
    ['#', '#', '#', '#', '#', '#', '#', '#', ' ', '#', '#', '#', '#', '#'],
    ['⬜', 'H', '.', '.', '.', '.', '.', '#', '#', '#', '.', '.', '.', '#'],
    ['#', '.', '.', '.', '.', '.', '.', '.', '|', '.', '.', '.', '.', '#'],
    ['#', '.', '.', '.', '.', '#', '#', '#', '#', '#', '.', '.', '.', '#'],
    ['#', '.', '.', '✳', '.', '#', 'f', '#', ' ', '#', '#', '#', '#', '#'],
    ['#', '.', '.', '.', '.', '#', '.', '#', ' ', '#', '.', '.', '.', '#'],
    ['#', '#', '#', '.', '#', '#', '.', '#', '#', '#', '.', '.', '.', '#'],
    ['#', '.', '.', '.', '.', '.', '.', '#', '.', '#', '.', '.', '.', '#'],
    ['#', '.', '.', '✳', '.', '.', '✳', '.', '.', '.', '.', '.', '.', '#'],
    ['#', '.', '.', '.', '.', '.', '.', '#', '.', '#', '.', '.', '.', '#'],
    ['#', '.', '.', '.', '.', '.', '.', '#', '.', '#', '#', '#', '#', '#'],
    ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', ' ', ' ', ' ', ' ']
],
'2': [
    ['#', '#', '#', '#', '#', '#', '#', '#'],
    ['#', 'H', '.', '✳', '✳', '✳', '.', '#'],
    ['⬜', '.', '.', '.', '.', '✳', '.', '#'],
    ['#', '.', '.', '.', '.', '✳', '.', '#'],
    ['#', '.', '.', '.', '.', '✳', '.', '#'],
    ['#', '#', '#', '#', '#', '#', '#', '#']
]
}
status_bar = [
    '+============+',
    '| HP = {:<6}|',
    '| MP = {:<6}|',
    '| Gl = {:<6}|',
    '| EX = {:<6}|',
    '| Lv = {:<6}|',
    '| Key= {:<6}|',
    '+============+'
]
for i in range(len(fields['1'])):
    try:
        status_bar[i]
    except IndexError:
        status_bar.append([' '])
# Инициализация
logs = Logs()
unit = Hero(fields, status_bar, logs)


def check(fields):
        if unit.location == 0:
            field = fields['1']
        elif unit.location == 1:
            field = fields['2']
        return field

status_bar = unit.status_bar
cls()
render(check(fields), status_bar)

ch = ''

while ch != 'q':
    ch = getchar()
    unit.events(ch)
    unit.update()
    cls()
    render(check(fields), status_bar)
    print('You pressed', ch)
    print(unit.key)
    if unit.Hit_Points == 0 or unit.Hit_Points < 0:
        print('You die!!!')
        ch = 'q'
    logs.render()

