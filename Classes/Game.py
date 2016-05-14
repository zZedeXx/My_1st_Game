import tty, termios, sys, os
from Classes.Enemy import Enemy
from Classes.Hero import Hero
from Data.inventory import Invent
from Data.Levels import fields
from Data import Objects
from Data.colors import *
from Data.status_bar import status_bar


class Game:
    def __init__(self):
        self.unit = Hero(fields, status_bar)
        self.inv = Invent(self.unit)
        self.enemy = Enemy(fields)
        self.invent = self.inv.inventory
        self.status_bar = self.unit.status_bar
        self.cls()

    def cont(self, field):
        """

        """
        if len(field) < len(self.status_bar):
            for j in range(len(self.status_bar)):
                try:
                    field[j], self.invent[j]
                except IndexError:
                    l = len(self.check(field))
                    field.append([l*' '])
        elif len(field) > len(self.status_bar) and len(field) > len(self.invent):
            for i in range(len(field)):
                try:
                    self.invent[i], self.status_bar[i]
                except IndexError:
                    self.status_bar.append([''])
                    self.invent.append([''])

    def getchar(self):
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

    def cls(self):
        """
        Очищаем консоль
        """
        os.system(['clear', 'cls'][os.name == 'nt'])

    def check(self, fields):
        """
        Опредиляет какой уровень отрисововать
        """
        return fields[self.unit.location]

    def render(self, ch, field, status_bar, inv):
        self.cls()
        self.cont(self.check(fields))
        for line_f, line_stat, line_inv in zip(field, status_bar, inv):
            render_line = ''
            for char in line_f:
                render_line += Objects.ICONS[char] if Objects.ICONS.get(char) else char
            for s_char in line_stat:
                render_line += LIGHT_GRAY(s_char)
            if ch == "i":
                for inv_char in line_inv:
                    render_line += LIGHT_GRAY(inv_char)
            print(BG_BLACK(render_line))
        print("Press 'q' to Exit")
        print(self.unit.key_left, " - move left")
        print("'d' - move right")
        print("'w' - move up")
        print("'s' - move down")

    def run(self):
        ch = ''
        while ch != 'q':
            ch = self.getchar()
            self.unit.events(ch)
            self.unit.update()
            self.enemy.AI()
            self.enemy.update()
            self.inv.draw_inv()
            self.render(ch, self.check(fields), self.status_bar, self.inv.inventory)
            print('You pressed', ascii(ch))
            if self.unit.Hit_Points == 0 or self.unit.Hit_Points < 0:
                print('You die!!!')
                ch = 'q'
            elif self.enemy.Hit_Points == 0 or self.enemy.Hit_Points < 0:
                self.enemy.alive = False

if __name__ == "__main__":
    game = Game()
    game.run()
