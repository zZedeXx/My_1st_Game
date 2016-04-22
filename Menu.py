import tty, termios, sys, os
from Data.menu import Menu


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

_menu_ = Menu()

cls()
_menu_.render()

while True:
    c = getchar()
    if _menu_.events(c):
        break
    cls()
    _menu_.render()
