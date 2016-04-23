import tty, termios, sys, os
from Classes.Enemy import Enemy
from Classes.Hero import Hero
from Data.Levels import fields


class Game:
    def __init__(self):
        self.status_bar = [
            ['╔═══════════╗'],
            ['║ HP = {:<5}║'],
            ['║ MP = {:<5}║'],
            ['║ Gl = {:<5}║'],
            ['║ EX = {:<5}║'],
            ['║ Lv = {:<5}║'],
            ['║ Key= {:<5}║'],
            ['╚═══════════╝']
        ]
        self.unit = Hero(fields, self.status_bar)
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
                    field.append(['{:^15}'.format(' ')])
        elif len(field) > len(self.status_bar):
            for i in range(len(field)):
                try:
                    self.status_bar[i]
                except IndexError:
                    self.status_bar.append([' '])

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

        """
        return fields[self.unit.location]

    def render(self, field, status_bar):
        self.cls()
        self.cont(self.check(fields))
        for line_f, line_stat in zip(field, status_bar):
            print(" ".join(line_f + ['{:^30}'.format(' ')] + line_stat))
        print("Press 'q' to Exit")
        print("'a' - move left")
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
            print(self.unit.key)
            if self.unit.Hit_Points == 0 or self.unit.Hit_Points < 0:
                print('You die!!!')
                ch = 'q'
            elif self.enemy.Hit_Points == 0 or self.enemy.Hit_Points < 0:
                self.enemy.alive = False

if __name__ == "__main__":
    game = Game()
    game.run()
