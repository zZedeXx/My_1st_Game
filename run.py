import tty, termios, sys, os
from Classes.Enemy import Enemy
from Classes.Hero import Hero
from Data.Levels import fields


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
        print(" ".join(line_f + ['{:^30}'.format(' ')] + line_stat))
    print("Press 'q' to Exit")
    print("'a' - move left")
    print("'d' - move right")
    print("'w' - move up")
    print("'s' - move down")


# Локация

status_bar = [
    ['+============+'],
    ['| HP = {:<6}|'],
    ['| MP = {:<6}|'],
    ['| Gl = {:<6}|'],
    ['| EX = {:<6}|'],
    ['| Lv = {:<6}|'],
    ['| Key= {:<6}|'],
    ['+============+']
]


def cont(field):
    if len(field) < len(status_bar):
        for j in range(len(status_bar)):
            try:
                field[j]
            except IndexError:
                field.append(['{:^15}'.format(' ')])
    elif len(field) > len(status_bar):
        for i in range(len(field)):
            try:
                status_bar[i]
            except IndexError:
                status_bar.append([' '])
# Инициализация
unit = Hero(fields, status_bar)
en = Enemy(fields)

def check(fields):
        if unit.location == 0:
            field = fields[0]
        elif unit.location == 1:
            field = fields[1]
        return field

status_bar = unit.status_bar
cls()
cont(check(fields))
render(check(fields), status_bar)

ch = ''

while ch != 'q':
    ch = getchar()
    unit.events(ch)
    unit.update()
    en.update()
    cls()
    cont(check(fields))
    cont(fields)
    render(check(fields), status_bar)
    print('You pressed', ch)
    print(unit.key)
    if unit.Hit_Points == 0 or unit.Hit_Points < 0:
        print('You die!!!')
        ch = 'q'

