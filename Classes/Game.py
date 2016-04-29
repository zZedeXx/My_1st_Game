import tty, termios, sys, os
from Classes.Enemy import Enemy
from Classes.Hero import Hero
from Data.Levels import fields
from Data import Objects
from Data.colors import *
from Data.status_bar import status_bar


class Game:
    def __init__(self):
        self.unit = Hero(fields, status_bar)
        # TODO: переименовать в enemy(complete)
        self.enemy = Enemy(fields)
        self.status_bar = self.unit.status_bar
        self.cls()

    def cont(self, field):
        """

        """
        if len(field) < len(self.status_bar):
            for j in range(len(self.status_bar)):
                try:
                    field[j]
                except IndexError:
                    l = len(self.check(field))
                    field.append([l*' '])
        elif len(field) > len(self.status_bar):
            for i in range(len(field)):
                try:
                    self.status_bar[i]
                except IndexError:
                    self.status_bar.append([''])

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

    def render(self, field, status_bar):
        self.cls()
        self.cont(self.check(fields))
        for line_f, line_stat in zip(field, status_bar):
            render_line = ''
            for char in line_f:
                render_line += Objects.ICONS[char] if Objects.ICONS.get(char) else char
            for s_char in line_stat:
                render_line += s_char
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
            self.render(self.check(fields), self.status_bar)
            print('You pressed', ascii(ch))
            print(self.unit.location)
            if self.unit.Hit_Points == 0 or self.unit.Hit_Points < 0:
                print('You die!!!')
                ch = 'q'
            elif self.enemy.Hit_Points == 0 or self.enemy.Hit_Points < 0:
                self.enemy.alive = False

if __name__ == "__main__":
    game = Game()
    game.run()
